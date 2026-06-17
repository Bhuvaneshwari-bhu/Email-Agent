import os

def load_emails(folder="emails"):

    emails = []

    for filename in os.listdir(folder):

        path = os.path.join(folder, filename)

        with open(path, "r") as f:

            content = f.read()

            emails.append({
                "file": filename,
                "content": content
            })

    return emails