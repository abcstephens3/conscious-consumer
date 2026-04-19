# OpenStreetMap Overpass API — Rest Stop and Amenity Data
# Free, no API key required
# Supplements Google Places for rest stops, parks, and accessible amenities

import requests
import math

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

def get_osm_rest_stops(lat, lon, radius_miles=15):
    """Get rest stops and accessible amenities near a waypoint via OpenStreetMap"""
    radius_meters = int(radius_miles * 1609.34)

    query = f"""
    [out:json][timeout:10];
    (
      node["highway"="rest_area"](around:{radius_meters},{lat},{lon});
      node["highway"="services"](around:{radius_meters},{lat},{lon});
      node["amenity"="toilets"]["wheelchair"="yes"](around:{radius_meters},{lat},{lon});
      node["amenity"="fuel"](around:{radius_meters},{lat},{lon});
      node["leisure"="park"](around:{radius_meters},{lat},{lon});
    );
    out body;
    """

    try:
        response = requests.post(OVERPASS_URL, data=query, timeout=12)
        data = response.json()
        elements = data.get("elements", [])

        results = []
        for el in elements[:10]:
            tags = el.get("tags", {})
            name = tags.get("name", "Rest Area")
            el_lat = el.get("lat", lat)
            el_lon = el.get("lon", lon)

            dlat = math.radians(el_lat - lat)
            dlon = math.radians(el_lon - lon)
            a = math.sin(dlat/2)**2 + math.cos(math.radians(lat)) * math.cos(math.radians(el_lat)) * math.sin(dlon/2)**2
            distance_miles = round(3959 * 2 * math.asin(math.sqrt(a)), 1)

            amenity = tags.get("amenity", tags.get("highway", "rest_area"))
            wheelchair = tags.get("wheelchair", "unknown")

            if amenity in ["rest_area", "services"]:
                category = "Rest Stop"
            elif amenity == "fuel":
                category = "Gas"
            elif amenity == "toilets":
                category = "Rest Stop"
            else:
                category = "Rest Stop"

            results.append({
                "name": name,
                "address": tags.get("addr:full", f"Near {lat:.2f}, {lon:.2f}"),
                "category": category,
                "score": 100,
                "distance_miles": distance_miles,
                "google_rating": None,
                "wheelchair_accessible": wheelchair in ["yes", "limited"],
                "lgbtq_friendly": False,
                "community_verified": False,
                "source": "OpenStreetMap",
                "lat": el_lat,
                "lon": el_lon
            })

        results.sort(key=lambda x: x["distance_miles"])
        return results[:5]

    except Exception as e:
        return []
