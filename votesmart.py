import os
import requests

VOTESMART_API_KEY = os.getenv("VOTESMART_API_KEY", "")
VOTESMART_BASE = "http://api.votesmart.org"

def search_candidate(name):
    """Search for a politician by name"""
    try:
        response = requests.get(
            f"{VOTESMART_BASE}/candidates.getByLastname",
            params={
                "key": VOTESMART_API_KEY,
                "lastName": name.split()[-1],
                "o": "JSON"
            },
            timeout=8
        )
        data = response.json()
        candidates = data.get("candidateList", {}).get("candidate", [])
        if isinstance(candidates, dict):
            candidates = [candidates]
        
        # Filter to current officeholders
        current = [c for c in candidates if c.get("electionStatus") in ["W", "I"] or c.get("officeId")]
        if not current:
            current = candidates
        
        if not current:
            return {"found": False}
        
        # Try to match full name
        name_lower = name.lower()
        for c in current:
            full = f"{c.get('firstName','')} {c.get('lastName','')}".lower()
            if name_lower in full or full in name_lower:
                return {"found": True, "candidate": c}
        
        return {"found": True, "candidate": current[0]}
    
    except Exception as e:
        return {"found": False, "error": str(e)}

def get_candidate_bio(candidate_id):
    """Get biographical info for a candidate"""
    try:
        response = requests.get(
            f"{VOTESMART_BASE}/candidatebio.getBio",
            params={"key": VOTESMART_API_KEY, "candidateId": candidate_id, "o": "JSON"},
            timeout=8
        )
        data = response.json()
        return data.get("bio", {})
    except:
        return {}

def get_interest_group_ratings(candidate_id):
    """Get interest group ratings for a candidate"""
    try:
        response = requests.get(
            f"{VOTESMART_BASE}/rating.getCandidateRating",
            params={"key": VOTESMART_API_KEY, "candidateId": candidate_id, "o": "JSON"},
            timeout=8
        )
        data = response.json()
        ratings = data.get("candidateRating", {}).get("rating", [])
        if isinstance(ratings, dict):
            ratings = [ratings]
        return ratings
    except:
        return []

def get_votes(candidate_id):
    """Get recent votes for a candidate"""
    try:
        response = requests.get(
            f"{VOTESMART_BASE}/votes.getByOfficial",
            params={
                "key": VOTESMART_API_KEY,
                "candidateId": candidate_id,
                "o": "JSON"
            },
            timeout=8
        )
        data = response.json()
        bills = data.get("bills", {}).get("bill", [])
        if isinstance(bills, dict):
            bills = [bills]
        return bills[:20]
    except:
        return []

# Interest groups we care about mapped to communities
COMMUNITY_ORGS = {
    "bipoc": ["NAACP", "National Urban League", "Leadership Conference on Civil Rights"],
    "lgbtq": ["Human Rights Campaign", "HRC", "GLAAD", "Equality Federation"],
    "workers": ["AFL-CIO", "SEIU", "United Auto Workers", "Teamsters", "NEA"],
    "disability": ["American Association of People with Disabilities", "AAPD", "National Council on Disability"],
    "women": ["National Organization for Women", "NOW", "NARAL", "Planned Parenthood"]
}

def get_politician_data(name):
    """Full politician lookup — search, bio, ratings, votes"""
    search = search_candidate(name)
    if not search["found"]:
        return {"found": False}
    
    candidate = search["candidate"]
    candidate_id = candidate.get("candidateId")
    
    if not candidate_id:
        return {"found": False}
    
    bio = get_candidate_bio(candidate_id)
    ratings = get_interest_group_ratings(candidate_id)
    votes = get_votes(candidate_id)
    
    # Parse community ratings
    community_ratings = {
        "bipoc": None, "lgbtq": None, "workers": None,
        "disability": None, "women": None
    }
    
    relevant_ratings = []
    for rating in ratings:
        org_name = rating.get("ratingName", "") or rating.get("sigId", "")
        rating_text = rating.get("rating", "")
        
        for community, orgs in COMMUNITY_ORGS.items():
            if any(org.lower() in org_name.lower() for org in orgs):
                try:
                    score = float(str(rating_text).replace("%", ""))
                    community_ratings[community] = score
                    relevant_ratings.append({
                        "org": org_name,
                        "rating": rating_text,
                        "community": community
                    })
                except:
                    pass
    
    # Calculate score
    base_score = 100
    
    # Deduct based on community org ratings
    for community, score in community_ratings.items():
        if score is not None and score < 50:
            deduction = int((50 - score) / 50 * 20)
            base_score -= deduction
    
    # Check missed votes from bio
    missed_votes_pct = 0
    office_info = bio.get("office", {})
    
    final_score = max(base_score, 0)
    
    candidate_info = bio.get("candidate", candidate)
    
    return {
        "found": True,
        "name": f"{candidate_info.get('firstName', '')} {candidate_info.get('lastName', '')}".strip(),
        "party": candidate_info.get("political", {}).get("party", candidate.get("party", "")),
        "state": candidate_info.get("political", {}).get("state", candidate.get("stateId", "")),
        "office": office_info.get("name", candidate.get("electionOffice", "")),
        "candidate_id": candidate_id,
        "score": final_score,
        "community_ratings": community_ratings,
        "relevant_ratings": relevant_ratings,
        "recent_votes": votes[:10],
        "photo_url": f"https://static.votesmart.org/canphoto/{candidate_id}.jpg",
        "source_url": f"https://votesmart.org/candidate/{candidate_id}"
    }
