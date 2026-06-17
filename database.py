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

        print(row)