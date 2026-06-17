from database import (
    get_all_opportunities,
    get_by_category
)

from router import route_query
from parser import parse_response

ALLOWED_TOOLS = {
    "get_all_opportunities",
    "get_by_category"
}

def display_rows(rows):

    if not rows:
        print("\nNo opportunities found.")
        return

    for row in rows:

        print("\n" + "=" * 50)

        print(f"📌 {row[2]}")
        print(f"Category : {row[1]}")
        print(f"Deadline : {row[3]}")
        print(f"Action   : {row[4]}")

        print("=" * 50)


while True:

    query = input("\nYou: ")

    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    try:

        route = parse_response(
            route_query(query)
        )

        print("\nAgent Decision:")
        print(route)

        tool = route.get("tool")

        if tool not in ALLOWED_TOOLS:
            print("\nInvalid tool selected by AI. Please try again.")
            continue

        if tool == "get_all_opportunities":

            rows = get_all_opportunities()

            display_rows(rows)

        elif tool == "get_by_category":

            category = route.get("category")
            if not category:
                print("\nCategory not specified.")
                continue
            rows = get_by_category(category)

            display_rows(rows)

        else:
             print("\nI couldn't understand your request. Try:")
    except Exception as e:

        print(
            f"\nError: {e}"
        )