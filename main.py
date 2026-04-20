import os
import requests
port = int(os.environ.get("PORT", 8000))
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fec import get_fec_donations
from news import get_news_sentiment
from legal import get_legal_records
from esg import get_esg_rating
from humanrights import get_human_rights_rating
from state_safety import get_state_safety
from police_violence import get_police_violence_by_state, get_police_violence_by_city, get_agency_violence_score
from local_awareness import get_local_awareness, get_local_awareness_by_coords
from ai_summary import generate_summary
from categories import get_category, get_alternatives_in_category
from eeoc import get_eeoc_data
from nlrb_data import get_nlrb_data
from osm_stops import get_osm_rest_stops
from map_data import get_map_data, get_map_lgbtq_rating
from corpwatch import get_corpwatch_data
from products import get_product_company


def get_google_reviews(business_name):
    """Get Google Places rating and review count"""
    try:
        GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/json",
            params={
                "input": business_name,
                "inputtype": "textquery",
                "fields": "name,rating,user_ratings_total,formatted_address",
                "key": GOOGLE_KEY
            }
        )
        data = response.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return {"found": False}
        place = candidates[0]
        rating = place.get("rating", None)
        total = place.get("user_ratings_total", 0)
        return {
            "found": True,
            "name": place.get("name"),
            "rating": rating,
            "total_reviews": total,
            "sentiment": "positive" if rating and rating >= 4.0 else "negative" if rating and rating < 3.0 else "mixed"
        }
    except Exception as e:
        return {"found": False}

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Conscious Consumer API is running"}
    
@app.get("/app")
def serve_frontend():
    return FileResponse("index.html")  
    
@app.get("/manifest.json")
def serve_manifest():
    return FileResponse("manifest.json")

@app.get("/favicon.ico")
def serve_favicon():
    return FileResponse("static/favicon.ico")

@app.get("/service_worker.js")
def serve_service_worker():
    return FileResponse("service_worker.js")      

@app.post("/search")
def search_business(business_name: str):
    # Check if search term is a product — redirect to parent company
    product_check = get_product_company(business_name)
    if product_check["found"]:
        original_product = business_name
        business_name = product_check["company"]
        product_redirect = {"found": True, "searched_product": original_product, "parent_company": product_check["company"]}
    else:
        product_redirect = {"found": False}
        
    fec_data = get_fec_donations(business_name)
    news_data = get_news_sentiment(business_name)
    legal_data = get_legal_records(business_name)
    esg_data = get_esg_rating(business_name)
    hr_data = get_human_rights_rating(business_name)
    google_reviews = get_google_reviews(business_name)
    eeoc_data = get_eeoc_data(business_name)
    nlrb_data = get_nlrb_data(business_name)
    corpwatch_data = get_corpwatch_data(business_name)
    
    base_score = 100
    flags = []
    
    # Factor NLRB into score
    if nlrb_data["found"] and nlrb_data["case_count"] > 0:
        base_score -= nlrb_data["score_impact"]
        flags.append(f"NLRB unfair labor practice cases: {nlrb_data['case_count']} charges filed")
        flags.append(f"NLRB summary: {nlrb_data['summary']}")

    if fec_data["found"]:
        base_score -= fec_data["score_impact"]
        flags.append("Political activity detected in FEC records")
    if news_data["found"] and news_data["negative_count"] > 0:
        base_score -= news_data["score_impact"]
        flags.append("Negative news coverage detected")
        for headline in news_data["flagged_headlines"]:
            if isinstance(headline, dict):
                flags.append(f"HEADLINE|{headline.get('title','')}|{headline.get('url','')}|{headline.get('source','')}")
            else:
                flags.append(f"Headline: {headline}")
    if legal_data["found"]:
        base_score -= legal_data["score_impact"]
        flags.append(f"Legal cases found in court records: {legal_data['case_count']} cases")
        for case in legal_data["flagged_cases"]:
            flags.append(f"Case: {case}")
    if esg_data["found"] and esg_data["score_impact"] > 0:
        base_score -= esg_data["score_impact"]
        flags.append(f"ESG rating: {esg_data.get('rating', 'Unknown')}")
    if hr_data["found"] and hr_data["score_impact"] > 0:
        base_score -= hr_data["score_impact"]
        flags.append(f"Human rights concerns: {hr_data['rating']}")
        for flag in hr_data["flags"]:
            flags.append(f"⚠️ {flag}")
   
    # Factor EEOC cases into score
    if eeoc_data["found"] and eeoc_data["case_count"] > 0:
        eeoc_impact = min(eeoc_data["case_count"] * 2, 20)
        base_score -= eeoc_impact
        flags.append(f"EEOC discrimination cases on record: {eeoc_data['case_count']} cases")
        flags.append(f"Communities affected: {', '.join(eeoc_data['communities']).upper()}")
        flags.append(f"EEOC summary: {eeoc_data['summary']}")

    # Factor Google reviews into score
    if google_reviews["found"] and google_reviews["rating"]:
        if google_reviews["rating"] < 2.5:
            base_score -= 15
            flags.append(f"Poor consumer ratings: {google_reviews['rating']}/5 stars ({google_reviews['total_reviews']:,} reviews)")
        elif google_reviews["rating"] < 3.5:
            base_score -= 5
            flags.append(f"Below average consumer ratings: {google_reviews['rating']}/5 stars ({google_reviews['total_reviews']:,} reviews)")

    # Check if this is a law enforcement agency
    pv_data = get_agency_violence_score(business_name)
    if pv_data["found"] and pv_data["score_impact"] > 0:
        base_score -= pv_data["score_impact"]
        flags.append(f"Police violence record: {pv_data['rating']}")
        flags.append(f"Total incidents: {pv_data['total_incidents']}")
        flags.append(f"Accountability rate: {pv_data['accountability_rate']}")
        flags.append(f"Unarmed victims: {pv_data['unarmed_rate']}")

    final_score = max(base_score, 0)
    ai_summary = generate_summary(business_name, final_score, flags, esg_data, hr_data, legal_data)

    # Get ethical alternatives if score is low
    alternatives = []
    if final_score < 50:
        category = get_category(business_name)
        if category:
            alternatives = get_alternatives_in_category(category, business_name)

    # Build source URLs
    bbb_url = f"https://www.bbb.org/search?find_text={business_name.replace(' ', '+')}"
    glassdoor_url = f"https://www.glassdoor.com/Search/results.htm?keyword={business_name.replace(' ', '+')}"
    google_reviews_url = f"https://www.google.com/search?q={business_name.replace(' ', '+')}+reviews"

    # Build community-specific flags
    all_flags_text = ' '.join(flags).lower()

    community_flags = {
        "bipoc": {
            "has_issue": False,
            "text": "No specific BIPOC concerns found in our database",
            "sources": [
                {"label": "BBB Profile", "url": bbb_url},
                {"label": "Google Reviews", "url": google_reviews_url},
                {"label": "Search Court Records", "url": f"https://www.courtlistener.com/?q={business_name.replace(' ', '+')}+discrimination&type=r"}
            ]
        },
        "lgbtq": {
            "has_issue": False,
            "text": "No specific LGBTQ+ concerns found in our database",
            "sources": [
                {"label": "View FEC Records", "url": f"https://www.fec.gov/data/committees/?q={business_name.replace(' ', '+')}"},
                {"label": "BBB Profile", "url": bbb_url},
                {"label": "Google Reviews", "url": google_reviews_url}
            ]
        },
        "women": {
            "has_issue": False,
            "text": "No specific concerns for women found in our database",
            "sources": [
                {"label": "BBB Profile", "url": bbb_url},
                {"label": "Google Reviews", "url": google_reviews_url},
                {"label": "Search Court Records", "url": f"https://www.courtlistener.com/?q={business_name.replace(' ', '+')}+gender+discrimination&type=r"}
            ]
        },
        "workers": {
            "has_issue": False,
            "text": "No specific worker concerns found in our database",
            "sources": [
                {"label": "Glassdoor Reviews", "url": glassdoor_url},
                {"label": "BBB Profile", "url": bbb_url},
                {"label": "Google Reviews", "url": google_reviews_url}
            ]
        },
        "disability": {
            "has_issue": False,
            "text": "No specific disability concerns found in our database",
            "sources": [
                {"label": "BBB Profile", "url": bbb_url},
                {"label": "Google Reviews", "url": google_reviews_url},
                {"label": "Search Court Records", "url": f"https://www.courtlistener.com/?q={business_name.replace(' ', '+')}+ADA+accessibility&type=r"}
            ]
        }
    }

    # BIPOC
    bipoc_triggers = ['indigenous', 'racial', 'discrimination', 'civil rights', 'naacp', 'minority', 'race']
    if any(t in all_flags_text for t in bipoc_triggers) or (eeoc_data.get("found") and "bipoc" in eeoc_data.get("communities", [])):
        community_flags["bipoc"]["has_issue"] = True
        community_flags["bipoc"]["text"] = "Racial discrimination concerns found in court, EEOC, or news records"
        eeoc_cases = [{"label": c["title"], "url": c["url"]} for c in eeoc_data.get("cases", [])] if eeoc_data.get("found") else []
        community_flags["bipoc"]["sources"] = eeoc_cases + [
            {"label": "Search EEOC Records", "url": f"https://www.eeoc.gov/newsroom/search?query={business_name.replace(' ', '+')}+race"},
            {"label": "Search Court Records", "url": f"https://www.courtlistener.com/?q={business_name.replace(' ', '+')}+discrimination&type=r"},
            {"label": "DOJ Civil Rights Cases", "url": f"https://www.justice.gov/crt/search-cases-and-matters?search={business_name.replace(' ', '+')}"},
            {"label": "BBB Profile", "url": bbb_url}
        ]

    # LGBTQ+
    lgbtq_triggers = ['lgbtq', 'gay', 'transgender', 'pride', 'sexual orientation', 'gender identity', 'hrc', 'anti-gay', 'conversion']
    if any(t in all_flags_text for t in lgbtq_triggers):
        community_flags["lgbtq"]["has_issue"] = True
        community_flags["lgbtq"]["text"] = "LGBTQ+ concerns or political opposition documented"
        community_flags["lgbtq"]["sources"] = [
            {"label": "View FEC Records", "url": f"https://www.fec.gov/data/committees/?q={business_name.replace(' ', '+')}"},
            {"label": "HRC Scorecard", "url": "https://www.hrc.org/resources/corporate-equality-index"},
            {"label": "BBB Profile", "url": bbb_url},
            {"label": "DOJ Civil Rights Cases", "url": f"https://www.justice.gov/crt/search-cases-and-matters?search={business_name.replace(' ', '+')}"},
            {"label": "Search News", "url": f"https://news.google.com/search?q={business_name.replace(' ', '+')}+LGBTQ"}
        ]

    # Women
    women_triggers = ['women', 'gender pay', 'sexual harassment', 'abortion', 'reproductive', 'maternity', 'gender discrimination']
    if any(t in all_flags_text for t in women_triggers) or (eeoc_data.get("found") and "women" in eeoc_data.get("communities", [])):
        community_flags["women"]["has_issue"] = True
        community_flags["women"]["text"] = "Gender discrimination or workplace concerns found in EEOC or court records"
        eeoc_cases = [{"label": c["title"], "url": c["url"]} for c in eeoc_data.get("cases", [])] if eeoc_data.get("found") else []
        community_flags["women"]["sources"] = eeoc_cases + [
            {"label": "Search EEOC Records", "url": f"https://www.eeoc.gov/newsroom/search?query={business_name.replace(' ', '+')}+gender"},
            {"label": "Search Court Records", "url": f"https://www.courtlistener.com/?q={business_name.replace(' ', '+')}+gender+discrimination&type=r"},
            {"label": "DOJ Civil Rights Cases", "url": f"https://www.justice.gov/crt/search-cases-and-matters?search={business_name.replace(' ', '+')}"},
            {"label": "BBB Profile", "url": bbb_url}
        ]

    # Workers
    worker_triggers = ['labor', 'worker', 'wage', 'union', 'employee', 'workplace', 'safety violation', 'osha', 'wage theft', 'nlrb']
    if any(t in all_flags_text for t in worker_triggers) or (nlrb_data.get("found") and nlrb_data.get("case_count", 0) > 0):
        community_flags["workers"]["has_issue"] = True
        community_flags["workers"]["text"] = "Labor violations or worker safety issues on record"
        nlrb_sources = nlrb_data.get("sources", []) if nlrb_data.get("found") else []
        community_flags["workers"]["sources"] = nlrb_sources + [
            {"label": "NLRB Case Search", "url": f"https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3A{business_name.replace(' ', '+')}"},
            {"label": "OSHA Records", "url": f"https://www.osha.gov/pls/imis/establishment.search?p_logger=1&establishment={business_name.replace(' ', '+')}"},
            {"label": "Search Court Records", "url": f"https://www.courtlistener.com/?q={business_name.replace(' ', '+')}+labor+violation&type=r"},
            {"label": "Glassdoor Reviews", "url": glassdoor_url},
            {"label": "BBB Profile", "url": bbb_url},
            {"label": "DOJ Civil Rights Cases", "url": f"https://www.justice.gov/crt/search-cases-and-matters?search={business_name.replace(' ', '+')}"},
            {"label": "Search News", "url": f"https://news.google.com/search?q={business_name.replace(' ', '+')}+labor+violations"}
        ]
    else:
        community_flags["workers"]["sources"] = [
            {"label": "NLRB Case Search", "url": f"https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3A{business_name.replace(' ', '+')}"},
            {"label": "Glassdoor Reviews", "url": glassdoor_url},
            {"label": "BBB Profile", "url": bbb_url}
        ]

    # Disability
    disability_triggers = ['disability', 'ada', 'accessibility', 'accommodation']
    if any(t in all_flags_text for t in disability_triggers) or (eeoc_data.get("found") and "disability" in eeoc_data.get("communities", [])):
        community_flags["disability"]["has_issue"] = True
        community_flags["disability"]["text"] = "ADA or disability discrimination concerns found in EEOC or court records"
        eeoc_cases = [{"label": c["title"], "url": c["url"]} for c in eeoc_data.get("cases", [])] if eeoc_data.get("found") else []
        community_flags["disability"]["sources"] = eeoc_cases + [
            {"label": "Search EEOC Records", "url": f"https://www.eeoc.gov/newsroom/search?query={business_name.replace(' ', '+')}+disability"},
            {"label": "ADA.gov Records", "url": "https://www.ada.gov/"},
            {"label": "DOJ Civil Rights Cases", "url": f"https://www.justice.gov/crt/search-cases-and-matters?search={business_name.replace(' ', '+')}"},
            {"label": "BBB Profile", "url": bbb_url}
        ]

    # Add news headline URLs to workers sources if available
    if news_data.get("found") and news_data.get("flagged_headlines"):
        for headline in news_data["flagged_headlines"]:
            if isinstance(headline, dict) and headline.get("url"):
                community_flags["workers"]["sources"].append({
                    "label": headline.get("source", "News Article"),
                    "url": headline["url"]
                })

    return {
        "business": business_name,
        "score": final_score,
        "flags": flags,
        "summary": ai_summary,
        "alternatives": alternatives,
        "community_flags": community_flags,
        "google_reviews": google_reviews,
        "eeoc_data": eeoc_data,
        "nlrb_data": nlrb_data,
        "corpwatch_data": corpwatch_data,
        "fec_data": fec_data,
        "news_data": news_data,
        "legal_data": legal_data,
        "esg_data": esg_data,
        "product_redirect": product_redirect,
        "human_rights_data": hr_data
    }

@app.post("/travel")
def travel_safety(location: str):
    safety_data = get_state_safety(location)

    # Parse city and state from input
    parts = [p.strip() for p in location.split(",")]
    city_data = {"found": False}

    if len(parts) >= 2:
        city = parts[0]
        state = parts[-1]
        city_data = get_police_violence_by_city(city, state)
        state_violence = get_police_violence_by_state(state)
    else:
        state_violence = get_police_violence_by_state(location)

    if not safety_data["found"]:
        return {
            "location": location,
            "found": False,
            "message": "Location not found. Try entering a US state name like 'Florida' or 'Texas'."
        }

    return {
        "location": location,
        "found": True,
        "overall_rating": safety_data["overall"],
        "lgbtq": safety_data["lgbtq"],
        "racial": safety_data["racial"],
        "religious_minority": safety_data["religious_minority"],
        "disability": safety_data["disability"],
        "women": safety_data["women"],
        "police_violence": {
            "state": state_violence,
            "city": city_data
        }
    }

@app.post("/local_by_coords")
def local_by_coords(lat: float, lon: float):
    from local_awareness import get_local_awareness_by_coords
    data = get_local_awareness_by_coords(lat, lon)
    return data
  
@app.post("/nearest_location")
def nearest_location(business_name: str, lat: float, lon: float):
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
        params={
            "location": f"{lat},{lon}",
            "rankby": "distance",
            "keyword": business_name,
            "key": GOOGLE_KEY
        }
    )
    data = response.json()
    results = data.get("results", [])
    if not results:
        return {"found": False, "message": f"No {business_name} locations found nearby"}
    
    nearest = results[0]
    return {
        "found": True,
        "name": nearest.get("name"),
        "address": nearest.get("vicinity"),
        "lat": nearest["geometry"]["location"]["lat"],
        "lon": nearest["geometry"]["location"]["lng"],
        "place_id": nearest.get("place_id")
    }

@app.post("/submit_company")
def submit_company(
    company_name: str,
    category: str,
    website: str = "",
    notes: str = ""
):
    import json
    from datetime import datetime
    
    submission = {
        "company_name": company_name,
        "category": category,
        "website": website,
        "notes": notes,
        "submitted_at": datetime.now().isoformat()
    }
    
    try:
        try:
            with open("submissions.json", "r") as f:
                submissions = json.load(f)
        except:
            submissions = []
        
        submissions.append(submission)
        
        with open("submissions.json", "w") as f:
            json.dump(submissions, f, indent=2)
        
        return {"success": True, "message": f"Thank you! {company_name} has been submitted for review."}
    except Exception as e:
        return {"success": False, "message": "Could not save submission. Please try again."}  

@app.get("/admin/submissions")
def view_submissions(key: str = ""):
    import json
    
    if key != os.getenv("ADMIN_KEY", "consciousconsumer2024"):
        return {"error": "Unauthorized"}
    
    try:
        with open("submissions.json", "r") as f:
            submissions = json.load(f)
        return {"total": len(submissions), "submissions": submissions}
    except:
        return {"total": 0, "submissions": []}
    
@app.post("/local")
def local_awareness(location: str):
    data = get_local_awareness(location)
    return data    
    
@app.post("/travel_by_address")
def travel_by_address(address: str):
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
    
    # Geocode the address to get coordinates and state
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params={"address": address, "key": GOOGLE_KEY}
    )
    data = response.json()
    
    if not data.get("results"):
        return {"found": False, "message": "Address not found"}
    
    result = data["results"][0]
    lat = result["geometry"]["location"]["lat"]
    lon = result["geometry"]["location"]["lng"]
    
    # Extract state from address components
    state_name = ""
    city_name = ""
    for component in result["address_components"]:
        if "administrative_area_level_1" in component["types"]:
            state_name = component["long_name"]
        if "locality" in component["types"]:
            city_name = component["long_name"]
    
    location = f"{city_name}, {state_name}" if city_name else state_name
    
    # Get safety ratings by state
    safety_data = get_state_safety(state_name)
    
    # Parse city/state for police violence
    parts = [p.strip() for p in location.split(",")]
    city_violence = {"found": False}
    if len(parts) >= 2:
        city_violence = get_police_violence_by_city(parts[0], parts[-1])
    state_violence = get_police_violence_by_state(state_name)
    
    if not safety_data["found"]:
        return {"found": False, "message": f"No safety data for {state_name}"}
    
    map_data = get_map_data(state_name)
    
    return {
        "found": True,
        "location": result["formatted_address"],
        "coordinates": {"lat": lat, "lon": lon},
        "overall_rating": safety_data.get("overall", "Unknown"),
        "lgbtq": safety_data.get("lgbtq", {}),
        "racial": safety_data.get("racial", {}),
        "religious_minority": safety_data.get("religious_minority", {}),
        "disability": safety_data.get("disability", {}),
        "women": safety_data.get("women", {}),
        "police_violence": {
            "state": state_violence,
            "city": city_violence
        },
        "map_data": map_data if map_data.get("found") else None
    }    
    
@app.post("/route_safety")
def route_safety(origin: str, destination: str):
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
    
    # Get route from Google Directions API
    response = requests.get(
        "https://maps.googleapis.com/maps/api/directions/json",
        params={
            "origin": origin,
            "destination": destination,
            "key": GOOGLE_KEY
        }
    )
    data = response.json()
    
    if data.get("status") != "OK":
        return {"found": False, "message": "Could not find route between those locations"}
    
    route = data["routes"][0]
    legs = route["legs"]
    
    # Extract states from the route
    states_on_route = []
    seen_states = set()
    
    for leg in legs:
        for step in leg["steps"]:
            # Get location of each step
            lat = step["end_location"]["lat"]
            lon = step["end_location"]["lng"]
            
            # Reverse geocode to get state
            geo_response = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json",
                params={
                    "latlng": f"{lat},{lon}",
                    "result_type": "administrative_area_level_1",
                    "key": GOOGLE_KEY
                }
            )
            geo_data = geo_response.json()
            
            if geo_data.get("results"):
                for component in geo_data["results"][0]["address_components"]:
                    if "administrative_area_level_1" in component["types"]:
                        state_name = component["long_name"]
                        if state_name not in seen_states:
                            seen_states.add(state_name)
                            safety = get_state_safety(state_name)
                            states_on_route.append({
                                "state": state_name,
                                "overall": safety.get("overall", "Unknown") if safety.get("found") else "Unknown",
                                "lgbtq": safety.get("lgbtq", {}).get("rating", "Unknown") if safety.get("found") else "Unknown",
                                "racial": safety.get("racial", {}).get("rating", "Unknown") if safety.get("found") else "Unknown",
                                "women": safety.get("women", {}).get("rating", "Unknown") if safety.get("found") else "Unknown",
                                "advisories": safety.get("lgbtq", {}).get("advisories", []) if safety.get("found") else []
                            })
    
    # Calculate total distance and duration
    total_distance = sum(leg["distance"]["value"] for leg in legs)
    total_duration = sum(leg["duration"]["value"] for leg in legs)
    distance_miles = round(total_distance * 0.000621371, 1)
    duration_hours = round(total_duration / 3600, 1)
    
    # Count high risk states
    high_risk = [s for s in states_on_route if "High" in s["overall"] or "Severe" in s["overall"]]
    
    # Build directions with safety overlays
    directions = []
    seen_direction_states = set()
    
    for leg in route["legs"]:
        for step in leg["steps"]:
            import re
            clean_text = re.sub('<[^<]+?>', ' ', step["html_instructions"]).strip()
            clean_text = re.sub(r'\s+', ' ', clean_text)
            distance = step["distance"]["text"]
            
            step_lat = step["end_location"]["lat"]
            step_lon = step["end_location"]["lng"]
            
            geo_response = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json",
                params={
                    "latlng": f"{step_lat},{step_lon}",
                    "result_type": "administrative_area_level_1",
                    "key": GOOGLE_KEY
                }
            )
            geo_data = geo_response.json()
            
            if geo_data.get("results"):
                for component in geo_data["results"][0]["address_components"]:
                    if "administrative_area_level_1" in component["types"]:
                        step_state = component["long_name"]
                        if step_state not in seen_direction_states:
                            seen_direction_states.add(step_state)
                            safety = get_state_safety(step_state)
                            overall = safety.get("overall", "") if safety.get("found") else ""
                            if "High" in overall or "Severe" in overall:
                                directions.append({
                                    "type": "warning",
                                    "text": f"Entering {step_state} — {overall} state. Review safety ratings."
                                })
            
            directions.append({
                "type": "step",
                "text": clean_text,
                "distance": distance
            })

    return {
        "found": True,
        "origin": legs[0]["start_address"],
        "destination": legs[-1]["end_address"],
        "distance_miles": distance_miles,
        "duration_hours": duration_hours,
        "states_on_route": states_on_route,
        "high_risk_states": len(high_risk),
        "route_summary": route["summary"],
        "directions": directions
    
    }
    
@app.post("/route_safe_stops")
def route_safe_stops(
    origin: str,
    destination: str,
    interval_hours: float = 4.0,
    categories: str = "food,gas,rest"
):
    import requests, os
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
    
    # Get route from Google
    response = requests.get(
        "https://maps.googleapis.com/maps/api/directions/json",
        params={
            "origin": origin,
            "destination": destination,
            "key": GOOGLE_KEY
        }
    )
    data = response.json()
    
    if data.get("status") != "OK":
        return {"found": False, "message": "Could not find route"}
    
    route = data["routes"][0]
    legs = route["legs"]
    total_duration_seconds = sum(leg["duration"]["value"] for leg in legs)
    total_hours = total_duration_seconds / 3600
    
    # Build list of steps with cumulative time
    steps_with_time = []
    cumulative = 0
    for leg in legs:
        for step in leg["steps"]:
            cumulative += step["duration"]["value"] / 3600
            steps_with_time.append({
                "cumulative_hours": cumulative,
                "lat": step["end_location"]["lat"],
                "lon": step["end_location"]["lng"]
            })
    
    # Calculate waypoint times
    waypoint_times = []
    current = interval_hours
    while current < total_hours - 0.5:
        waypoint_times.append(round(current, 1))
        current += interval_hours
    
    if not waypoint_times:
        waypoint_times = [round(total_hours / 2, 1)]
    
    # Find closest step to each waypoint time
    cats = [c.strip() for c in categories.split(",")]
    from local_awareness import get_safe_stops_near
    
    waypoints = []
    for target_time in waypoint_times:
        closest = min(steps_with_time, key=lambda s: abs(s["cumulative_hours"] - target_time))
        
        # Reverse geocode to get city name
        geo = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json",
            params={
                "latlng": f"{closest['lat']},{closest['lon']}",
                "result_type": "locality",
                "key": GOOGLE_KEY
            }
        )
        geo_data = geo.json()
        city = "Along your route"
        if geo_data.get("results"):
            city = geo_data["results"][0].get("formatted_address", "Along your route")
        
        stops = get_safe_stops_near(
            closest["lat"], closest["lon"],
            cats, radius_miles=15, min_score=65
        )
        
        # Supplement with OSM rest stops if rest category selected
        if "rest" in cats:
            osm_stops = get_osm_rest_stops(closest["lat"], closest["lon"], radius_miles=15)
            existing_names = {s["name"].lower() for s in stops}
            for osm in osm_stops:
                if osm["name"].lower() not in existing_names:
                    stops.append(osm)
            stops.sort(key=lambda x: (-x["score"], x["distance_miles"]))
            stops = stops[:8]
        
        waypoints.append({
            "hours_in": target_time,
            "city": city,
            "lat": closest["lat"],
            "lon": closest["lon"],
            "stops": stops
        })
    
    return {
        "found": True,
        "total_hours": round(total_hours, 1),
        "interval_hours": interval_hours,
        "waypoints": waypoints
    }    
