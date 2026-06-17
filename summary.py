from database import get_all_opportunities
from datetime import datetime

def generate_summary():

    rows = get_all_opportunities()

    internships = []
    hackathons = []

    for r in rows:

        if r[1] == "Internship":
            internships.append(r)

        elif r[1] == "Hackathon":
            hackathons.append(r)

    print("\n📬 DAILY OPPORTUNITY SUMMARY")
    print("=" * 50)

    print("\n🔥 Internships:")
    for i in internships:
        print(f"- {i[2]} | Deadline: {i[3]}")

    print("\n🚀 Hackathons:")
    for h in hackathons:
        print(f"- {h[2]} | Deadline: {h[3]}")

    print("\n📊 Total Opportunities:", len(rows))
    print("=" * 50)


if __name__ == "__main__":
    generate_summary()