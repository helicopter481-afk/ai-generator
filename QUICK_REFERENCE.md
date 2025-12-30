# 🎯 QUICK REFERENCE CARD

## ⚡ 30 DETIK SETUP

```bash
# 1. Install packages
pip install -r requirements.txt

# 2. Setup .env
cp .env.example .env
# → Edit .env, paste GROQ_API_KEY dari https://console.groq.com

# 3. Run
python app.py

# 4. Open http://localhost:5000
```

---

## 📝 FORM FILLING GUIDE

```
┌─────────────────────────────────────────────────┐
│ 💼 Jenis Usaha / Produk                         │
│                                                  │
│ ✅ "Kopi specialty arabika dari Aceh"          │
│ ✅ "Tas kulit handmade untuk wanita"            │
│ ✅ "Aplikasi manajemen keuangan personal"       │
│ ❌ "Toko online"                               │
│ ❌ "Bisnis"                                     │
│ ❌ "Produk"                                     │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ 👥 Target Audiens                               │
│                                                  │
│ ✅ "Wanita 25-35 tahun profesional"             │
│ ✅ "Pecinta kopi & coffee enthusiasts"           │
│ ✅ "Entrepreneur muda yang peduli kualitas"     │
│ ❌ "Semua orang"                                │
│ ❌ "Yang butuh produk ini"                      │
│ ❌ "Masyarakat Indonesia"                       │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ 📱 Platform                                     │
│                                                  │
│ 📸 Instagram → Visual, aesthetic, storytelling  │
│ 🎬 TikTok    → Trending, casual, entertaining   │
│ 💬 WhatsApp  → Personal, direct, urgent         │
│ 👥 Facebook  → Community, trust, long-form      │
│ 💼 LinkedIn  → Professional, B2B, expertise     │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ 🖊️ Gaya Bahasa                                 │
│                                                  │
│ 😎 Santai       → Casual, friendly, chill      │
│ 🎯 Profesional  → Expert, credible, formal     │
│ 🔥 Promosi      → Urgent, FOMO, exciting       │
│ 📚 Edukatif     → Tips, how-to, helpful        │
│ 😄 Humoris      → Funny, entertaining, trendy  │
└─────────────────────────────────────────────────┘
```

---

## 🎬 WORKFLOW

```
1. FILL FORM
   ↓
2. CLICK "BUAT KONTEN"
   ↓
3. WAIT FOR LOADING (5-10 detik)
   ↓
4. VIEW RESULTS
   ├─ Hook Tab → 5 catchy openers
   ├─ Caption Tab → 3 caption variants
   └─ CTA Tab → 3 call-to-action options
   ↓
5. COPY WHAT YOU NEED
   ├─ Copy individual items
   └─ Or Copy All at once
   ↓
6. POST TO MEDIA SOSIAL
```

---

## 🎯 OUTPUT STRUCTURE

```
HASIL OUTPUT:
├── 🔥 HOOKS (5 pieces)
│   ├─ Hook 1 [Copy]
│   ├─ Hook 2 [Copy]
│   └─ ... (5 total)
│
├── 📝 CAPTIONS (3 variants)
│   ├─ Super Singkat (1 kalimat) [Copy]
│   ├─ Singkat (1-2 kalimat) [Copy]
│   └─ Normal (3-4 kalimat) [Copy]
│
└── 🎯 CTA (3 pieces)
    ├─ CTA 1 [Copy]
    ├─ CTA 2 [Copy]
    └─ CTA 3 [Copy]

TOTAL = 11+ pieces of ready-to-use content!
```

---

## 💾 COPY OPTIONS

```
Option 1: Copy Individual Item
├─ Hover over card
├─ Click [Copy] button
└─ Paste where needed

Option 2: Copy All Results
├─ Click [Copy Semua Hasil]
├─ Get all content in one go
└─ Paste & organize
```

---

## 🔌 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "Module not found" | `pip install -r requirements.txt` |
| "Invalid API Key" | Check `.env` has correct GROQ_API_KEY |
| "Port 5000 in use" | Change port in `app.py`: `app.run(port=5001)` |
| "Results not showing" | Check browser console (F12) for errors |
| "Slow generation" | Normal (5-10 sec), Groq API can be slow sometimes |

---

## 📊 PRO TIPS

### Tip 1: Specific is Better
```
❌ "Toko"
✅ "Online shop yang jual fashion muslim untuk working mom"
```

### Tip 2: Match Platform with Style
```
Instagram + Santai    ✅ Natural aesthetic
LinkedIn + Promosi    ❌ Wrong combo
TikTok + Humoris      ✅ Trending & fun
```

### Tip 3: A/B Test
```
Generate 2 different styles → Post both
Compare which gets more engagement → Iterate
```

### Tip 4: Save Good Results
```
Generate output → Copy all → Paste in spreadsheet
Track: platform, style, engagement results
```

### Tip 5: Mix & Match
```
Take 1 hook from Hook tab
Combine with Caption Normal
Add 1 CTA = Custom powerful post
```

---

## 🎓 COMMON OUTPUTS

### For Instagram
```
Use: Caption Normal + 1-2 Hooks
Post as: Carousel with images
```

### For TikTok
```
Use: Caption Super Singkat (script) + Hook
Post as: 15-60 second video
```

### For WhatsApp
```
Use: Caption Singkat + CTA
Send as: Direct message or broadcast
```

### For LinkedIn
```
Use: Caption Normal + Professional style
Add: Context about why posting
```

---

## ⌨️ KEYBOARD SHORTCUTS

```
Enter      → Submit form (when focus on input)
Esc        → Close output modal
Tab        → Navigate through form fields
```

---

## 📱 MOBILE TIPS

```
✅ Form fills nicely on small screens
✅ Buttons are touch-friendly (big enough)
✅ Output modal is readable on mobile
✅ Copy works on all devices

💡 Landscape mode shows more content
💡 Pinch to zoom if text too small
```

---

## 🔒 SECURITY NOTES

```
✅ .env file is gitignored (keep API key safe!)
✅ API key only in .env, never in code
✅ Input is validated before sending
✅ Never commit .env to git
```

---

## 📈 SUCCESS METRICS

Track these to measure success:

```
Per Post:
- Likes/Reactions
- Comments
- Shares
- Clicks (if link)
- Conversion (sales/signups)

Per Content Type:
- Which style gets most engagement?
- Which platform performs best?
- Which CTA converts most?
```

---

## 🎁 BONUS HACKS

### Hack 1: Content Batching
```
1. Generate 5 different combinations
2. Schedule all for the week
3. Monitor results
4. Repeat what works
```

### Hack 2: Template Library
```
Save successful prompts:
- Usaha: Coffee Shop
- Audiens: Coffee lovers
- Platform: Instagram
- Gaya: Santai
→ Save for next coffee shop client!
```

### Hack 3: Team Workflow
```
1. Manager: Use app to generate content
2. Designer: Add images
3. Account: Review before posting
4. Scheduler: Post according to calendar
```

---

## 📚 WHERE TO FIND HELP

```
❓ Setup issues?      → README.md
❓ How to use?        → TIPS_AND_TRICKS.md
❓ Technical details? → CHANGELOG.md, IMPROVEMENTS.md
❓ API issues?        → https://console.groq.com
```

---

## ⏱️ TIME ESTIMATES

```
Setup:     5 minutes
Generate:  10 seconds to 1 minute
Copy:      5 seconds
Post:      2 minutes
Total:     ~3 minutes per post!

VS.

Manual copywriting: 30-60 minutes
Result quality:     Good → Better
Consistency:        Random → Predictable
```

---

## 🚀 READY TO START?

```
1. Setup .env with API key
2. pip install -r requirements.txt
3. python app.py
4. Open http://localhost:5000
5. Fill form & generate!
6. Copy & post content
7. Measure results
8. Iterate & improve
```

---

**You got this!** 💪
Start creating viral content now! 🚀
