import requests

import os
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

def get_news_sentiment(business_name):
    try:
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "apiKey": NEWS_API_KEY,
                "q": business_name,
                "language": "en",
                "sortBy": "relevancy",
                "pageSize": 10
            }
        )
        data = response.json()
        articles = data.get("articles", [])

        if not articles:
            return {"found": False, "article_count": 0, "score_impact": 0}

        # Look for negative keywords in headlines
        negative_words = [
            "lawsuit", "scandal", "fraud", "fine", "penalty",
            "violation", "corrupt", "illegal", "investigation", "controversy"
        ]

        negative_count = 0
        flagged_headlines = []

        for article in articles:
            title = article.get("title", "").lower()
            for word in negative_words:
                if word in title:
                    negative_count += 1
                    flagged_headlines.append({
                        "title": article.get("title"),
                        "url": article.get("url", ""),
                        "source": article.get("source", {}).get("name", "")
                    })
                    break

        score_impact = min(negative_count * 8, 30)
        

        return {
            "found": True,
            "article_count": len(articles),
            "negative_count": negative_count,
            "score_impact": score_impact,
            "flagged_headlines": flagged_headlines[:3]
        }
    except Exception as e:
        return {"found": False, "article_count": 0, "score_impact": 0}
