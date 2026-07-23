# Task 2 — The Server Commander

Provision a Linux VM in the cloud, connect via SSH, install a web server, and host a
custom **"Welcome to DecodeLabs"** page.

**Live site:** http://20.244.1.237/  (see `LIVE-LINK.md`)

Hosted on an **Azure Virtual Machine** (Ubuntu + Apache).

## Files
- `index.html` — the "Welcome to DecodeLabs" page
- `setup.sh` — installs Apache and deploys the page (run on the VM)
- `LIVE-LINK.md` — the live URL (server public IP)

## Steps (Azure VM)
1. Azure Portal → **Virtual machines** → **Create** → Ubuntu 22.04, size **B1s**, auth = **SSH public key**.
2. Networking: allow inbound **SSH (22)** and **HTTP (80)**.
3. Connect: `ssh azureuser@<public-ip>`
4. Upload `index.html` (or paste it), then run:
   ```bash
   chmod +x setup.sh && ./setup.sh
   ```
   (or manually: `sudo apt update && sudo apt install -y apache2` then copy `index.html` to `/var/www/html/`)
5. Open `http://<public-ip>/` in a browser.

> AWS EC2 works the same way: launch Ubuntu/Amazon Linux, open ports 22 & 80, SSH in, install `apache2`/`httpd`.
