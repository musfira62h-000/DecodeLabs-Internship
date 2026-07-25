# Task 3 — The Data Warehouse (AWS RDS MySQL)

Managed cloud database on **AWS RDS (MySQL)** in a **private subnet**, accessed via **SSH tunnel**.

## Milestone checklist
- [ ] MySQL/MariaDB RDS in a **private subnet**
- [ ] Security Group locked to **port 3306**
- [ ] Table `Interns` with **PRIMARY KEY**, **UNIQUE**, **NOT NULL**
- [ ] Dummy records via `INSERT INTO`
- [ ] Screenshot of `SELECT` via **MySQL Workbench** or **Python** over **SSH tunnel**

## Files
- `schema.sql` — creates `Interns`
- `seed.sql` — dummy rows
- `insert_interns.py` — Python connector (via tunnel)
- `requirements.txt` / `.env.example`
- `LIVE-LINK.md` — fill after RDS is created
- `ssh-tunnel.example.ps1` — tunnel command template

## Architecture (what you build)
1. **VPC** with public + private subnets  
2. **EC2 bastion** in public subnet (SSH port 22)  
3. **RDS MySQL** in private subnet (not publicly accessible)  
4. **RDS Security Group:** inbound **3306** only from the bastion SG  
5. Connect from your PC with SSH tunnel → MySQL Workbench / Python

## Quick connect (after infra exists)
```powershell
# Terminal 1 — keep this open (SSH tunnel)
ssh -i "C:\Users\hp\Downloads\your-key.pem" -L 3307:YOUR-RDS-ENDPOINT:3306 ec2-user@BASTION-PUBLIC-IP -N

# Terminal 2 — Python
cd "C:\Users\hp\Documents\Decodelabs_task1\Task-3-Data-Warehouse"
pip install -r requirements.txt
copy .env.example .env
# edit .env with password, then:
python insert_interns.py
```

Or MySQL Workbench: host `127.0.0.1`, port `3307`, user/password from RDS.

## Cost tip
Stop/terminate EC2 + delete RDS when grading is done (RDS is the main cost).
