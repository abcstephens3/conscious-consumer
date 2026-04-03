from local_awareness import match_business_score
tests = ["McDonald's", "Shell", "Kroger", "BP", "Chevron"]
for t in tests:
    result = match_business_score(t)
    print(f"{t}: {result}")
