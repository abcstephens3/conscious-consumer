import pandas as pd
import os
import requests as req

DATASET_LOADED = False
df = None

def download_dataset():
    url = "https://mappingpoliceviolence.us/s/MPVDatasetDownload.xlsx"
    path = "mpv_data.xlsx"
    if not os.path.exists(path):
        print("Downloading MPV dataset...")
        r = req.get(url, timeout=30)
        with open(path, 'wb') as f:
            f.write(r.content)
        print("MPV dataset downloaded.")

try:
    download_dataset()
    df = pd.read_excel('mpv_data.xlsx')
    df.columns = df.columns.str.strip()
    df['State'] = df['State'].str.strip().str.upper()
    df['City'] = df['City'].str.strip().str.lower()
    DATASET_LOADED = True
except Exception as e:
    print(f"Warning: Could not load MPV dataset: {e}")
    DATASET_LOADED = False
    df = None

STATE_ABBREVS = {
    'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR',
    'CALIFORNIA': 'CA', 'COLORADO': 'CO', 'CONNECTICUT': 'CT', 'DELAWARE': 'DE',
    'FLORIDA': 'FL', 'GEORGIA': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID',
    'ILLINOIS': 'IL', 'INDIANA': 'IN', 'IOWA': 'IA', 'KANSAS': 'KS',
    'KENTUCKY': 'KY', 'LOUISIANA': 'LA', 'MAINE': 'ME', 'MARYLAND': 'MD',
    'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN', 'MISSISSIPPI': 'MS',
    'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV',
    'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC', 'NORTH DAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK',
    'OREGON': 'OR', 'PENNSYLVANIA': 'PA', 'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX', 'UTAH': 'UT',
    'VERMONT': 'VT', 'VIRGINIA': 'VA', 'WASHINGTON': 'WA', 'WEST VIRGINIA': 'WV',
    'WISCONSIN': 'WI', 'WYOMING': 'WY', 'DISTRICT OF COLUMBIA': 'DC'
}

def normalize_state(state_input):
    """Convert state name or abbreviation to 2-letter code"""
    s = state_input.strip().upper()
    if len(s) == 2:
        return s
    return STATE_ABBREVS.get(s, None)

def get_police_violence_by_state(state_input):
    """Get police violence statistics for a state"""
    if not DATASET_LOADED:
        return {"found": False, "message": "Dataset not available"}

    state_code = normalize_state(state_input)
    if not state_code:
        return {"found": False, "message": f"State not recognized: {state_input}"}

    try:
        state_df = df[df['State'] == state_code]
        if state_df.empty:
            return {"found": False, "message": f"No data for state: {state_input}"}

        total = len(state_df)

        # Racial breakdown
        race_counts = state_df["Victim's race"].value_counts().to_dict()

        # Accountability
        charges = state_df['Criminal Charges?'].str.lower()
        charged = charges.str.contains('yes', na=False).sum()
        accountability_rate = round((charged / total) * 100, 1) if total > 0 else 0

        # Unarmed victims
        armed_col = 'Armed/Unarmed Status'
        unarmed = state_df[armed_col].str.lower().str.contains('unarmed', na=False).sum()
        unarmed_rate = round((unarmed / total) * 100, 1) if total > 0 else 0

        # Body camera usage
        body_cam = state_df['Body Camera (Source: WaPo)'].str.lower()
        body_cam_yes = body_cam.str.contains('yes', na=False).sum()
        body_cam_rate = round((body_cam_yes / total) * 100, 1) if total > 0 else 0

        # Risk level
        if accountability_rate < 5 and unarmed_rate > 15:
            risk_level = "High Risk"
            score_impact = 25
        elif accountability_rate < 10 or unarmed_rate > 10:
            risk_level = "Medium Risk"
            score_impact = 15
        else:
            risk_level = "Lower Risk"
            score_impact = 5

        return {
            "found": True,
            "state": state_code,
            "total_incidents": total,
            "racial_breakdown": race_counts,
            "accountability_rate": f"{accountability_rate}%",
            "unarmed_rate": f"{unarmed_rate}%",
            "body_camera_rate": f"{body_cam_rate}%",
            "risk_level": risk_level,
            "score_impact": score_impact
        }

    except Exception as e:
        return {"found": False, "message": str(e)}

def get_police_violence_by_city(city_input, state_input):
    """Get police violence statistics for a specific city"""
    if not DATASET_LOADED:
        return {"found": False, "message": "Dataset not available"}

    state_code = normalize_state(state_input)
    city_lower = city_input.strip().lower()

    try:
        city_df = df[
            (df['City'] == city_lower) &
            (df['State'] == state_code)
        ]

        if city_df.empty:
            return {"found": False, "message": f"No data for {city_input}, {state_input}"}

        total = len(city_df)
        race_counts = city_df["Victim's race"].value_counts().to_dict()

        charges = city_df['Criminal Charges?'].str.lower()
        charged = charges.str.contains('yes', na=False).sum()
        accountability_rate = round((charged / total) * 100, 1) if total > 0 else 0

        unarmed = city_df['Armed/Unarmed Status'].str.lower().str.contains('unarmed', na=False).sum()
        unarmed_rate = round((unarmed / total) * 100, 1) if total > 0 else 0

        if accountability_rate < 5 and unarmed_rate > 15:
            risk_level = "High Risk"
        elif accountability_rate < 10 or unarmed_rate > 10:
            risk_level = "Medium Risk"
        else:
            risk_level = "Lower Risk"

        return {
            "found": True,
            "city": city_input,
            "state": state_code,
            "total_incidents": total,
            "racial_breakdown": race_counts,
            "accountability_rate": f"{accountability_rate}%",
            "unarmed_rate": f"{unarmed_rate}%",
            "risk_level": risk_level
        }

    except Exception as e:
        return {"found": False, "message": str(e)}

def get_agency_violence_score(agency_name):
    """Score a law enforcement agency based on violence data"""
    if not DATASET_LOADED:
        return {"found": False, "score_impact": 0}

    agency_lower = agency_name.lower()

    try:
        agency_df = df[
            df['Agency responsible for death'].str.lower().str.contains(
                agency_lower, na=False
            )
        ]

        if agency_df.empty:
            return {"found": False, "score_impact": 0}

        total = len(agency_df)
        charges = agency_df['Criminal Charges?'].str.lower()
        charged = charges.str.contains('yes', na=False).sum()
        accountability_rate = round((charged / total) * 100, 1) if total > 0 else 0

        unarmed = agency_df['Armed/Unarmed Status'].str.lower().str.contains(
            'unarmed', na=False
        ).sum()
        unarmed_rate = round((unarmed / total) * 100, 1) if total > 0 else 0

        if total > 50 and accountability_rate < 5:
            score_impact = 30
            rating = "High Risk"
        elif total > 20 or unarmed_rate > 15:
            score_impact = 20
            rating = "Medium Risk"
        elif total > 5:
            score_impact = 10
            rating = "Low Risk"
        else:
            score_impact = 5
            rating = "Minimal"

        return {
            "found": True,
            "total_incidents": total,
            "accountability_rate": f"{accountability_rate}%",
            "unarmed_rate": f"{unarmed_rate}%",
            "score_impact": score_impact,
            "rating": rating
        }

    except Exception as e:
        return {"found": False, "score_impact": 0}
