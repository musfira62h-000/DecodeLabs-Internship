# AWS RDS Connection Details

**Engine:** MySQL (RDS)  
**RDS endpoint:** *(fill after create — e.g. `decodelabs-interns.xxxxx.ap-south-1.rds.amazonaws.com`)*  
**Port:** `3306`  
**Database name:** `internsdb`  
**Master username:** *(e.g. `admin`)*  
**Access:** Private subnet → connect via **SSH tunnel** through EC2 bastion  

**Bastion public IP:** *(fill)*  
**Key pair:** *(e.g. `decodelabs-key.pem`)*

## Tunnel command
```powershell
ssh -i "C:\path\to\key.pem" -L 3307:YOUR-RDS-ENDPOINT:3306 ec2-user@BASTION-PUBLIC-IP -N
```

Then connect to `127.0.0.1:3307` with MySQL Workbench or `python insert_interns.py`.

> Do **not** commit the RDS password or `.pem` key to GitHub.
