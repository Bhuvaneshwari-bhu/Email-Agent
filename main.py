from gmail_reader import load_emails
from agent import analyze_email
from parser import parse_response
from report_generator import (
    is_important,
    generate_report
)
from database import save_opportunity


emails = load_emails()

important = []
for email in emails:

    print("=" * 50)

    print(email["file"])

    result = analyze_email(
        email["content"]
    )

    data = parse_response(result)

    if is_important(data):
        important.append(data)
        save_opportunity(data)

generate_report(important)



# from agent import classify_email
# from agent import analyze_email
# sample_email = """
# Google Summer Internship Applications Open.

# Deadline July 15.

# Apply Now.
# Submit your resume and transcript
# """

# result = classify_email(sample_email)

# print(result)
# print(analyze_email(sample_email))


