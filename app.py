from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)
app.secret_key = "content-generator-secret-key"

# Password untuk akses (satu password saja - tidak bisa diubah)
PASSWORD = "ayomulai123"  # ← GANTI DENGAN PASSWORD ANDA

def build_prompt(usaha, audiens, platform, gaya):
    gaya_detail = {
        "Santai": """
SANTAI = Casual, relaxed, fun, kayak ngobrol temen di kafe.
- Tone: bersahabat, nggak perlu formal, bisa pakai jokes ringan
- Sentence: pendek, broken, natural
- Vibe: "eh coba ini", "lumayan sih", "worth it deh"
- Jangan: terlalu serious, terlalu banyak emoji, nada condescending
- Contoh hook: "lagi cari yg legit?" "ini sih top tier" "worth the hype banget"
- Contoh caption: "honestly ini oke banget. nggak overrated. recommended sih"
- Contoh CTA: "coba aja", "cek dm", "swipe up"
""",
        "Profesional": """
PROFESIONAL = Business tone tapi tetap human, credible, trustworthy.
- Tone: expert yang bisa dipercaya, informed, jelas value propositionnya
- Sentence: structured tapi jangan kaku, tetap natural
- Vibe: "here's why", "proven to be", "solution untuk", "hasil nyata"
- Jangan: klise, terlalu salesy, jargon berlebihan
- Contoh hook: "cari solusi yang terbukti?" "kualitas yang bisa dipercaya" "hasil yang terukur"
- Contoh caption: "ini sudah teruji. kualitasnya consistent. value-nya jelas. customer juga satisfied"
- Contoh CTA: "hubungi kami untuk konsultasi", "lihat case study", "request demo"
""",
        "Promosi": """
PROMOSI = Sales-driven tapi tetap smart, nggak desperate.
- Tone: exciting, highlight keuntungan/value, bikin FOMO tapi subtle
- Sentence: energik, highlight benefits dan urgency
- Vibe: "limited", "promo", "grab while it lasts", "harga special", "bonus"
- Jangan: terlalu clickbait, aggressive, fake urgency
- Contoh hook: "promo terbatas nih!" "stok terbatas, jangan kehabisan" "harga spesial hari ini"
- Contoh caption: "promo akhir bulan. harga turun banyak. gratis ongkir juga. jangan sampai kehabisan deh"
- Contoh CTA: "order sekarang", "claim promo", "stok limited, pesan yuk"
""",
        "Edukatif": """
EDUKATIF = Kasih tahu, educate audience, value-add.
- Tone: teacher/expert yang sharing knowledge, helpful
- Sentence: clear, informative, ada flow logis
- Vibe: "tau nggak", "jadi gini", "tips", "yang perlu kamu tahu", "ilmu"
- Jangan: boring, terlalu panjang, condescending
- Contoh hook: "tau nggak sih bedanya?" "ini yang sering terlewat" "perlu banget tau ini"
- Contoh caption: "banyak yang salah di sini. yang baik itu harus X dan Y. ini punya keduanya. plus bonus Z juga"
- Contoh CTA: "pelajari lebih lanjut", "baca artikel lengkapnya", "tanya ahlinya"
""",
        "Humoris": """
HUMORIS = Lucu, witty, banyak jokes atau observasi absurd yang relate.
- Tone: funny, sarcastic, dark humor (sesuai audiens), playful
- Sentence: punchline setup, unexpected turn, meme reference
- Vibe: "relatable humor", punchlines, jokes about customer pain points
- Jangan: jokes yang nggak relate, offensive, terlalu out-of-context
- Contoh hook: "udah coba puluhan? ini yang ngga mengecewain" "kalau ini nggak bisa, nothing will" "ini candu parah gw ngl"
- Contoh caption: "gw trauma sama brand lain tbh. ini akhirnya yang enak. semoga idup lama banget lol. jangan discontinued please"
- Contoh CTA: "grab sekarang sebelum gw abiskan sendiri", "mau jadi addict juga?", "join the cult"
"""
    }
    
    gaya_instruction = gaya_detail.get(gaya, gaya_detail["Santai"])
    
    return f"""Kamu adalah copywriter Gen-Z/Millennial yang nulis caption buat Instagram/TikTok.
Tulisan kamu CASUAL, AUTHENTIC, dan SEPERTI NGOBROL AMA TEMEN.

TONE YANG HARUS KEDENGERAN:
• Natural pakai kata-kata sehari-hari (nggak, nih, deh, sih, lah)
• Kalimat PENDEK. Jangan panjang-panjang
• Pakai feeling, bukan spesifikasi teknis
• Fragment sentences allowed (tidak harus sempurna grammar)
• Tulis SEPERTI CERITA ASLI

GAYA BAHASA YANG DIMINTA - IKUTI INI PERSIS:
{gaya_instruction}

KONTEKS:
🎯 Produk: {usaha}
👥 Target: {audiens}
📱 Platform: {platform}
💬 Tone: {gaya}

FORMAT OUTPUT (HARUS PERSIS):

**Hook:**
1. (maksimal 8 kata, sesuai gaya {gaya})
2. (maksimal 8 kata, sesuai gaya {gaya})
3. (maksimal 8 kata, sesuai gaya {gaya})
4. (maksimal 8 kata, sesuai gaya {gaya})
5. (maksimal 8 kata, sesuai gaya {gaya})

**Caption_Singkat:**
1-2 kalimat, tone seperti temen rekomendasi, sesuai gaya {gaya}. HARUS TERASA BERBEDA dari gaya lain.

**Caption_Normal:**
3-4 kalimat cerita relatable + solution, sesuai gaya {gaya}. HARUS TERASA BERBEDA dari gaya lain.

**Caption_Super_Singkat:**
1 kalimat super punchy, sesuai gaya {gaya}. HARUS TERASA BERBEDA dari gaya lain.

**CTA:**
1. (sesuai gaya {gaya})
2. (sesuai gaya {gaya})
3. (sesuai gaya {gaya})

PENTING: Setiap output harus JELAS TERASA BERBEDA karena gaya {gaya}. Jangan samaan sama gaya lain!
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == PASSWORD:
            session["authenticated"] = True
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Password salah!")
    return render_template("login.html")

@app.route("/")
def index():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/generate", methods=["POST"])
def generate():
    if not session.get("authenticated"):
        return jsonify({"status": "error", "message": "Unauthorized"}), 401
    
    data = request.json
    # Validasi input
    if not all([data.get("usaha"), data.get("audiens"), data.get("platform"), data.get("gaya")]):
        return jsonify({
            "status": "error",
            "message": "Semua field harus diisi"
        }), 400

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": build_prompt(
                        data["usaha"],
                        data["audiens"],
                        data["platform"],
                        data["gaya"]
                    )
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        content = completion.choices[0].message.content
        
        hooks = extract_section(content, "HOOK")
        caption_singkat = extract_text(content, "CAPTION_SINGKAT")
        caption_normal = extract_text(content, "CAPTION_NORMAL")
        caption_super = extract_text(content, "CAPTION_SUPER_SINGKAT")
        cta = extract_section(content, "CTA")
        
        return jsonify({
            "status": "ok",
            "data": {
                "hooks": hooks if hooks else [],
                "caption_singkat": caption_singkat,
                "caption_normal": caption_normal,
                "caption_super": caption_super,
                "cta": cta if cta else [],
                "raw": content
            }
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({
            "status": "error",
            "message": "Layanan sedang padat. Coba lagi dalam beberapa saat."
        }), 500

def extract_section(text, section_name):
    """Extract bulleted/numbered items from a section"""
    import re
    # Look for **Section:** format instead of Section:
    pattern = rf"\*\*{section_name}[:\*]*\*\*\s*\n([\s\S]*?)(?=\n\*\*|$)"
    match = re.search(pattern, text, re.IGNORECASE)
    
    if not match:
        # Try alternative format without bold
        pattern_alt = rf"{section_name}:\s*\n([\s\S]*?)(?=\n[A-Z]|$)"
        match = re.search(pattern_alt, text, re.IGNORECASE)
        if not match:
            return []
    
    section = match.group(1).strip()
    items = []
    
    # Extract numbered items (1. "text", 2. "text", etc) or bullet items
    for line in section.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Remove numbering (1., 2., etc)
        if re.match(r'^\d+\.\s+', line):
            line = re.sub(r'^\d+\.\s+', '', line)
        # Remove bullet points
        elif line.startswith('- '):
            line = line[2:]
        elif line.startswith('-'):
            line = line[1:]
        
        # Remove quotes if present
        line = line.strip().strip('"').strip("'")
        
        if line:
            items.append(line)
    
    return items

def extract_text(text, section_name):
    """Extract paragraph text from a section"""
    import re
    
    # Build flexible pattern to match section name with different cases/underscores
    # Convert "CAPTION_SINGKAT" to pattern that matches "Caption_Singkat", "CAPTION_SINGKAT", etc
    section_pattern = section_name.replace('_', '[_\\s]?')
    
    # Look for **Section:** format (case insensitive)
    pattern = rf"\*\*{section_pattern}[:\*]*\*\*\s*\n([\s\S]*?)(?=\n\*\*|$)"
    match = re.search(pattern, text, re.IGNORECASE)
    
    if not match:
        # Try alternative format without bold
        pattern_alt = rf"{section_pattern}:\s*\n([\s\S]*?)(?=\n[A-Z\*]|$)"
        match = re.search(pattern_alt, text, re.IGNORECASE)
        if not match:
            return ""
    
    content = match.group(1).strip()
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    if not lines:
        return ""
    
    # Join all lines, removing quotes
    result = ' '.join(lines)
    result = result.strip('"').strip("'")
    
    return result

if __name__ == "__main__":
    app.run(debug=True)

