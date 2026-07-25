# Task 3 — The Data Warehouse

Provision a managed cloud database, create an `Interns` table, and insert dummy records.

**Cloud:** Azure Database for PostgreSQL (managed / DBaaS)  
**Bonus:** Python script to connect and verify data persistence

## Files
- `schema.sql` — creates `Interns (Name, Role, Email)`
- `seed.sql` — dummy records
- `insert_interns.py` — bonus Python connector
- `requirements.txt` — Python deps
- `.env.example` — DB credentials template (copy to `.env`, never commit `.env`)
- `LIVE-LINK.md` — server / connection details after setup

## Azure setup (short)
1. Portal → **Azure Database for PostgreSQL flexible servers** → **Create**
2. Resource group: `portfolio-rg2` · Server name: `decodelabs-interns-db` · Region: Central India
3. Workload: **Development** · Compute: smallest burstable (e.g. **B1ms**)
4. Admin username + strong password (save them)
5. Networking: **Allow public access** + **Allow public access from any Azure service** + add your client IP (firewall)
6. Create → open server → **Database** ready
7. Connect with **Azure Cloud Shell** / **pgAdmin** / **psql** / Python:
   - Run `schema.sql` then `seed.sql`
   - Or: `pip install -r requirements.txt` → copy `.env.example` to `.env` → `python insert_interns.py`

## Verify
```sql
SELECT * FROM Interns;
```
You should see your dummy rows — data persists in the cloud.

## Cost tip
Stop / delete the PostgreSQL server when grading is done to save Azure credit.
