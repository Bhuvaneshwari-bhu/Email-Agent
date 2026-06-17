from gmail_reader import authenticate_gmail
from agent import extract_email
service = authenticate_gmail()

results = service.users().messages().list(
    userId='me',
    maxResults=5
).execute()

messages = results.get('messages', [])

print("Latest emails:")

import base64

def get_email_body(payload):

    if 'parts' in payload:

        for part in payload['parts']:

            mime_type = part.get('mimeType', '')

            if mime_type in ['text/plain', 'text/html']:

                data = part['body'].get('data')

                if data:
                    return base64.urlsafe_b64decode(data).decode(errors="ignore")

    else:

        data = payload['body'].get('data')

        if data:
            return base64.urlsafe_b64decode(data).decode(errors="ignore")

    return ""

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

    keywords = ["internship", "hackathon", "apply", "deadline", "job", "register"]

    if not any(k in text_check for k in keywords):
        print("Skipped (not relevant)")
        continue


    email_text = f"""
        From: {sender}
        Subject: {subject}
        Body: {body}
        """

    result = extract_email(email_text)

    print("\n======================")
    print("From:", sender)
    print("Subject:", subject)
    print("AI RESULT:", result)