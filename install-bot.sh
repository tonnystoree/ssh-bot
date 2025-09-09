#!/bin/bash
# Auto Installer Bot Telegram SSH

echo ">>> Update & install dependencies"
apt update && apt upgrade -y
apt install -y python3 python3-pip git

echo ">>> Clone repo bot"
rm -rf /root/ssh-bot
git clone https://github.com/tonnystoree/ssh-bot.git /root/ssh-bot

echo ">>> Install Python requirements"
pip3 install -r /root/ssh-bot/requirements.txt

echo ">>> Buat service systemd"
cat > /etc/systemd/system/sshbot.service << END
[Unit]
Description=Telegram SSH Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /root/ssh-bot/bot.py
WorkingDirectory=/root/ssh-bot
Restart=always
User=root

[Install]
WantedBy=multi-user.target
END

echo ">>> Reload & start service"
systemctl daemon-reload
systemctl enable sshbot
systemctl start sshbot

echo ">>> Bot Berhasil Diinstall & Berjalan Otomatis 24 Jam ✅"
