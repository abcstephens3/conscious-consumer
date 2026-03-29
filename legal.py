import requests

import os
COURT_TOKEN = os.getenv("COURT_LISTENER_TOKEN", "")

def get_legal_records(business_name):
    try:
        response = requests.get(
            "https://www.courtlistener.com/api/rest/v4/search/",
            headers={"Authorization": f"Token {COURT_TOKEN}"},
            params={"q": business_name, "type": "d", "page_size": 10}
        )
        data = response.json()
        results = data.get("results", [])

        if not results:
            return {"found": False, "case_count": 0, "score_impact": 0}

        case_count = len(results)
        flagged_cases = [r.get("caseName") for r in results[:3]]

        if case_count >= 15:
            score_impact = 30
        elif case_count >= 10:
            score_impact = 20
        elif case_count >= 5:
            score_impact = 10
        else:
            score_impact = 5

        return {
            "found": True,
            "case_count": case_count,
            "score_impact": score_impact,
            "flagged_cases": flagged_cases
        }
    except Exception as e:
        return {"found": False, "case_count": 0, "score_impact": 0}
