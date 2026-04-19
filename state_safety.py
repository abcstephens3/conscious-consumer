# State Safety Ratings for Marginalized Communities
# Sources: NAACP Travel Advisories, HRC State Scorecards,
# ACLU Legislative Tracking, Movement Advancement Project,
# ADA National Network, Pew Research

from map_data import get_map_data, get_map_lgbtq_rating

STATE_SAFETY = {
    "Alabama": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No statewide nondiscrimination protections. Multiple anti-trans laws passed. No same-sex adoption protections.",
            "advisories": ["LGBTQ+ travelers should exercise caution", "Limited legal protections if discrimination occurs"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "NAACP has issued travel advisories for Alabama. History of voting rights restrictions.",
            "advisories": ["NAACP travel advisory in effect", "Documented racial profiling concerns"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Strong Christian majority culture. Limited protections for non-Christian minorities.",
            "advisories": ["Muslim and Jewish travelers should be aware of limited accommodations in rural areas"]
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "ADA compliance inconsistent in rural areas. Limited accessible transportation.",
            "advisories": ["Verify accessibility before travel to rural areas"]
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Near-total abortion ban in effect. Limited reproductive healthcare access.",
            "advisories": ["Reproductive healthcare severely restricted", "Medical emergency exceptions limited"]
        }
    },
    "Alaska": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Some protections in place. No conversion therapy ban. Rural areas may be unwelcoming.",
            "advisories": ["Exercise caution in rural and remote areas"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Indigenous communities face systemic challenges. Some racial tensions in urban areas.",
            "advisories": ["Indigenous travelers may face unique challenges"]
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 6,
            "notes": "Generally tolerant in urban areas.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Remote geography makes accessibility very challenging. Limited accessible infrastructure.",
            "advisories": ["Accessibility very limited outside Anchorage", "Plan thoroughly before travel"]
        },
        "women": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Abortion rights protected. Some healthcare access challenges in remote areas.",
            "advisories": []
        }
    },
    "Arizona": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Phoenix and Tucson are generally welcoming. Rural areas vary significantly.",
            "advisories": ["Urban areas generally safe", "Exercise caution in rural areas"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "History of anti-immigration laws. Latino community faces profiling concerns.",
            "advisories": ["Latino travelers should be aware of law enforcement interactions"]
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 6,
            "notes": "Diverse urban population. Generally tolerant in cities.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Urban areas generally accessible. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Near-total abortion ban enacted. Reproductive healthcare severely restricted.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Arkansas": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Multiple anti-trans laws. No nondiscrimination protections. Hostile legislative environment.",
            "advisories": ["LGBTQ+ travelers should exercise significant caution", "No legal recourse if discrimination occurs"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Limited civil rights protections. Racial disparities in criminal justice system.",
            "advisories": ["NAACP recommends caution"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong evangelical Christian culture. Limited accommodations for minorities.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Inconsistent ADA compliance especially in rural areas.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban. Among most restrictive states for reproductive rights.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "California": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Among the most protective states. Comprehensive nondiscrimination laws. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong civil rights protections. Diverse population. Some urban inequality persists.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Very diverse. Strong protections for religious minorities.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Strong ADA enforcement. Generally excellent accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected. Comprehensive reproductive healthcare.",
            "advisories": []
        }
    },
    "Colorado": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong protections. Conversion therapy banned. Denver very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally progressive. Some rural areas less diverse.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Diverse and generally tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Good accessibility in urban areas. Mountain terrain can be challenging.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights protected by state law.",
            "advisories": []
        }
    },
    "Connecticut": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned. Very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Some economic inequality in urban areas.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Diverse and generally tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Good ADA compliance generally.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "Delaware": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Comprehensive nondiscrimination laws. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong civil rights protections.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Generally tolerant and diverse.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Good accessibility standards.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights protected.",
            "advisories": []
        }
    },
    "Florida": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Don't Say Gay law. Anti-trans healthcare restrictions. HRC has issued travel advisory.",
            "advisories": ["HRC travel advisory in effect", "LGBTQ+ families with children should exercise caution", "Anti-trans healthcare laws restrict medical access"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "NAACP travel advisory issued. Anti-DEI legislation. African American history curriculum restrictions.",
            "advisories": ["NAACP travel advisory in effect", "Anti-DEI laws restrict education and workplace protections"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "South Florida very diverse. Rural north Florida less welcoming.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Urban areas generally accessible. Heat can be challenging.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Six week abortion ban. Severely restricted reproductive healthcare.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Georgia": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "No statewide protections. Atlanta is an exception and very welcoming.",
            "advisories": ["Exercise caution outside Atlanta metro area"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 4,
            "notes": "NAACP has flagged voting rights concerns. Atlanta has strong Black community infrastructure.",
            "advisories": ["Voting rights concerns documented"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Atlanta very diverse. Rural areas less so.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Atlanta generally accessible. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Six week abortion ban. Limited reproductive healthcare.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Hawaii": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Very welcoming. Strong protections. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Most diverse state in the US. Strong cultural respect.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Extremely diverse and tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally accessible. Some terrain challenges.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "Idaho": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Anti-trans laws passed. Very hostile legislative environment.",
            "advisories": ["LGBTQ+ travelers should exercise significant caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "History of white nationalist activity in northern regions.",
            "advisories": ["Travelers of color should exercise caution especially in rural northern areas"]
        },
        "religious_minority": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Strong LDS and evangelical influence. Limited tolerance for minority religions.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Rural terrain limits accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban. Among most restrictive states.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "Illinois": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong protections. Chicago very welcoming. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong civil rights laws. Chicago has some neighborhood segregation historically.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very diverse especially in Chicago.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Chicago excellent accessibility. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "Indiana": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "No statewide protections. RFRA law allows discrimination. Anti-trans legislation.",
            "advisories": ["Limited legal protections if discrimination occurs"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Indianapolis generally welcoming. Rural areas vary.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "RFRA law can impact religious minorities.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Generally adequate ADA compliance.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Near-total abortion ban enacted.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Iowa": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Some protections exist but being rolled back. Anti-trans legislation passed.",
            "advisories": ["Protections weakening", "Exercise caution in rural areas"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Limited diversity outside cities. Some racial disparities in criminal justice.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Predominantly Christian. Limited diversity in rural areas.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Adequate in cities. Rural areas less accessible.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Six week abortion ban. Severely restricted reproductive healthcare.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Kansas": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "No statewide protections. Anti-trans legislation. Rural areas hostile.",
            "advisories": ["Exercise caution especially in rural areas"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Limited diversity. Kansas City area more welcoming.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong evangelical influence.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Adequate in cities. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Abortion rights protected by state Supreme Court ruling.",
            "advisories": []
        }
    },
    "Kentucky": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Anti-trans laws. Very hostile legislative environment.",
            "advisories": ["LGBTQ+ travelers should exercise significant caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Limited civil rights protections. Racial disparities documented.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong Baptist and evangelical culture.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Inconsistent accessibility especially in Appalachian regions.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban. Among most restrictive states.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "Louisiana": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No statewide protections. New Orleans is an exception and very welcoming.",
            "advisories": ["Exercise caution outside New Orleans", "No legal recourse if discrimination occurs"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "NAACP has flagged concerns. Deep racial disparities in criminal justice.",
            "advisories": ["NAACP recommends caution", "Documented racial disparities in law enforcement"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong Catholic and Baptist culture. New Orleans more diverse.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "New Orleans improving. Rural areas limited.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Total abortion ban. No exceptions for rape or incest.",
            "advisories": ["Total abortion ban in effect"]
        }
    },
    "Maine": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong protections. Conversion therapy banned. Generally welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Limited diversity but generally welcoming.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Rural terrain can limit accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "Maryland": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned. Very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong civil rights protections. Diverse population.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very diverse. Strong protections.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Generally good accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "Massachusetts": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Among the most protective states in the nation. First state to legalize same-sex marriage.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong protections. Some historical racial tensions in Boston area.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Very diverse. Excellent protections.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Excellent accessibility standards.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Abortion rights strongly protected. Excellent reproductive healthcare access.",
            "advisories": []
        }
    },
    "Michigan": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Nondiscrimination protections added. Detroit and Ann Arbor very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Detroit has strong Black community infrastructure.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Diverse especially in Detroit metro. Large Muslim community in Dearborn.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally good accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Abortion rights restored by ballot measure.",
            "advisories": []
        }
    },
    "Minnesota": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned. Very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Minneapolis has significant Somali and Hmong communities.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very diverse. Strong protections.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Good accessibility standards.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "Mississippi": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 1,
            "notes": "No protections. HB 1523 allows broad discrimination. Most hostile state for LGBTQ+ rights.",
            "advisories": ["HRC travel advisory in effect", "Broad legal discrimination permitted", "Exercise extreme caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 2,
            "notes": "NAACP travel advisory in effect. Deep racial disparities. History of racial violence.",
            "advisories": ["NAACP travel advisory in effect", "Documented racial profiling concerns", "Exercise significant caution"]
        },
        "religious_minority": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Strong evangelical Christian majority. Very limited tolerance for minority religions.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Among worst states for disability accessibility and services.",
            "advisories": ["Verify accessibility thoroughly before travel"]
        },
        "women": {
            "rating": "High Risk",
            "score": 1,
            "notes": "Total abortion ban. No exceptions. Among most restrictive states.",
            "advisories": ["Total abortion ban with no exceptions"]
        }
    },
    "Missouri": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "No statewide protections. Anti-trans legislation. St. Louis and Kansas City more welcoming.",
            "advisories": ["Exercise caution outside major cities"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 4,
            "notes": "Ferguson and St. Louis have documented racial tensions. Racial disparities in criminal justice.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Cities more diverse. Rural areas less welcoming.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Cities generally accessible. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban. Very limited exceptions.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "Montana": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Anti-trans legislation. No comprehensive protections. Rural areas hostile.",
            "advisories": ["Exercise caution especially in rural areas"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Indigenous communities face significant challenges. Limited diversity.",
            "advisories": ["Indigenous travelers may face unique challenges"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Predominantly Christian. Limited religious diversity.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Rural terrain severely limits accessibility.",
            "advisories": ["Accessibility very limited outside cities"]
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Abortion rights under legal challenge. Access limited.",
            "advisories": []
        }
    },
    "Nebraska": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "No statewide protections. Anti-trans legislation passed.",
            "advisories": ["Limited legal protections if discrimination occurs"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Omaha more diverse. Rural areas limited.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Predominantly Christian. Some diversity in Omaha.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Omaha generally accessible. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "12-week abortion ban enacted.",
            "advisories": ["Reproductive healthcare significantly restricted"]
        }
    },
    "Nevada": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Comprehensive protections. Las Vegas very welcoming. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Diverse population. Strong protections.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very diverse especially in Las Vegas.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Las Vegas excellent accessibility. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights protected.",
            "advisories": []
        }
    },
    "New Hampshire": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong protections. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Limited diversity but generally welcoming.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally good accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Abortion rights generally protected.",
            "advisories": []
        }
    },
    "New Jersey": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned. Very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong civil rights protections. Very diverse.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Extremely diverse. Strong protections.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Generally good accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "New Mexico": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Comprehensive protections. Conversion therapy banned. Welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Majority minority state. Strong Indigenous and Latino community presence.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Diverse. Strong Indigenous and Catholic traditions respected.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Urban areas accessible. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "New York": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Among the most protective states. NYC is a global LGBTQ+ hub. Comprehensive protections.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong civil rights laws. Extremely diverse especially NYC.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Most diverse state. Excellent protections for all religious minorities.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "NYC excellent accessibility standards. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Abortion rights strongly protected. Excellent reproductive healthcare.",
            "advisories": []
        }
    },
    "North Carolina": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "History of HB2 bathroom bill. Some protections restored. Charlotte more welcoming.",
            "advisories": ["Research local protections before travel"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Voting rights concerns documented. Urban areas more welcoming.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Cities more diverse. Rural areas less welcoming.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Cities generally accessible.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "12-week abortion ban enacted.",
            "advisories": ["Reproductive healthcare significantly restricted"]
        }
    },
    "North Dakota": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Anti-trans laws. Very hostile.",
            "advisories": ["Exercise significant caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Indigenous communities face significant challenges. Standing Rock area tensions.",
            "advisories": ["Indigenous travelers should be aware of local tensions"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Predominantly Christian. Limited diversity.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Rural terrain limits accessibility significantly.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 1,
            "notes": "Total abortion ban. No exceptions.",
            "advisories": ["Total abortion ban in effect"]
        }
    },
    "Ohio": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "No statewide protections. Columbus and Cleveland more welcoming.",
            "advisories": ["Exercise caution outside major cities"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Urban areas have strong Black community infrastructure. Rural areas vary.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Cities diverse. Rural areas less so.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Cities generally accessible.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Six week abortion ban enacted despite ballot measure. Legal battles ongoing.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Oklahoma": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Multiple anti-trans laws. Very hostile legislative environment.",
            "advisories": ["Exercise significant caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Tulsa Race Massacre history. Limited civil rights protections.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 3,
            "notes": "Strong evangelical culture. Limited tolerance for minority religions.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Limited accessibility especially in rural areas.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 1,
            "notes": "Total abortion ban. No exceptions for rape or incest.",
            "advisories": ["Total abortion ban with no exceptions"]
        }
    },
    "Oregon": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned. Portland very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Portland has a history of racial inequity being addressed.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very tolerant. Diverse urban areas.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Portland excellent accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Among the most protective states for reproductive rights.",
            "advisories": []
        }
    },
    "Pennsylvania": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Philadelphia and Pittsburgh very welcoming. Statewide protections improving.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong urban civil rights infrastructure. Philadelphia has strong Black community.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very diverse especially in Philadelphia.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Cities generally accessible.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Abortion rights protected by governor veto.",
            "advisories": []
        }
    },
    "Rhode Island": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Diverse urban population.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Diverse and tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally good accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "South Carolina": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Anti-trans legislation. Very hostile environment.",
            "advisories": ["Exercise significant caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "NAACP has flagged concerns. Charleston Emanuel AME shooting history.",
            "advisories": ["NAACP recommends caution"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong evangelical and Baptist culture.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Inconsistent accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Six week abortion ban. Very limited exceptions.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "South Dakota": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Multiple anti-trans laws. Very hostile.",
            "advisories": ["Exercise significant caution"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Indigenous communities face severe challenges. Pine Ridge Reservation conditions.",
            "advisories": ["Indigenous travelers should be aware of systemic challenges"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Predominantly Christian. Limited diversity.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Rural terrain severely limits accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 1,
            "notes": "Total abortion ban. No exceptions for rape or incest.",
            "advisories": ["Total abortion ban with no exceptions"]
        }
    },
    "Tennessee": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Multiple anti-trans laws. Nashville more welcoming but limited protections.",
            "advisories": ["HRC has flagged Tennessee", "Exercise significant caution", "Anti-drag and anti-trans laws in effect"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Memphis has documented racial tensions. Limited civil rights protections.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong evangelical and Baptist culture.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Cities generally accessible. Rural areas less so.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban. Very limited exceptions.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "Texas": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 3,
            "notes": "No statewide protections. Anti-trans laws. Austin and Houston more welcoming.",
            "advisories": ["HRC has flagged Texas", "Exercise caution outside major cities", "Anti-trans healthcare laws restrict medical access"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "NAACP has flagged voting rights concerns. El Paso Walmart shooting. Racial disparities documented.",
            "advisories": ["NAACP recommends awareness", "Voting rights concerns documented"]
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Cities very diverse. Rural areas less welcoming.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Cities generally accessible. Heat can be challenging.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 1,
            "notes": "Total abortion ban. No exceptions for rape or incest. SB8 vigilante enforcement.",
            "advisories": ["Total abortion ban with vigilante enforcement mechanism"]
        }
    },
    "Utah": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Some protections exist. Salt Lake City welcoming. Strong LDS influence statewide.",
            "advisories": ["Research local protections before travel", "Salt Lake City more welcoming than rural areas"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Limited diversity. Salt Lake City more diverse.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong LDS majority culture. Non-LDS travelers may find culture unfamiliar.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Terrain can be challenging. Cities more accessible.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Near-total abortion ban. Very limited exceptions.",
            "advisories": ["Reproductive healthcare severely restricted"]
        }
    },
    "Vermont": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "First state to legalize civil unions. Among most protective. Conversion therapy banned.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong protections. Limited diversity but welcoming.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very tolerant.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally accessible. Some rural terrain challenges.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Abortion rights enshrined in state constitution.",
            "advisories": []
        }
    },
    "Virginia": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Comprehensive protections added. Northern Virginia and Richmond welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Strong civil rights laws. Diverse northern Virginia.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Northern Virginia extremely diverse.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 7,
            "notes": "Generally good accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Abortion rights protected by governor veto.",
            "advisories": []
        }
    },
    "Washington": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Comprehensive protections. Conversion therapy banned. Seattle very welcoming.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Strong protections. Diverse urban areas.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Very diverse. Strong protections.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 8,
            "notes": "Seattle excellent accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    },
    "West Virginia": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Anti-trans legislation. Very hostile environment.",
            "advisories": ["Exercise significant caution"]
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Very limited diversity. Racial disparities in criminal justice.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Strong evangelical culture. Limited religious diversity.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Appalachian terrain severely limits accessibility.",
            "advisories": ["Accessibility very challenging in most of the state"]
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "Wisconsin": {
        "overall": "Medium Risk",
        "lgbtq": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Some protections. Madison and Milwaukee welcoming. Rural areas vary.",
            "advisories": []
        },
        "racial": {
            "rating": "Medium Risk",
            "score": 5,
            "notes": "Milwaukee has significant racial disparities. Madison more welcoming.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Cities diverse. Rural areas less so.",
            "advisories": []
        },
        "disability": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Cities generally accessible.",
            "advisories": []
        },
        "women": {
            "rating": "Medium Risk",
            "score": 6,
            "notes": "Abortion rights restored by court ruling. Some restrictions remain.",
            "advisories": []
        }
    },
    "Wyoming": {
        "overall": "High Risk",
        "lgbtq": {
            "rating": "High Risk",
            "score": 2,
            "notes": "No protections. Matthew Shepard murder history. Very hostile rural environment.",
            "advisories": ["Exercise significant caution", "Matthew Shepard case reflects historical hostility"]
        },
        "racial": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Very limited diversity. Indigenous communities face challenges.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Medium Risk",
            "score": 4,
            "notes": "Predominantly Christian. Very limited religious diversity.",
            "advisories": []
        },
        "disability": {
            "rating": "High Risk",
            "score": 3,
            "notes": "Rural terrain severely limits accessibility.",
            "advisories": []
        },
        "women": {
            "rating": "High Risk",
            "score": 2,
            "notes": "Near-total abortion ban.",
            "advisories": ["Reproductive healthcare near-totally banned"]
        }
    },
    "Washington DC": {
        "overall": "Low Risk",
        "lgbtq": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Among the most welcoming places in the US. Comprehensive protections.",
            "advisories": []
        },
        "racial": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Strong civil rights infrastructure. Majority Black city historically.",
            "advisories": []
        },
        "religious_minority": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Extremely diverse. Excellent protections.",
            "advisories": []
        },
        "disability": {
            "rating": "Low Risk",
            "score": 9,
            "notes": "Excellent accessibility standards.",
            "advisories": []
        },
        "women": {
            "rating": "Low Risk",
            "score": 10,
            "notes": "Abortion rights strongly protected.",
            "advisories": []
        }
    }
}

STATE_ABBREVIATIONS = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming", "DC": "Washington DC"
}

def get_state_safety(location):
    """Get safety ratings for a state, enriched with MAP LGBTQ+ data"""
    key = location.lower().strip()
    
    # Try direct match first
    data = None
    if key in STATE_SAFETY:
        data = STATE_SAFETY[key]
    else:
        for state, state_data in STATE_SAFETY.items():
            if state in key or key in state:
                data = state_data
                key = state
                break
    
    if not data:
        return {"found": False}
    
    import copy
    result = copy.deepcopy(data)
    result["found"] = True
    
    # Enrich with MAP data
    map_data = get_map_data(key)
    if map_data["found"]:
        # Override LGBTQ rating with MAP's more precise data
        map_rating = get_map_lgbtq_rating(key)
        if map_rating and result.get("lgbtq"):
            result["lgbtq"]["rating"] = map_rating
            
            # Add MAP-specific advisories
            map_advisories = map_data.get("advisories", [])
            existing = result["lgbtq"].get("advisories", [])
            combined = list(dict.fromkeys(existing + map_advisories))
            result["lgbtq"]["advisories"] = combined
            
            # Add MAP policy details
            result["lgbtq"]["map_score"] = map_data.get("tally_score")
            result["lgbtq"]["map_category"] = map_data.get("category")
            result["lgbtq"]["nondiscrimination_law"] = map_data.get("nondiscrimination")
            result["lgbtq"]["conversion_therapy_ban"] = map_data.get("conversion_therapy_ban")
            result["lgbtq"]["anti_trans_laws"] = map_data.get("anti_trans_laws")
            result["lgbtq"]["map_source"] = map_data.get("source")
        
        # Update overall rating if MAP shows negative category
        if map_data.get("category") == "negative" and result.get("overall") != "High Risk":
            result["overall"] = "High Risk"
    
    return result
