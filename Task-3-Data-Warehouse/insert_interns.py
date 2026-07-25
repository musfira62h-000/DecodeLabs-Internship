"""
DecodeLabs Project 3 (Azure PostgreSQL) - connect and verify Interns data.
"""

import os
import sys

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
except ImportError:
    print("Missing dependency. Run: pip install -r requirements.txt")
    sys.exit(1)


def load_env():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.isfile(env_path):
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()

HOST = os.getenv("DB_HOST", "decodelabs-interns-mysql.postgres.database.azure.com")
PORT = os.getenv("DB_PORT", "5432")
DBNAME = os.getenv("DB_NAME", "postgres")
USER = os.getenv("DB_USER", "decodelabsinterns1")
PASSWORD = os.getenv("DB_PASSWORD", "")
SSLMODE = os.getenv("DB_SSLMODE", "require")


def main():
    if not PASSWORD:
        print("Set DB_PASSWORD in .env (see .env.example).")
        sys.exit(1)

    print(f"Connecting to {HOST} ...")
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DBNAME,
        user=USER,
        password=PASSWORD,
        sslmode=SSLMODE,
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Interns (
          id SERIAL PRIMARY KEY,
          Name  VARCHAR(100) NOT NULL,
          Role  VARCHAR(100) NOT NULL,
          Email VARCHAR(150) NOT NULL UNIQUE
        );
        """
    )

    rows = [
        ("Musfira Hassan", "Cyber Security Intern", "musfirahassan13@gmail.com"),
        ("Ali Khan", "Cloud Engineer Intern", "ali.khan@example.com"),
        ("Sara Ahmed", "Frontend Developer Intern", "sara.ahmed@example.com"),
        ("Omar Raza", "DevOps Intern", "omar.raza@example.com"),
        ("Hina Malik", "Data Analyst Intern", "hina.malik@example.com"),
    ]
    for name, role, email in rows:
        cur.execute(
            """
            INSERT INTO Interns (Name, Role, Email)
            VALUES (%s, %s, %s)
            ON CONFLICT (Email) DO NOTHING;
            """,
            (name, role, email),
        )

    conn.commit()
    cur.execute("SELECT id, Name, Role, Email FROM Interns ORDER BY id;")
    results = cur.fetchall()
    print(f"\nInterns table ({len(results)} rows):")
    print("-" * 70)
    for r in results:
        print(f"{r['id']:>3} | {r['Name']:<20} | {r['Role']:<26} | {r['Email']}")
    print("-" * 70)
    print("Done. Data persisted in Azure PostgreSQL.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
