import os
from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def classify_email(email_text):

    prompt = f"""
    Classify this email into ONE category:

    Internship
    Scholarship
    Hackathon
    Fellowship
    Certificate
    Promotion
    Spam
    Personal

    Email:
    {email_text}

    Return only the category.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()

def analyze_email(email_text):

    prompt = f"""
    Analyze this email.

    Return ONLY valid JSON.

    {{
      "category":"",
      "opportunity_name":"",
      "deadline":"",
      "action_required":""
    }}

    Email:
    {email_text}
    """

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"Attempt {attempt+1} failed")

            time.sleep(3)

    return """
    {
      "category":"Error",
      "opportunity_name":"",
      "deadline":"",
      "action_required":""
    }
    """