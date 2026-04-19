import requests
import os
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance in miles between two coordinates"""
    R = 3958.8
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return round(R * c, 1)
from esg import ESG_DATA
from humanrights import HUMAN_RIGHTS_DATA

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBalxLq35w_7SCawNXOq-xpzpd06cWUpyM")

def geocode_location(location):
    """Convert location name to coordinates using Google"""
    try:
        response = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json",
            params={
                "address": location,
                "key": GOOGLE_API_KEY
            }
        )
        data = response.json()
        if data["status"] != "OK":
            return None
        result = data["results"][0]
        lat = result["geometry"]["location"]["lat"]
        lon = result["geometry"]["location"]["lng"]
        display = result["formatted_address"]
        return {"lat": lat, "lon": lon, "display_name": display}
    except Exception as e:
        return None

def search_nearby_businesses(lat, lon, radius=2000):
    """Search for nearby businesses using Google Places"""
    try:
        businesses = []
        types = ["supermarket", "restaurant", "bank", "gas_station", "department_store"]
        
        for place_type in types:
            response = requests.get(
                "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
                params={
                    "location": f"{lat},{lon}",
                    "rankby": "distance",
                    "type": place_type,
                    "key": GOOGLE_API_KEY
                }
            )
            data = response.json()
            results = data.get("results", [])
            for r in results:
                r['_search_lat'] = lat
                r['_search_lon'] = lon
            businesses.extend(results)
        
        return businesses
    except Exception as e:
        return []

def match_business_score(name):
    """Match a business name against our scoring datasets"""
    if not name:
        return None
    import re
    name_lower = re.sub(r"['\-&.,]", "", name.lower().strip())
    name_lower = re.sub(r"\s+", " ", name_lower).strip()

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

def get_ethical_alternatives(scored_businesses):
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
    """Get local business awareness for a location string"""
    try:
        coords = geocode_location(location)
        if not coords:
            return {
                "found": False,
                "message": f"Could not find location: {location}"
            }
        return get_local_awareness_by_coords(coords["lat"], coords["lon"])
    except Exception as e:
        return {
            "found": False,
            "message": f"Error looking up location: {str(e)}"
        }

def get_local_awareness_by_coords(lat, lon):
    """Get local business awareness using exact coordinates"""
    try:
        businesses = search_nearby_businesses(lat, lon)

        seen_names = set()
        scored_businesses = []
        unrated_businesses = []

        for business in businesses:
            name = business.get("name", "")
            if not name or name in seen_names:
                continue
            seen_names.add(name)

            scored = match_business_score(name)
            if scored:
                scored_businesses.append(scored)
            else:
                unrated_businesses.append({
                    "name": name,
                    "score": None,
                    "esg_rating": "Unrated",
                    "hr_rating": "Unrated",
                    "matched_key": None
                })

        scored_businesses.sort(key=lambda x: x["score"], reverse=True)
        alternatives = get_ethical_alternatives(scored_businesses)

        return {
            "found": True,
            "location": f"{lat}, {lon}",
            "coordinates": {"lat": lat, "lon": lon},
            "nearby_scored": scored_businesses[:10],
            "nearby_unrated": unrated_businesses[:5],
            "ethical_alternatives": alternatives,
            "total_found": len(businesses)
        }

    except Exception as e:
        return {
            "found": False,
            "message": f"Error looking up location: {str(e)}"
        }
        
def get_safe_stops_near(lat, lon, categories, radius_miles=10, min_score=65):
    """Get safe stop recommendations near a waypoint"""
    import os, requests
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
    
    CATEGORY_TYPES = {
        "food": ["restaurant", "meal_takeaway", "fast_food"],
        "gas": ["gas_station"],
        "rest": ["rest_stop", "park"],
        "coffee": ["cafe"],
        "lodging": ["lodging"],
        "pharmacy": ["pharmacy", "drugstore"]
    }
    
    doj_url = "https://www.justice.gov/crt/search-cases-and-matters"
    radius_meters = int(radius_miles * 1609.34)
    place_types = []
    for cat in categories:
        place_types.extend(CATEGORY_TYPES.get(cat, []))
    
    if not place_types:
        place_types = ["restaurant", "gas_station", "cafe"]
    
    results = []
    seen_places = set()
    
    for place_type in place_types[:6]:
        try:
            response = requests.get(
                "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
                params={
                    "location": f"{lat},{lon}",
                    "radius": radius_meters,
                    "type": place_type,
                    "key": GOOGLE_KEY
                }
            )
            data = response.json()
            
            for place in data.get("results", [])[:5]:
                place_id = place.get("place_id")
                if place_id in seen_places:
                    continue
                seen_places.add(place_id)
                
                name = place.get("name", "")
                address = place.get("vicinity", "")
                google_rating = place.get("rating", None)
                
                # Check our database for score
                from esg import get_esg_rating
                from humanrights import get_human_rights_rating
                esg = get_esg_rating(name)
                hr = get_human_rights_rating(name)
                
                base = 100
                if esg.get("found") and esg.get("score_impact", 0) > 0:
                    base -= esg["score_impact"]
                if hr.get("found") and hr.get("score_impact", 0) > 0:
                    base -= hr["score_impact"]
                score = max(base, 0)
                
                # Get place details for attributes
                details_response = requests.get(
                    "https://maps.googleapis.com/maps/api/place/details/json",
                    params={
                        "place_id": place_id,
                        "fields": "name,formatted_address,rating,geometry,wheelchair_accessible_entrance",
                        "key": GOOGLE_KEY
                    }
                )
                details = details_response.json().get("result", {})
                
                place_lat = place["geometry"]["location"]["lat"]
                place_lon = place["geometry"]["location"]["lng"]
                
                # Calculate distance
                import math
                dlat = math.radians(place_lat - lat)
                dlon = math.radians(place_lon - lon)
                a = math.sin(dlat/2)**2 + math.cos(math.radians(lat)) * math.cos(math.radians(place_lat)) * math.sin(dlon/2)**2
                distance_miles = round(3959 * 2 * math.asin(math.sqrt(a)), 1)
                
                # Determine category label
                cat_label = place_type.replace("_", " ").title()
                if place_type in ["restaurant", "meal_takeaway", "fast_food"]:
                    cat_label = "Food"
                elif place_type == "gas_station":
                    cat_label = "Gas"
                elif place_type == "cafe":
                    cat_label = "Coffee"
                elif place_type == "lodging":
                    cat_label = "Lodging"
                elif place_type == "pharmacy":
                    cat_label = "Pharmacy"
                elif place_type in ["rest_stop", "park"]:
                    cat_label = "Rest Stop"
                
                # Only include if meets minimum score
                if score >= min_score:
                    results.append({
                        "name": name,
                        "address": address,
                        "category": cat_label,
                        "score": score,
                        "distance_miles": distance_miles,
                        "google_rating": google_rating,
                        "wheelchair_accessible": details.get("wheelchair_accessible_entrance", False),
                        "lgbtq_friendly": False,
                        "community_verified": False,
                        "place_id": place_id,
                        "lat": place_lat,
                        "lon": place_lon
                    })
        except Exception as e:
            continue
    
    # Sort by score descending, then distance
    results.sort(key=lambda x: (-x["score"], x["distance_miles"]))
    
    # Add community certification flags from Google Places attributes
    for result in results:
        tags = []
        if result.get("wheelchair_accessible"):
            tags.append("Wheelchair accessible")
        if result.get("lgbtq_friendly"):
            tags.append("LGBTQ+ friendly")
        if result.get("community_verified"):
            tags.append("Community verified")
        result["tags"] = tags
    
    return results[:8]
