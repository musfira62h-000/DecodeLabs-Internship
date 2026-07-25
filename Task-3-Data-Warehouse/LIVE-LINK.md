# Azure PostgreSQL Connection Details

**Service:** Azure Database for PostgreSQL Flexible Server  
**Server name:** `decodelabs-interns-mysql`  
**Endpoint:** `decodelabs-interns-mysql.postgres.database.azure.com`  
**Port:** `5432`  
**Database:** `postgres`  
**Admin username:** `decodelabsinterns1`  
**Table:** `Interns` (`Name`, `Role`, `Email`) — PRIMARY KEY, UNIQUE, NOT NULL  

## Screenshots
- `screenshots/01-deployment-complete.png` — deployment succeeded  
- `screenshots/02-server-overview.png` — server overview / endpoint  
- `screenshots/03-select-interns.png` — `SELECT * FROM Interns;` (5 rows verified)

## Verification
Table created + 5 dummy rows inserted via Cloud Shell (`psql`). Status: **Complete** ✅

> Password is private — do not commit it.  
> Note: server name contains "mysql" but the engine is **PostgreSQL**.
