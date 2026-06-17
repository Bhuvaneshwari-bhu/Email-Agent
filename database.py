import sqlite3

conn = sqlite3.connect("opportunities.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    opportunity_name TEXT UNIQUE,
    deadline TEXT,
    action_required TEXT
)
""")

conn.commit()


def save_opportunity(data):
    
    try:
        if not data.get("opportunity_name"):
            return
        cursor.execute("""
        INSERT INTO opportunities
        (
            category,
            opportunity_name,
            deadline,
            action_required
        )
        VALUES (?, ?, ?, ?)
        """, (
            data["category"],
            data["opportunity_name"],
            data["deadline"],
            data["action_required"]
        ))

        conn.commit()

    except sqlite3.IntegrityError:

        print(
            f"Already exists: {data['opportunity_name']}"
        )


def show_opportunities():

    cursor.execute(
        "SELECT * FROM opportunities"
    )

    rows = cursor.fetchall()

    for row in rows:

        print("\n" + "=" * 40)

        print(f"📌 {row[2]}")
        print(f"Category: {row[1]}")
        print(f"Deadline: {row[3]}")
        print(f"Action: {row[4]}")

        print("=" * 40)

def get_by_category(category):

    cursor.execute(
        """
        SELECT * FROM opportunities
        WHERE category = ?
        """,
        (category,)
    )

    return cursor.fetchall()


def get_all_opportunities():

    cursor.execute(
        "SELECT * FROM opportunities"
    )

    return cursor.fetchall()


def get_categories():

    cursor.execute(
        """
        SELECT DISTINCT category
        FROM opportunities
        """
    )

    return cursor.fetchall()