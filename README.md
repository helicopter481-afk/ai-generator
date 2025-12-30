# 🚀 ContentHub - Hook & Caption Generator

Generator konten AI untuk membuat hook dan caption viral yang siap posting langsung ke media sosial. Dibuat dengan Flask + Groq API + Tailwind CSS.

## ✨ Fitur

- **🔥 Hook Generator** - 5 hook pembuka yang provokatif dan relatable
- **📝 Multi-Caption Variants** - Super singkat, singkat, dan normal untuk berbagai kebutuhan
- **🎯 Smart CTA** - Call-to-action yang natural dan tidak maksa
- **📱 Responsive Design** - Berfungsi sempurna di desktop, tablet, dan mobile
- **⚡ Loading State** - User feedback visual saat AI sedang bekerja
- **📋 Copy Button** - Copy dengan 1 klik langsung ke clipboard
- **🎨 Modern UI** - Gradient colors, smooth animations, dan polished design

## 📋 Requirements

- Python 3.8+
- Flask
- Groq API Key
- pip (Python package manager)

## 🔧 Setup

### 1. Clone atau buat project folder
```bash
cd your-project-directory
```

### 2. Buat virtual environment
```bash
python -m venv .venv
```

### 3. Aktivasi virtual environment
**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup environment variables
Buat file `.env` di root project:
```env
GROQ_API_KEY=your_api_key_here
FLASK_ENV=development
FLASK_DEBUG=1
```

Dapatkan API key gratis di: https://console.groq.com

### 6. Jalankan aplikasi
```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## 🎯 Cara Menggunakan

1. **Isi Jenis Usaha/Produk** - Contoh: "Kopi Premium", "Tas Kulit", "Jasa Design"
2. **Tentukan Target Audiens** - Contoh: "Profesional muda", "Ibu rumah tangga"
3. **Pilih Platform** - Instagram, TikTok, WhatsApp, Facebook, LinkedIn
4. **Tentukan Gaya Bahasa** - Santai, Profesional, Promosi, Edukatif, Humoris
5. **Klik "Buat Konten Sekarang"** - Tunggu hasil dalam hitungan detik
6. **Copy hasil yang dibutuhkan** - Langsung siap posting!

## 📁 Struktur Project

```
content-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (jangan commit!)
├── static/
│   └── style.css         # Custom CSS (optional)
└── templates/
    └── index.html        # Main UI
```

## 🔑 Groq API Key

1. Kunjungi https://console.groq.com
2. Daftar dengan akun Anda
3. Buat API key baru
4. Copy key dan paste di `.env` file sebagai `GROQ_API_KEY`

## 🌐 Deployment

### Heroku
```bash
# Install Heroku CLI, lalu:
heroku login
heroku create your-app-name
git push heroku main
```

### PythonAnywhere
1. Upload project ke PythonAnywhere
2. Setup virtual environment
3. Konfigurasi web app dengan Flask
4. Set GROQ_API_KEY di environment variables

### Railway / Render
1. Push repo ke GitHub
2. Connect repository
3. Set environment variables
4. Deploy!

## 🎨 Customization

### Mengubah Model AI
Edit di `app.py` baris `model="llama-3.1-8b-instant"`:
```python
model="mixtral-8x7b-32768"  # Model lain yang lebih powerful
```

### Mengubah Prompt
Edit function `build_prompt()` di `app.py` untuk customize instruksi AI.

### Mengubah Tampilan
- Edit `templates/index.html` untuk mengubah struktur
- Modifikasi color gradient di `<style>` section
- Adjust Tailwind classes sesuai kebutuhan

## 🐛 Troubleshooting

### "Invalid API Key"
- Pastikan GROQ_API_KEY benar di `.env`
- Restart aplikasi setelah menambah `.env`
- Verify API key di console.groq.com

### "Module not found"
```bash
pip install -r requirements.txt
```

### Port 5000 sudah terpakai
Edit `app.py`:
```python
app.run(debug=True, port=5001)
```

## 📊 Performance Tips

- **Cache hasil** jika input sama untuk menghemat API quota
- **Reduce token limit** jika respons terlalu panjang (edit `max_tokens=1024`)
- **Batch requests** untuk penggunaan komersial

## 📄 License

MIT License - Bebas digunakan untuk personal dan komersial

## 💬 Support

Butuh bantuan? Buat issue atau hubungi developer.

---

**Made with ❤️ for Indonesian UMKM**
