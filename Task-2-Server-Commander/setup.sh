#!/usr/bin/env bash
#
# The Server Commander - one-shot web server setup (Ubuntu / Debian).
# Installs Apache, deploys the "Welcome to DecodeLabs" page, and starts the service.
#
# Usage (run ON the VM, from the folder that contains index.html):
#   chmod +x setup.sh
#   ./setup.sh
#
set -euo pipefail

echo "==> Updating packages..."
sudo apt update -y

echo "==> Installing Apache..."
sudo apt install -y apache2

echo "==> Enabling and starting Apache..."
sudo systemctl enable --now apache2

echo "==> Deploying the Welcome page..."
if [ -f "./index.html" ]; then
  sudo cp ./index.html /var/www/html/index.html
else
  echo "index.html not found next to the script - writing a fallback page."
  echo "<h1>Welcome to DecodeLabs</h1><p>Served from a self-managed Linux cloud server.</p>" \
    | sudo tee /var/www/html/index.html >/dev/null
fi

echo "==> Opening firewall for HTTP (if ufw is active)..."
sudo ufw allow 'Apache' 2>/dev/null || true

echo ""
echo "Done. Visit your server's public IP in a browser:  http://<your-server-ip>/"
echo "Apache status:"
sudo systemctl --no-pager status apache2 | head -n 5

# --- Amazon Linux / RHEL equivalent (use instead of the apt lines above) ---
#   sudo yum update -y
#   sudo yum install -y httpd
#   sudo systemctl enable --now httpd
#   sudo cp ./index.html /var/www/html/index.html
