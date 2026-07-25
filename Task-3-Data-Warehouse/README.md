# Task 3 — The Data Warehouse (Azure PostgreSQL)

Managed cloud database on **Azure Database for PostgreSQL Flexible Server**.

**Server:** `decodelabs-interns-mysql.postgres.database.azure.com`  
**Admin:** `decodelabsinterns1`

## Screenshots
See [`screenshots/`](./screenshots/) for proof:
- `01-deployment-complete.png`
- `02-server-overview.png`
- `03-select-interns.png` — Interns table with 5 rows ✅

## Files
- `schema.sql` / `seed.sql` — table + dummy data
- `insert_interns.py` — Python connector (bonus)
- `LIVE-LINK.md` — connection details

## Connect (Cloud Shell)
```bash
psql "host=decodelabs-interns-mysql.postgres.database.azure.com port=5432 dbname=postgres user=decodelabsinterns1 sslmode=require"
```

Then run `schema.sql` + `seed.sql` contents, or:
```sql
SELECT * FROM Interns;
```

## Cost tip
Stop/delete the server when finished.
