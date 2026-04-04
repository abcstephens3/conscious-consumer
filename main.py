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

@app.get("/service_worker.js")
def serve_service_worker():
    return FileResponse("service_worker.js")      

@app.post("/search")
def search_business(business_name: str):
    fec_data = get_fec_donations(business_name)
    news_data = get_news_sentiment(business_name)
    legal_data = get_legal_records(business_name)
    esg_data = get_esg_rating(business_name)
    hr_data = get_human_rights_rating(business_name)
    base_score = 100
    flags = []
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
    
    # Check if this is a law enforcement agency
    pv_data = get_agency_violence_score(business_name)
    if pv_data["found"] and pv_data["score_impact"] > 0:
        base_score -= pv_data["score_impact"]
        flags.append(f"Police violence record: {pv_data['rating']}")
        flags.append(f"Total incidents: {pv_data['total_incidents']}")
        flags.append(f"Accountability rate: {pv_data['accountability_rate']}")
        flags.append(f"Unarmed victims: {pv_data['unarmed_rate']}")
    
    final_score = max(base_score, 0)
    ai_summary = generate_summary(
        business_name,
        final_score,
        flags,
        esg_data,
        hr_data,
        legal_data
    )
# Get ethical alternatives if score is low
    alternatives = []
    if final_score < 50:
        category = get_category(business_name)
        if category:
            alternatives = get_alternatives_in_category(category, business_name)

    return {
        "business": business_name,
        "score": final_score,
        "flags": flags,
        "summary": ai_summary,
        "alternatives": alternatives,
        "fec_data": fec_data,
        "news_data": news_data,
        "legal_data": legal_data,
        "esg_data": esg_data,
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
    
    return {
        "found": True,
        "location": result["formatted_address"],
        "coordinates": {"lat": lat, "lon": lon},
        "overall_rating": safety_data["overall"],
        "lgbtq": safety_data["lgbtq"],
        "racial": safety_data["racial"],
        "religious_minority": safety_data["religious_minority"],
        "disability": safety_data["disability"],
        "women": safety_data["women"],
        "police_violence": {
            "state": state_violence,
            "city": city_violence
        }
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
            clean_text = re.sub('<[^<]+?>', '', step["html_instructions"])
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
