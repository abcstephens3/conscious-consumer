import anthropic

import os
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))

def generate_summary(business_name, score, flags, esg_data, hr_data, legal_data):
    try:
        # Build context from all data sources
        flag_text = "\n".join(flags) if flags else "No major flags detected"
        esg_info = f"ESG Risk Rating: {esg_data.get('rating', 'Unknown')} (score: {esg_data.get('esg_score', 'N/A')})" if esg_data.get('found') else "No ESG data found"
        hr_info = f"Human Rights Rating: {hr_data.get('rating', 'Unknown')}" if hr_data.get('found') else "No human rights data found"
        legal_info = f"{legal_data.get('case_count', 0)} federal court cases found" if legal_data.get('found') else "No legal records found"

        prompt = f"""You are a consumer transparency assistant. Based on the following data about {business_name}, write a clear, honest, 3-4 sentence summary that a regular consumer would understand. Be direct about concerns but fair. Do not use bullet points.

Business: {business_name}
Transparency Score: {score}/100
{esg_info}
{hr_info}
{legal_info}

Flags detected:
{flag_text}

Write a plain-language summary explaining what this score means for a consumer considering spending money at this business."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return message.content[0].text

    except Exception as e:
        return f"{business_name} scored {score}/100 based on political activity, news sentiment, legal records, ESG ratings, and human rights data."
