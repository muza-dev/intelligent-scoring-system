# 🏦 Iste'mol Kreditlari uchun Intellektual Skoring Modeli

Ko'p rollli, to'liq lokalizatsiya qilingan Streamlit veb-ilovasi. Bank xodimlari va administratorlar uchun mashinaviy o'rganish modellari yordamida kredit arizalarini baholash imkonini beradi.

## Asosiy Imkoniyatlar

- **Rol Asosidagi Autentifikatsiya**: `Admin` (o'qitish, foydalanuvchilarni boshqarish, EDA va barcha sahifalar) va `Bank Xodimi` (faqat bashorat sahifalari) rollari uchun alohida kirish huquqlari. PBKDF2-SHA256 parol shifrlash va 10 daqiqalik sessiya timeout bilan himoyalangan.
- **Ko'p Modelli Reestr (Multi-Model Registry)**: 6 ta ML modeli bir vaqtda o'qitiladi va saqlanadi. Admin ular orasida istalgan vaqtda almashishi mumkin: Logistic Regression, Random Forest, SVM, MLP, RBF Network, **EnsembleSoft**.
- **EnsembleSoft**: 5 ta bazaviy modelning CV aniqligiga mutanosib vaznli yumshoq ovoz berish (Weighted Soft Voting) ansambli — `VotingClassifier(voting='soft', weights=[...])`.
- **Yakka va Ommaviy Bashorat**:
  - Bitta ariza uchun ehtimollik, qaror va xususiyat ahamiyati ko'rsatiladi.
  - CSV fayl yuklash orqali yuzlab arizani bir zumda baholash va natijalarni yuklab olish.
- **DTI-ga Asoslangan Dinamik Kredit Muddati**: Ariza beruvchi daromadidan kelib chiqib, 35% DTI qoidasi bo'yicha minimal kredit muddati avtomatik hisoblanadi.
- **Human-in-the-Loop (HITL)**: 5 ta bazaviy model o'zaro qarama-qarshi xulosa bildirsa, tizim avtomatik "Edge Case / Manual Review Required" belgisini qo'yadi.
- **Ma'lumotlar Tahlili (EDA)**: Adminlar uchun dataset taqsimoti, korrelyatsiya va grafik tahlil sahifasi.
- **Xalqarolashtirish (i18n)**: To'liq uch tilli interfeys — O'zbekcha 🇺🇿, Ruscha 🇷🇺, Inglizcha 🇺🇸 (UZS valyuta formati bilan).
- **Mavzular**: Tizim, Qorong'u va Yorug' mavzular — login sahifasida va dashboardda alohida tanlanadi.
- **Foydalanuvchilarni Boshqarish**: Admin bank xodimlarini qo'shishi, ko'rishi va o'chirishi mumkin.

## Texnologiya To'plami

| Qatlam | Texnologiya |
|---|---|
| **Framework** | [Streamlit](https://streamlit.io/) |
| **Machine Learning** | scikit-learn (`Pipeline`, `VotingClassifier`) |
| **Ma'lumotlar** | Pandas, NumPy |
| **Vizualizatsiya** | Matplotlib, Seaborn |
| **Ma'lumotlar Bazasi** | SQLite (`users.db`) |
| **Xavfsizlik** | PBKDF2-SHA256 (hashlib) |
| **Dependency** | `uv` / `pip` (Python >= 3.11) |

## O'rnatish

1. **Repozitoriyani klonlash**

2. **Virtual muhit yaratish**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # yoki Windows: .venv\Scripts\activate
   ```

3. **Kutubxonalarni o'rnatish**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ma'lumotlar to'plamini qo'shish**
   [Kaggle Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset) dan yuklab, `data/raw/` papkasiga joylashtiring.

5. **Ilovani ishga tushirish**
   ```bash
   streamlit run main.py
   ```

## Ishlatish

- **Kirish**: Login sahifasida username va parol kiriting. Admin sukut bo'yicha `admin` / `admin123` bilan kiradi.
- **O'qitish**: Admin sifatida **O'qitish va Metrikalar** sahifasiga o'ting va "Modelni O'qitish" tugmasini bosing — 6 ta model bir vaqtda o'qitiladi.
- **Faol Modelni Almashtirish**: Sidebar'dagi "Active Model" ro'yxatidan istalgan modelni tanlang.
- **Mavzu va Til**: Sidebar (dashboard) yoki login sahifasida o'zgartiriladi.
