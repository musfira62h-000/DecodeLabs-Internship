# Task 3 — The Data Warehouse (Azure MySQL)

Managed cloud database on **Azure Database for MySQL Flexible Server**.

## Milestone mapping
- Managed MySQL cloud DB (Azure equivalent of AWS RDS MySQL)
- Port **3306**
- Table `Interns` with **PRIMARY KEY**, **UNIQUE**, **NOT NULL**
- Dummy records via `INSERT`
- Verify with `SELECT` (Cloud Shell / MySQL client / Python)

## Files
- `schema.sql` — creates `Interns`
- `seed.sql` — dummy rows
- `insert_interns.py` — Python connector
- `.env.example` / `requirements.txt`
- `LIVE-LINK.md` — fill after server is created

## Azure setup
1. Portal → **Azure Database for MySQL flexible servers** → **Create**
2. Resource group: `portfolio-rg2`
3. Server name: `decodelabs-interns-mysql` (must be unique)
4. Region: Central India · Workload: Development · smallest compute (Burstable)
5. Admin username + strong password (save them)
6. Networking: public access + **Add current client IP**
7. Create → then create database `internsdb`
8. Run `schema.sql` + `seed.sql` (or `python insert_interns.py`)

## Verify
```sql
SELECT * FROM Interns;
```

## Cost tip
**Stop** or **Delete** the MySQL server when finished.
