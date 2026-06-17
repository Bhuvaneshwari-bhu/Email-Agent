def is_important(data):

    important_categories = [
        "Internship",
        "Hackathon",
        "Scholarship",
        "Fellowship"
    ]

    return (
        data["category"]
        in important_categories
    )

def generate_report(opportunities):

    print("\n📬 DAILY OPPORTUNITY DIGEST\n")

    for item in opportunities:

        print(
            f"🔥 {item['opportunity_name']}"
        )

        print(
            f"Category: {item['category']}"
        )

        print(
            f"Deadline: {item['deadline']}"
        )

        print(
            f"Action: {item['action_required']}"
        )

        print("-" * 40)