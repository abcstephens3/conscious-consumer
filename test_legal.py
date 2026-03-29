import requests

response = requests.get(
    "https://www.courtlistener.com/api/rest/v4/search/",
    headers={"Authorization": "Token 6d2cf30f4a6c87f97e208eb91a73be0ac5e55246"},
    params={"q": "Exxon", "type": "d", "page_size": 5}
)

data = response.json()
for case in data.get("results", []):
    print(case.get("caseName"))
