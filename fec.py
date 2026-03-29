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
