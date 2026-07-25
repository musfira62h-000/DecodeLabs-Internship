"""
DecodeLabs Project 3 (AWS) - connect to RDS MySQL via SSH tunnel / local port.

Typical flow:
  1. Start SSH tunnel to private RDS through EC2 bastion:
       ssh -i key.pem -L 3307:YOUR-RDS-ENDPOINT:3306 ec2-user@BASTION-PUBLIC-IP -N
  2. Fill .env (see .env.example) — DB_HOST=127.0.0.1, DB_PORT=3307
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

HOST = os.getenv("DB_HOST", "127.0.0.1")
PORT = int(os.getenv("DB_PORT", "3307"))
DBNAME = os.getenv("DB_NAME", "internsdb")
USER = os.getenv("DB_USER", "admin")
PASSWORD = os.getenv("DB_PASSWORD", "")


def main():
    if not PASSWORD:
        print("Set DB_PASSWORD in .env (see .env.example).")
        sys.exit(1)

    print(f"Connecting to MySQL at {HOST}:{PORT} / {DBNAME} ...")
    conn = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DBNAME,
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
    print("Done. Data persisted in AWS RDS MySQL.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
