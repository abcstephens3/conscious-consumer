import requests
from esg import ESG_DATA
from humanrights import HUMAN_RIGHTS_DATA

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
REVERSE_URL = "https://nominatim.openstreetmap.org/reverse"

HEADERS = {"User-Agent": "ConsciousConsumer/1.0"}

# Business categories to search for
SEARCH_CATEGORIES = [
    "supermarket",
    "fast_food",
    "restaurant",
    "bank",
    "fuel",
    "convenience",
    "department_store",
    "clothes"
]

def geocode_location(location):
    """Convert a city/state name to coordinates"""
    try:
        response = requests.get(
            NOMINATIM_URL,
            headers=HEADERS,
            params={
                "q": location,
                "format": "json",
                "limit": 1,
                "countrycodes": "us"
            }
        )
        results = response.json()
        if not results:
            return None
        return {
            "lat": float(results[0]["lat"]),
            "lon": float(results[0]["lon"]),
            "display_name": results[0]["display_name"]
        }
    except Exception as e:
        return None

def search_nearby_businesses(lat, lon, category, radius=5000):
    """Search for nearby businesses using Overpass API"""
    try:
        overpass_url = "https://overpass-api.de/api/interpreter"
        query = f"""
        [out:json][timeout:10];
        node["amenity"="{category}"]
          (around:{radius},{lat},{lon});
        out body 10;
        """
        response = requests.post(
            overpass_url,
            data=query,
            headers=HEADERS,
            timeout=15
        )
        data = response.json()
        return data.get("elements", [])
    except Exception as e:
        return []

def match_business_score(name):
    """Match a business name against our scoring datasets"""
    if not name:
        return None

    name_lower = name.lower().strip()

    # Check for partial matches in our datasets
    for key in ESG_DATA:
        key_words = key.split()
        if (name_lower == key or
            (len(key_words) > 1 and key in name_lower) or
            (len(key) > 6 and key in name_lower)):
            
            esg = ESG_DATA[key]
            hr = HUMAN_RIGHTS_DATA.get(key, {})

            base_score = 100
            base_score -= esg.get("score_impact", 0)
            base_score -= hr.get("score_impact", 0)

            return {
                "name": name,
                "score": max(base_score, 0),
                "esg_rating": esg.get("rating", "Unknown"),
                "hr_rating": hr.get("rating", "Unknown") if hr else "No data",
                "matched_key": key
            }
    return None

def get_ethical_alternatives(category_scores):
    """Find the best scoring businesses from our dataset"""
    alternatives = []
    seen = set()

    for key in ESG_DATA:
        if key in seen:
            continue
        esg = ESG_DATA[key]
        hr = HUMAN_RIGHTS_DATA.get(key, {})

        base_score = 100
        base_score -= esg.get("score_impact", 0)
        base_score -= hr.get("score_impact", 0)
        final_score = max(base_score, 0)

        if final_score >= 75:
            alternatives.append({
                "name": key.title(),
                "score": final_score,
                "esg_rating": esg.get("rating", "Unknown"),
            })
            seen.add(key)

    alternatives.sort(key=lambda x: x["score"], reverse=True)
    return alternatives[:8]

def get_local_awareness(location):
    """Main function - get local business awareness for a location"""
    try:
        # Step 1: Geocode the location
        coords = geocode_location(location)
        if not coords:
            return {
                "found": False,
                "message": f"Could not find location: {location}"
            }

        # Step 2: Search for nearby businesses
        found_businesses = []
        scored_businesses = []

        for category in SEARCH_CATEGORIES[:4]:  # Limit to 4 categories
            businesses = search_nearby_businesses(
                coords["lat"],
                coords["lon"],
                category
            )
            found_businesses.extend(businesses)

        # Step 3: Match against our scoring dataset
        seen_names = set()
        for business in found_businesses:
            tags = business.get("tags", {})
            name = tags.get("name", "")
            if not name or name in seen_names:
                continue
            seen_names.add(name)

            scored = match_business_score(name)
            if scored:
                scored_businesses.append(scored)

        # Sort by score
        scored_businesses.sort(key=lambda x: x["score"], reverse=True)

        # Step 4: Get ethical alternatives
        alternatives = get_ethical_alternatives(scored_businesses)

        return {
            "found": True,
            "location": coords["display_name"],
            "coordinates": {"lat": coords["lat"], "lon": coords["lon"]},
            "nearby_scored": scored_businesses[:10],
            "ethical_alternatives": alternatives,
            "total_found": len(found_businesses)
        }

    except Exception as e:
        return {
            "found": False,
            "message": f"Error looking up location: {str(e)}"
        }
