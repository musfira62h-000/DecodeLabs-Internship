# Example SSH tunnel: local 3307 -> private RDS:3306 via EC2 bastion
# Edit the values, then run in PowerShell. Keep the window open while using Workbench/Python.

$KeyPath = "$HOME\Downloads\your-key.pem"
$BastionIP = "x.x.x.x"
$RdsEndpoint = "your-db.xxxxx.region.rds.amazonaws.com"
$LocalPort = 3307

ssh -i $KeyPath -L "${LocalPort}:${RdsEndpoint}:3306" "ec2-user@$BastionIP" -N
