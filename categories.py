# Maps business names to their category
BUSINESS_CATEGORIES = {
    # RETAIL
    "walmart": "retail", "amazon": "retail", "target": "retail",
    "costco": "retail", "home depot": "retail", "lowes": "retail",
    "kroger": "retail", "walgreens": "retail", "cvs": "retail",
    "dollar general": "retail", "dollar tree": "retail", "shein": "retail",
    "fashion nova": "retail", "tj maxx": "retail", "marshalls": "retail",
    "ross": "retail", "macys": "retail", "nordstrom": "retail",
    "gap": "retail", "old navy": "retail", "h&m": "retail", "zara": "retail",
    "forever 21": "retail", "nike": "retail", "adidas": "retail",
    "under armour": "retail", "best buy": "retail", "ebay": "retail",
    "etsy": "retail", "wayfair": "retail", "ikea": "retail",
    "sephora": "retail", "ulta": "retail", "bath and body works": "retail",
    "victorias secret": "retail", "ralph lauren": "retail",

    # FAST FOOD
    "mcdonalds": "fast_food", "starbucks": "fast_food",
    "chick-fil-a": "fast_food", "chick fil a": "fast_food",
    "burger king": "fast_food", "taco bell": "fast_food",
    "wendys": "fast_food", "subway": "fast_food", "dominos": "fast_food",
    "pizza hut": "fast_food", "chipotle": "fast_food", "dunkin": "fast_food",
    "popeyes": "fast_food", "kfc": "fast_food", "sonic": "fast_food",
    "dairy queen": "fast_food", "five guys": "fast_food",
    "in n out": "fast_food", "shake shack": "fast_food",
    "panda express": "fast_food", "olive garden": "fast_food",
    "applebees": "fast_food", "ihop": "fast_food", "dennys": "fast_food",
    "red lobster": "fast_food", "panera": "fast_food",
    "papa johns": "fast_food", "little caesars": "fast_food",

    # TECH
    "apple": "tech", "google": "tech", "alphabet": "tech",
    "microsoft": "tech", "meta": "tech", "facebook": "tech",
    "twitter": "tech", "x": "tech", "netflix": "tech", "uber": "tech",
    "lyft": "tech", "airbnb": "tech", "tiktok": "tech",
    "bytedance": "tech", "snap": "tech", "spotify": "tech",
    "adobe": "tech", "salesforce": "tech", "oracle": "tech",
    "ibm": "tech", "intel": "tech", "nvidia": "tech", "amd": "tech",
    "qualcomm": "tech", "cisco": "tech", "dell": "tech", "hp": "tech",
    "samsung": "tech", "sony": "tech", "paypal": "tech",
    "shopify": "tech", "zoom": "tech", "discord": "tech",

    # BANKS
    "jpmorgan": "banking", "jp morgan": "banking",
    "bank of america": "banking", "wells fargo": "banking",
    "citibank": "banking", "citigroup": "banking",
    "goldman sachs": "banking", "morgan stanley": "banking",
    "american express": "banking", "visa": "banking",
    "mastercard": "banking", "discover": "banking",
    "capital one": "banking", "chase": "banking",
    "us bank": "banking", "pnc": "banking", "td bank": "banking",
    "ally bank": "banking", "charles schwab": "banking",
    "fidelity": "banking", "vanguard": "banking",
    "blackrock": "banking", "coinbase": "banking", "robinhood": "banking",

    # OIL & ENERGY
    "exxon": "energy", "exxonmobil": "energy", "chevron": "energy",
    "shell": "energy", "bp": "energy", "conocophillips": "energy",
    "marathon oil": "energy", "valero": "energy", "halliburton": "energy",
    "duke energy": "energy", "nextera energy": "energy",
    "tesla energy": "energy", "sunrun": "energy", "first solar": "energy",

    # PHARMA
    "johnson and johnson": "pharma", "johnson & johnson": "pharma",
    "pfizer": "pharma", "moderna": "pharma", "merck": "pharma",
    "abbvie": "pharma", "eli lilly": "pharma", "novartis": "pharma",
    "roche": "pharma", "bayer": "pharma", "purdue pharma": "pharma",

    # FOOD & BEVERAGE
    "coca cola": "food", "pepsi": "food", "nestle": "food",
    "unilever": "food", "kraft heinz": "food", "general mills": "food",
    "kelloggs": "food", "tyson foods": "food", "perdue": "food",
    "smithfield": "food", "beyond meat": "food",
    "impossible foods": "food",

    # INSURANCE
    "state farm": "insurance", "allstate": "insurance",
    "geico": "insurance", "progressive": "insurance",
    "liberty mutual": "insurance", "usaa": "insurance",
    "nationwide": "insurance", "aig": "insurance", "aflac": "insurance",

    # TELECOM
    "att": "telecom", "at&t": "telecom", "verizon": "telecom",
    "tmobile": "telecom", "t-mobile": "telecom", "xfinity": "telecom",
    "spectrum": "telecom", "cox": "telecom",

    # AUTOMOTIVE
    "tesla": "automotive", "ford": "automotive", "general motors": "automotive",
    "gm": "automotive", "toyota": "automotive", "honda": "automotive",
    "volkswagen": "automotive", "vw": "automotive", "bmw": "automotive",
    "mercedes": "automotive", "volvo": "automotive", "subaru": "automotive",
    "rivian": "automotive", "carvana": "automotive",

    # TRAVEL
    "marriott": "travel", "hilton": "travel", "delta airlines": "travel",
    "united airlines": "travel", "american airlines": "travel",
    "southwest airlines": "travel", "carnival cruise": "travel",
    "royal caribbean": "travel", "airbnb": "travel",

    # EDUCATION
    "university of phoenix": "education", "devry university": "education",
    "khan academy": "education", "coursera": "education",
    "udemy": "education", "chegg": "education", "pearson": "education",
    "duolingo": "education", "masterclass": "education",
}

def get_category(business_name):
    return BUSINESS_CATEGORIES.get(business_name.lower().strip(), None)

def get_alternatives_in_category(category, exclude_name, min_score=70):
    """Get ethical alternatives in the same category"""
    from esg import ESG_DATA
    from humanrights import HUMAN_RIGHTS_DATA

    alternatives = []
    exclude = exclude_name.lower().strip()

    for name, cat in BUSINESS_CATEGORIES.items():
        if cat != category or name == exclude:
            continue
        if name not in ESG_DATA:
            continue

        esg = ESG_DATA[name]
        hr = HUMAN_RIGHTS_DATA.get(name, {})

        base_score = 100
        base_score -= esg.get("score_impact", 0)
        base_score -= hr.get("score_impact", 0)
        final_score = max(base_score, 0)

        if final_score >= min_score:
            alternatives.append({
                "name": name.title(),
                "score": final_score,
                "category": category,
                "esg_rating": esg.get("rating", "Unknown")
            })

    alternatives.sort(key=lambda x: x["score"], reverse=True)
    return alternatives[:4]
