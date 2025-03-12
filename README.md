# Pterodactyl Monitoring Dashboard

🚀 **Pterodactyl Monitoring Dashboard** – Web dashboard berbasis **Flask** untuk memantau status server di **Pterodactyl Panel**.

## 🔹 Fitur
✅ Cek status server (Online/Offline)  
✅ Monitor penggunaan **CPU, RAM, dan Disk**  
✅ **API endpoint** untuk integrasi eksternal  
✅ Notifikasi otomatis ke **Telegram** jika server down  
✅ UI sederhana berbasis **HTML + Flask**  

## 💻 Language
- Python (Flask)
- Pterodactyl API
- Telegram Bot API

## 📌 How To Use?

### 1️⃣ Clone Repository & Masuk ke Folder
```bash
git clone https://github.com/davinclouds/pterodactyl-monitoring.git
cd pterodactyl-monitoring
```

### 2️⃣ Install Dependensi
```bash
pip install flask requests
```

### 3️⃣ Konfigurasi API
Edit file `app.py` dan isi dengan **API Key** serta **Telegram Bot Token**:
```python
PANEL_URL = "https://your-pterodactyl-panel.com"
API_KEY = "your_api_key_here"
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
```

### 4️⃣ Jalankan Aplikasi
```bash
python app.py
```

Akses dashboard melalui: **http://localhost:5000**

## 🔗 API Endpoint
**Cek status server via API:**
```bash
GET /api/status
```
Response:
```json
{
    "status": "RUNNING",
    "cpu": "15%",
    "ram": "512 MB",
    "disk": "10 GB"
}
```

## 🛠 Lisensi
Proyek ini menggunakan **MIT License** – bebas digunakan dan dimodifikasi!

---
💡 **Contributions Welcome!** Jika ingin menambahkan fitur baru, silakan buat pull request! 🚀
