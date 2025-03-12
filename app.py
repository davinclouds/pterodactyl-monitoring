# Website Monitoring for Pterodactyl Panel (Web Dashboard)
#
# Features:
# - Web dashboard with Flask
# - Check server status (online/offline)
# - Fetch resource usage (CPU, RAM, Disk)
# - API integration with Pterodactyl
# - Send alerts via Telegram
# - HTML template for web UI

from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

# Pterodactyl API Credentials
PANEL_URL = "https://your-pterodactyl-panel.com"
API_KEY = "your_api_key_here"

# Telegram Bot Credentials
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "Application/vnd.pterodactyl.v1+json"
}

def get_server_status(server_id):
    url = f"{PANEL_URL}/api/client/servers/{server_id}/resources"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        attributes = data["attributes"]
        status = attributes["current_state"]
        cpu = attributes["resources"]["cpu_absolute"]
        ram = attributes["resources"]["memory_bytes"] // (1024 * 1024)
        disk = attributes["resources"]["disk_bytes"] // (1024 * 1024)
        
        return {
            "status": status.upper(),
            "cpu": f"{cpu}%",
            "ram": f"{ram} MB",
            "disk": f"{disk} MB"
        }
    else:
        return None

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

@app.route('/')
def index():
    server_id = "your_server_id_here"
    data = get_server_status(server_id)
    return render_template("index.html", data=data)

@app.route('/api/status')
def api_status():
    server_id = "your_server_id_here"
    data = get_server_status(server_id)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch server status"}), 500

if __name__ == "__main__":
    app.run(debug=True)
