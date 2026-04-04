import os
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
    return {
        "business": business_name,
        "score": final_score,
        "flags": flags,
        "summary": ai_summary,
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
