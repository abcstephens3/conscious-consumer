import requests

def get_fec_donations(business_name):
    try:
        # Search both candidates and committees
        committee_response = requests.get(
            "https://api.open.fec.gov/v1/committees/",
            params={
                "api_key": "DEMO_KEY",
                "q": business_name,
                "per_page": 10
            }
        )
        data = committee_response.json()
        results = data.get("results", [])

        if not results:
            return {"found": False, "total_donations": 0, "score_impact": 0}

        total = len(results)
        return {
            "found": True,
            "total_donations": total,
            "score_impact": min(total * 10, 40),
            "committees": [r.get("name") for r in results[:3]]
        }
    except Exception as e:
        return {"found": False, "total_donations": 0, "score_impact": 0}
        
def get_individual_donations(person_name):
    """Search FEC for individual political donations by a person"""
    try:
        response = requests.get(
            "https://api.open.fec.gov/v1/schedules/schedule_a/",
            params={
                "api_key": "DEMO_KEY",
                "contributor_name": person_name,
                "per_page": 20,
                "sort_hide_null": True,
                "sort": "-contribution_receipt_date"
            },
            timeout=8
        )
        data = response.json()
        results = data.get("results", [])
        
        if not results:
            return {"found": False}
        
        total_amount = sum(r.get("contribution_receipt_amount", 0) for r in results)
        
        # Party breakdown
        party_totals = {}
        recipients = []
        for r in results[:10]:
            party = r.get("committee", {}).get("party", "Unknown")
            amount = r.get("contribution_receipt_amount", 0)
            party_totals[party] = party_totals.get(party, 0) + amount
            recipients.append({
                "recipient": r.get("committee", {}).get("name", "Unknown"),
                "party": party,
                "amount": amount,
                "date": r.get("contribution_receipt_date", "")[:10] if r.get("contribution_receipt_date") else ""
            })
        
        return {
            "found": True,
            "total_donations": len(results),
            "total_amount": round(total_amount, 2),
            "party_breakdown": party_totals,
            "recipients": recipients[:8],
            "source_url": f"https://www.fec.gov/data/receipts/?contributor_name={person_name.replace(' ', '+')}"
        }
    
    except Exception as e:
        return {"found": False}        
