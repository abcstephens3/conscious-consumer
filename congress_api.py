import os
import requests

CONGRESS_API_KEY = os.getenv("CONGRESS_API_KEY", "")
CONGRESS_BASE = "https://api.congress.gov/v3"

def search_member(name):
    """Search for a member of Congress by name"""
    try:
        response = requests.get(
            f"{CONGRESS_BASE}/member",
            params={
                "api_key": CONGRESS_API_KEY,
                "query": name,
                "limit": 5,
                "format": "json"
            },
            timeout=8
        )
        data = response.json()
        members = data.get("members", [])
        if not members:
            return {"found": False}
        
        # Try to match name more precisely
        name_parts = name.lower().split()
        for m in members:
            full = m.get('name', '').lower()
            # Require at least last name match
            if name_parts[-1] in full:
                return {"found": True, "member": m}
        
        # Only return first result if name parts strongly match
        if members:
            first = members[0].get('name', '').lower()
            if any(part in first for part in name_parts if len(part) > 3):
                return {"found": True, "member": members[0]}
        
        return {"found": False}
    
    except Exception as e:
        return {"found": False, "error": str(e)}

def get_member_details(bioguide_id):
    """Get detailed info for a member including sponsored bills"""
    try:
        response = requests.get(
            f"{CONGRESS_BASE}/member/{bioguide_id}",
            params={"api_key": CONGRESS_API_KEY, "format": "json"},
            timeout=8
        )
        data = response.json()
        return data.get("member", {})
    except:
        return {}

def get_sponsored_bills(bioguide_id):
    """Get bills sponsored by a member"""
    try:
        response = requests.get(
            f"{CONGRESS_BASE}/member/{bioguide_id}/sponsored-legislation",
            params={
                "api_key": CONGRESS_API_KEY,
                "limit": 10,
                "format": "json"
            },
            timeout=8
        )
        data = response.json()
        return data.get("sponsoredLegislation", [])
    except:
        return []

def get_cosponsored_bills(bioguide_id):
    """Get bills cosponsored by a member"""
    try:
        response = requests.get(
            f"{CONGRESS_BASE}/member/{bioguide_id}/cosponsored-legislation",
            params={
                "api_key": CONGRESS_API_KEY,
                "limit": 10,
                "format": "json"
            },
            timeout=8
        )
        data = response.json()
        return data.get("cosponsoredLegislation", [])
    except:
        return []

# Community-relevant bill keywords
COMMUNITY_BILL_KEYWORDS = {
    "bipoc": ["civil rights", "racial equity", "voting rights", "anti-discrimination", 
              "hate crimes", "police reform", "criminal justice reform"],
    "lgbtq": ["equality act", "lgbtq", "same-sex", "gender identity", "non-discrimination",
              "conversion therapy", "transgender"],
    "workers": ["minimum wage", "union", "labor", "worker protection", "wage theft",
                "collective bargaining", "workplace safety", "osha"],
    "disability": ["ada", "disability", "accessibility", "accommodations", 
                   "rehabilitation act", "special education"],
    "women": ["equal pay", "reproductive", "violence against women", "vawa", 
              "gender pay gap", "maternal health", "planned parenthood"]
}

def analyze_bills_for_communities(bills):
    """Check which community issues a member has sponsored legislation for"""
    community_support = {c: [] for c in COMMUNITY_BILL_KEYWORDS}
    
    for bill in bills:
        title = (bill.get("title", "") or "").lower()
        for community, keywords in COMMUNITY_BILL_KEYWORDS.items():
            if any(kw in title for kw in keywords):
                community_support[community].append({
                    "title": bill.get("title", ""),
                    "number": bill.get("number", ""),
                    "type": bill.get("type", ""),
                    "url": bill.get("url", "")
                })
    
    return community_support

def get_congress_member_data(name):
    """Full Congress.gov lookup for a politician"""
    search = search_member(name)
    if not search["found"]:
        return {"found": False}
    
    member = search["member"]
    bioguide_id = member.get("bioguideId")
    
    if not bioguide_id:
        return {"found": False}
    
    details = get_member_details(bioguide_id)
    sponsored = get_sponsored_bills(bioguide_id)
    cosponsored = get_cosponsored_bills(bioguide_id)
    
    all_bills = sponsored + cosponsored
    community_bills = analyze_bills_for_communities(all_bills)
    
    # Get terms info
    terms_raw = details.get("terms", {})
    if isinstance(terms_raw, list):
        terms = terms_raw
    elif isinstance(terms_raw, dict):
        terms = terms_raw.get("item", [])
    else:
        terms = []
    if isinstance(terms, dict):
        terms = [terms]
    current_term = terms[-1] if terms else {}
    
    return {
        "found": True,
        "name": details.get("directOrderName", member.get("name", "")),
        "bioguide_id": bioguide_id,
        "party": details.get("partyHistory", [{}])[-1].get("partyName", "") if details.get("partyHistory") else "",
        "state": current_term.get("stateCode", ""),
        "chamber": current_term.get("chamber", ""),
        "office": current_term.get("memberType", ""),
        "sponsored_count": len(sponsored),
        "cosponsored_count": len(cosponsored),
        "community_bills": community_bills,
        "recent_sponsored": sponsored[:5],
        "source_url": f"https://www.congress.gov/member/{bioguide_id}",
        "bioguide_url": f"https://bioguide.congress.gov/search/bio/{bioguide_id}"
    }
