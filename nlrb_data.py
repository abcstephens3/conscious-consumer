# NLRB (National Labor Relations Board) — Unfair Labor Practice Data
# Source: nlrb.gov/search/case
# Tracks union-busting complaints and labor violations by employer

NLRB_DATA = {
    "amazon": {
        "has_cases": True,
        "case_count": 75,
        "summary": "Over 75 unfair labor practice charges filed including union-busting, illegal surveillance, and retaliatory firings of union organizers",
        "score_impact": 20,
        "sources": [
            {"label": "NLRB Case Search — Amazon", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AAmazon"},
            {"label": "NLRB News — Amazon", "url": "https://www.nlrb.gov/news-outreach/news-story/nlrb-issues-complaint-against-amazon"}
        ]
    },
    "starbucks": {
        "has_cases": True,
        "case_count": 120,
        "summary": "Over 120 unfair labor practice charges filed including illegal store closures to prevent unionization and retaliation against union organizers",
        "score_impact": 20,
        "sources": [
            {"label": "NLRB Case Search — Starbucks", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AStarbucks"},
            {"label": "NLRB News — Starbucks", "url": "https://www.nlrb.gov/news-outreach/news-story/nlrb-issues-complaints-against-starbucks"}
        ]
    },
    "walmart": {
        "has_cases": True,
        "case_count": 43,
        "summary": "Dozens of NLRB charges including illegal store closures, surveillance of workers discussing wages, and retaliation against organizing employees",
        "score_impact": 15,
        "sources": [
            {"label": "NLRB Case Search — Walmart", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AWalmart"}
        ]
    },
    "apple": {
        "has_cases": True,
        "case_count": 18,
        "summary": "NLRB charges including illegal interrogation of employees about union activity and unlawful policies restricting worker communication",
        "score_impact": 10,
        "sources": [
            {"label": "NLRB Case Search — Apple", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AApple"}
        ]
    },
    "tesla": {
        "has_cases": True,
        "case_count": 22,
        "summary": "Multiple NLRB charges including illegal firing of union organizers, unlawful no-recording policies, and mandatory anti-union meetings",
        "score_impact": 12,
        "sources": [
            {"label": "NLRB Case Search — Tesla", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3ATesla"}
        ]
    },
    "mcdonalds": {
        "has_cases": True,
        "case_count": 38,
        "summary": "NLRB charges including franchise-wide retaliation against Fight for $15 organizers and illegal interference with worker organizing rights",
        "score_impact": 14,
        "sources": [
            {"label": "NLRB Case Search — McDonald's", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_stye%3AC&f%5B1%5D=respondent%3AMcDonalds"}
        ]
    },
starbucks":    "whole foods": {
        "has_cases": True,
        "case_count": 12,
        "summary": "NLRB charges including surveillance of workers and retaliatory discipline of employees engaged in union activity",
        "score_impact": 8,
        "sources": [
            {"label": "NLRB Case Search — Whole Foods", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AWhole+Foods"}
        ]
    },
    "google": {
        "has_cases": True,
        "case_count": 9,
        "summary": "NLRB charges including illegal firing of workers engaged in protected concerted activity and unlawful workplace policies",
        "score_impact": 8,
        "sources": [
            {"label": "NLRB Case Search — Google", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AGoogle"}
        ]
    },
    "trader joes": {
        "has_cases": True,
        "case_count": 14,
        "summary": "NLRB charges including retaliatory store closures and illegal interference with union organizing efforts",
        "score_impact": 9,
        "sources": [
            {"label": "NLRB Case Search — Trader Joe's", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3ATrader+Joes"}
        ]
    },
    "chipotle": {
        "has_cases": True,
        "case_count": 8,
        "summary": "NLRB charges including illegal store closure and retaliatory firing of union organizers",
        "score_impact": 7,
        "sources": [
            {"label": "NLRB Case Search — Chipotle", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AChipotle"}
        ]
    },
    "verizon": {
        "has_cases": True,
        "case_count": 11,
        "summary": "NLRB charges including bad faith bargaining and illegal unilateral changes to working conditions",
        "score_impact": 8,
        "sources": [
            {"label": "NLRB Case Search — Verizon", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AVerizon"}
        ]
    },
    "ford": {
        "has_cases": True,
        "case_count": 7,
        "summary": "NLRB charges related to bargaining disputes and workplace safety violations during labor negotiations",
        "score_impact": 6,
        "sources": [
            {"label": "NLRB Case Search — Ford", "url": "https://www.nlrb.gov/search/case?f%5B0%5D=case_type%3AC&f%5B1%5D=respondent%3AFord"}
        ]
    }
}

def get_nlrb_data(business_name):
    """Get NLRB unfair labor practice data for a business"""
    key = business_name.lower().strip()
    if key in NLRB_DATA:
        return {"found": True, **NLRB_DATA[key]}
    for company, data in NLRB_DATA.items():
        if company in key or key in company:
            return {"found": True, **data}
    return {"found": False}
