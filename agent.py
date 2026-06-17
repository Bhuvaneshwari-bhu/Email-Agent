import os
import json
import time
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_email(email_text):

    prompt = f"""
You are an AI email intelligence system.

Extract structured data from this email.

Return ONLY valid JSON (no explanation, no markdown).

Schema:
{{
  "category": "Internship | Hackathon | Scholarship | Fellowship | Certificate | Promotion | Spam | Personal",
  "opportunity_name": "string or null",
  "deadline": "string or null",
  "action_required": "string or null"
}}

Rules:
- If it is security alert, login alert, or ads → category = "Spam"
- If no opportunity exists → category = "Spam"
- Keep values short and clean
- Output must be ONLY JSON

EMAIL:
\"\"\"{email_text}\"\"\"
"""

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = response.text

            # SAFE JSON extraction
            match = re.search(r"\{.*\}", text, re.S)

            if match:
                return json.loads(match.group())

            raise ValueError("No JSON found")

        except Exception as e:

            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5 * attempt)

    return {
        "category": "Error",
        "opportunity_name": None,
        "deadline": None,
        "action_required": None
    }