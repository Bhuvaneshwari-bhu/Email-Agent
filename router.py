from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def route_query(user_query):

    prompt = f"""
    You are an AI router.

    Available tools:

    1. get_all_opportunities

    2. get_by_category

    Categories:
    Internship
    Hackathon
    Scholarship
    Fellowship

    Return ONLY JSON.

    Examples:

    User:
    show internships

    Output:
    {{
        "tool":"get_by_category",
        "category":"Internship"
    }}

    User:
    show everything

    Output:
    {{
        "tool":"get_all_opportunities"
    }}

    User Query:
    {user_query}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text