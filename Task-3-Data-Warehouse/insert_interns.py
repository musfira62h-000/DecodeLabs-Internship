"""
DecodeLabs Project 3 (Azure) - connect to Azure Database for MySQL and verify Interns data.

Setup:
  1. pip install -r requirements.txt
  2. Copy .env.example to .env and fill credentials
  3. python insert_interns.py
"""

import os
import sys

try:
    import pymysql
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

HOST = os.getenv("DB_HOST", "")
PORT = int(os.getenv("DB_PORT", "3306"))
DBNAME = os.getenv("DB_NAME", "internsdb")
USER = os.getenv("DB_USER", "")
PASSWORD = os.getenv("DB_PASSWORD", "")
SSL = os.getenv("DB_SSL", "true").lower() in ("1", "true", "yes")


def main():
    if not HOST or not USER or not PASSWORD:
        print("Set DB_HOST, DB_USER, and DB_PASSWORD in .env (see .env.example).")
        sys.exit(1)

    print(f"Connecting to Azure MySQL at {HOST}:{PORT} / {DBNAME} ...")
    conn = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DBNAME,
        ssl={"ssl": {}} if SSL else None,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Interns (
          id INT AUTO_INCREMENT PRIMARY KEY,
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
            INSERT IGNORE INTO Interns (Name, Role, Email)
            VALUES (%s, %s, %s);
            """,
            (name, role, email),
        )

    cur.execute("SELECT id, Name, Role, Email FROM Interns ORDER BY id;")
    results = cur.fetchall()
    print(f"\nInterns table ({len(results)} rows):")
    print("-" * 70)
    for r in results:
        print(f"{r['id']:>3} | {r['Name']:<20} | {r['Role']:<26} | {r['Email']}")
    print("-" * 70)
    print("Done. Data persisted in Azure Database for MySQL.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
