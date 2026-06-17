from database import get_all_opportunities
from report_generator import generate_report, is_important


def run_report():

    rows = get_all_opportunities()

    important = []

    for row in rows:

        data = {
            "category": row[1],
            "opportunity_name": row[2],
            "deadline": row[3],
            "action_required": row[4]
        }

        if is_important(data):
            important.append(data)

    generate_report(important)


if __name__ == "__main__":
    run_report()