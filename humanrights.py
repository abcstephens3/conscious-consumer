# Human Rights Risk Scores based on:
# - KnowTheChain Benchmark
# - Corporate Human Rights Benchmark
# - Business & Human Rights Resource Centre
# - Dept of Labor reports
# Scale: 0-10 (0 = excellent, 10 = severe violations)

HUMAN_RIGHTS_DATA = {
    # --- RETAIL / SHOPPING ---
    "walmart": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Wage theft settlements", "Anti-union practices", "Supply chain labor concerns"]},
    "amazon": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Warehouse worker conditions", "Anti-union practices", "Delivery driver exploitation"]},
    "shein": {"score": 10, "rating": "Severe Risk", "score_impact": 25, "flags": ["Forced labor supply chain concerns", "Child labor risk", "Extreme worker exploitation"]},
    "fashion nova": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Sweatshop labor reports", "Worker wage violations"]},
    "h&m": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Supply chain labor concerns", "Factory worker conditions"]},
    "zara": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Supply chain labor violations", "Factory worker conditions"]},
    "forever 21": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["LA garment worker violations", "Wage theft history"]},
    "gap": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Supply chain labor concerns"]},
    "nike": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Historical sweatshop concerns", "Ongoing supply chain monitoring"]},
    "adidas": {"score": 4, "rating": "Low Risk", "score_impact": 10, "flags": ["Supply chain improvement efforts noted"]},
    "target": {"score": 3, "rating": "Low Risk", "score_impact": 10, "flags": ["Some supply chain concerns"]},
    "dollar general": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Worker safety violations", "OSHA citations"]},
    "dollar tree": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Worker safety violations", "OSHA citations"]},

    # --- FAST FOOD / RESTAURANTS ---
    "mcdonalds": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Wage theft settlements", "Worker safety issues", "Franchise labor violations"]},
    "burger king": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Wage violations reported", "Worker conditions concerns"]},
    "wendys": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Tomato supply chain labor abuses", "Refused to join Fair Food Program"]},
    "taco bell": {"score": 4, "rating": "Low Risk", "score_impact": 10, "flags": ["Joined Fair Food Program"]},
    "subway": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Franchise labor concerns"]},
    "chick-fil-a": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Anti-LGBTQ+ donation history", "Discrimination claims"]},
    "chick fil a": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Anti-LGBTQ+ donation history", "Discrimination claims"]},
    "dominos": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Delivery driver labor concerns"]},

    # --- TECH COMPANIES ---
    "amazon": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Warehouse conditions", "Anti-union practices", "Worker surveillance"]},
    "apple": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Foxconn supply chain concerns", "Cobalt sourcing issues"]},
    "meta": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Content moderation worker trauma", "Myanmar genocide role"]},
    "facebook": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Content moderation worker trauma", "Myanmar genocide role"]},
    "google": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Contractor worker concerns", "Content moderator conditions"]},
    "microsoft": {"score": 4, "rating": "Low Risk", "score_impact": 10, "flags": ["Some supply chain mineral concerns"]},
    "tesla": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Anti-union practices", "Cobalt sourcing concerns", "Worker safety violations"]},
    "uber": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Driver misclassification", "Gig worker exploitation"]},
    "lyft": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Driver misclassification concerns"]},
    "tiktok": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Content moderation worker conditions", "Data privacy concerns"]},

    # --- BANKS & FINANCE ---
    "wells fargo": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Predatory lending history", "Fake accounts scandal", "Discriminatory lending"]},
    "jpmorgan": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Financing of private prisons", "Discriminatory lending settlements"]},
    "jp morgan": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Financing of private prisons", "Discriminatory lending settlements"]},
    "bank of america": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Predatory lending settlements"]},
    "citibank": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Discriminatory lending history"]},
    "goldman sachs": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["1MDB scandal involvement", "Predatory practices"]},
    "coinbase": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Employee racial discrimination claims"]},
    "robinhood": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Gamification of investing concerns", "User exploitation"]},

    # --- OIL & ENERGY ---
    "exxon": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Indigenous rights violations", "Climate denial funding", "Environmental racism"]},
    "exxonmobil": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Indigenous rights violations", "Climate denial funding", "Environmental racism"]},
    "chevron": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Ecuador environmental destruction", "Indigenous rights violations"]},
    "shell": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Nigeria Delta destruction", "Indigenous rights violations", "Climate denial"]},
    "bp": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Deepwater Horizon disaster", "Worker safety record", "Environmental destruction"]},
    "halliburton": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["War profiteering concerns", "Environmental violations"]},

    # --- PHARMACEUTICALS ---
    "purdue pharma": {"score": 10, "rating": "Severe Risk", "score_impact": 25, "flags": ["Opioid crisis responsibility", "Deliberate addiction creation", "Community destruction"]},
    "johnson and johnson": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Opioid settlement", "Baby powder asbestos", "Talc cancer links"]},
    "johnson & johnson": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Opioid settlement", "Baby powder asbestos", "Talc cancer links"]},
    "mckesson": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Opioid distribution role", "Settlement payments"]},
    "cardinal health": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Opioid distribution role", "Settlement payments"]},
    "bayer": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Roundup cancer settlements", "Monsanto acquisition legacy"]},
    "mallinckrodt": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Opioid crisis role", "Bankruptcy to avoid settlements"]},

    # --- FOOD & BEVERAGE ---
    "tyson foods": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Slaughterhouse worker conditions", "COVID worker deaths", "Child labor violations"]},
    "perdue": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Poultry worker conditions", "Wage concerns"]},
    "smithfield": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Worker conditions", "COVID outbreak mishandling", "Environmental racism"]},
    "nestle": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Child labor in cocoa supply chain", "Water privatization", "Baby formula marketing"]},
    "coca cola": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Union busting in Colombia", "Water depletion in communities"]},
    "kraft heinz": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Supply chain labor concerns"]},

    # --- EDUCATION ---
    "university of phoenix": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Predatory enrollment practices", "Student debt exploitation", "Military targeting"]},
    "devry university": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Fraudulent job placement claims", "Predatory lending", "FTC settlement"]},
    "grand canyon university": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Misleading PhD program claims", "Predatory enrollment"]},
    "chegg": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Academic integrity concerns", "Data breach history"]},
    "pearson": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Textbook price gouging", "Student data concerns"]},
    "mcgraw hill": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Textbook price gouging"]},
    "cengage": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Textbook price gouging"]},

    # --- AUTOMOTIVE ---
    "volkswagen": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Dieselgate emissions fraud", "Deliberate environmental deception"]},
    "vw": {"score": 9, "rating": "Severe Risk", "score_impact": 25, "flags": ["Dieselgate emissions fraud", "Deliberate environmental deception"]},
    "ford": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Historical worker safety issues", "Supply chain concerns"]},
    "general motors": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Ignition switch cover-up", "Worker safety violations"]},
    "gm": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Ignition switch cover-up", "Worker safety violations"]},
    "tesla": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Anti-union practices", "Worker safety violations", "Racial discrimination lawsuits"]},
    "carvana": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Title fraud issues", "Consumer complaints"]},

    # --- TRAVEL & HOSPITALITY ---
    "carnival cruise": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Environmental dumping convictions", "Worker conditions", "Environmental violations"]},
    "royal caribbean": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Environmental violations", "Worker conditions"]},
    "united airlines": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Forced passenger removal incident", "Worker disputes"]},
    "american airlines": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Worker safety concerns", "Labor disputes"]},
    "spirit airlines": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Worker conditions concerns"]},

    # --- TELECOM ---
    "att": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Mass surveillance cooperation", "Worker union disputes"]},
    "at&t": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Mass surveillance cooperation", "Worker union disputes"]},
    "verizon": {"score": 5, "rating": "Medium Risk", "score_impact": 15, "flags": ["Surveillance cooperation concerns"]},
    "xfinity": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Data privacy concerns", "Consumer complaints"]},
    "spectrum": {"score": 6, "rating": "Medium Risk", "score_impact": 15, "flags": ["Consumer complaints", "Worker disputes"]},

    # --- REAL ESTATE ---
    "blackstone": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Tenant displacement", "Housing crisis contributor", "Rent gouging"]},
    "invitation homes": {"score": 8, "rating": "High Risk", "score_impact": 20, "flags": ["Tenant displacement", "Rent increases", "Housing shortage contributor"]},
    "american homes 4 rent": {"score": 7, "rating": "High Risk", "score_impact": 20, "flags": ["Tenant rights concerns", "Rent gouging"]},
}

def get_human_rights_rating(business_name):
    try:
        key = business_name.lower().strip()
        data = HUMAN_RIGHTS_DATA.get(key, None)

        if not data:
            return {"found": False, "score_impact": 0}

        return {
            "found": True,
            "human_rights_score": data["score"],
            "rating": data["rating"],
            "score_impact": data["score_impact"],
            "flags": data["flags"]
        }
    except Exception as e:
        return {"found": False, "score_impact": 0}
