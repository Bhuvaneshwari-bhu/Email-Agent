from gmail_reader import authenticate_gmail
from agent import extract_email
from database import save_opportunity
import base64


def get_email_body(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part.get('mimeType') in ['text/plain', 'text/html']:
                data = part['body'].get('data')
                if data:
                    return base64.urlsafe_b64decode(data).decode(errors="ignore")
    else:
        data = payload['body'].get('data')
        if data:
            return base64.urlsafe_b64decode(data).decode(errors="ignore")

    return ""


def sync_emails():
    service = authenticate_gmail()

    results = service.users().messages().list(
        userId='me',
        maxResults=3
    ).execute()

    messages = results.get('messages', [])

    print("\n📡 Syncing Gmail...\n")

    for msg in messages:

        msg_data = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='full'
        ).execute()

        payload = msg_data['payload']
        headers = payload['headers']

        subject = ""
        sender = ""

        for h in headers:
            if h['name'] == 'Subject':
                subject = h['value']
            if h['name'] == 'From':
                sender = h['value']

        body = get_email_body(payload)

        text_check = (subject + body).lower()

        keywords = [
            "internship",
            "hackathon",
            "scholarship",
            "fellowship",
            "apply",
            "application",
            "deadline",
            "selection",
            "job",
            "career",
            "opportunity",
            "register",
            "recruitment",
            "assessment",
            "interview",
            "bootcamp",
            "program"
        ]

        if not any(k in text_check for k in keywords):
            print(f"Skipped: {subject}")
            continue

        email_text = f"""
From: {sender}
Subject: {subject}
Body: {body}
"""

        try:
            result = extract_email(email_text)

            if not result:
                print("Skipped (empty AI response)")
                continue

            if not isinstance(result, dict):
                print("Skipped (invalid AI format)")
                continue

            if (
                result.get("category")
                and result.get("category") != "Spam"
                and result.get("opportunity_name")
                and result.get("opportunity_name").strip()
            ):
                save_opportunity(result)
                print("Saved:", result.get("opportunity_name"))

        except Exception as e:
            print("Failed:", e)


if __name__ == "__main__":
    sync_emails()