import os
import requests

def get_corpwatch_data(business_name):
    """Get corporate structure data from CorpWatch API"""
    try:
        API_KEY = os.getenv("CORPWATCH_API_KEY", "")
        
        response = requests.get(
            "http://api.corpwatch.org/companies.json",
            params={
                "company_name": business_name,
                "limit": 5,
                "key": API_KEY
            },
            timeout=8
        )
        
        data = response.json()
        
        if not data.get("result") or not data["result"].get("companies"):
            return {"found": False}
        
        companies = list(data["result"]["companies"].values())
        if not companies:
            return {"found": False}
        
        # Take best match
        company = companies[0]
        
        # Get subsidiary count
        cw_id = company.get("cw_id")
        subsidiary_count = 0
        parent_name = None
        countries = []
        
        if cw_id:
            # Get children (subsidiaries)
            children_response = requests.get(
                f"http://api.corpwatch.org/companies/{cw_id}/children.json",
                params={"key": API_KEY},
                timeout=8
            )
            children_data = children_response.json()
            if children_data.get("result", {}).get("companies"):
                subsidiary_count = len(children_data["result"]["companies"])
            
            # Get parents
            parents_response = requests.get(
                f"http://api.corpwatch.org/companies/{cw_id}/parents.json",
                params={"key": API_KEY},
                timeout=8
            )
            parents_data = parents_response.json()
            if parents_data.get("result", {}).get("companies"):
                parents = list(parents_data["result"]["companies"].values())
                if parents:
                    parent_name = parents[0].get("company_name")
            
            # Get locations
            locations_response = requests.get(
                f"http://api.corpwatch.org/companies/{cw_id}/locations.json",
                params={"key": API_KEY},
                timeout=8
            )
            locations_data = locations_response.json()
            if locations_data.get("result", {}).get("locations"):
                seen = set()
                for loc in locations_data["result"]["locations"].values():
                    country = loc.get("country_code", "")
                    if country and country not in seen:
                        seen.add(country)
                        countries.append(country)
        
        return {
            "found": True,
            "company_name": company.get("company_name"),
            "cw_id": cw_id,
            "sic_code": company.get("sic_code"),
            "sector": company.get("sector_name"),
            "industry": company.get("industry_name"),
            "subsidiary_count": subsidiary_count,
            "parent_company": parent_name,
            "countries": countries[:10],
            "country_count": len(countries),
            "top_parent_id": company.get("top_parent_id"),
            "source_url": f"http://api.corpwatch.org/companies/{cw_id}.json" if cw_id else None
        }
    
    except Exception as e:
        return {"found": False}
