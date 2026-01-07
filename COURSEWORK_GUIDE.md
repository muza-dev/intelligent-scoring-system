# 📚 Loan Approval Prediction - Coursework Guide

### 1. Loyiha Haqida Umumiy Ma'lumot

**Loyiha nomi:** Kredit Tasdiqlash Bashorati Ilovasi

**Maqsad:** Bu kurs ishi mashinaviy o'rganish (Machine Learning) yordamida bank kredit arizalarini avtomatik tasdiqlash yoki rad etish bashoratini amalga oshiruvchi to'liq web-ilova yaratishga bag'ishlangan.

**Muammo:** Banklar kuniga minglab kredit arizalarini ko'rib chiqadi. Qo'lda ko'rib chiqish:
- Vaqt talab qiladi
- Xatolarga moyil
- Bir xil bo'lmagan qarorlar

**Yechim:** Mashinaviy o'rganish modeli tarixiy ma'lumotlardan o'rganib, yangi arizalarni avtomatik baholaydi.

---

### 2. Mashinaviy O'rganish Qanday Ishlaydi?

#### 2.1 Ma'lumotlar To'plami (Dataset)
Biz Kaggle platformasidan "Loan Prediction Dataset" ni ishlatdik. Bu to'plamda ~600 ta kredit arizasi mavjud.

**Kirish xususiyatlari (Features):**
| Xususiyat | Tavsifi |
|-----------|---------|
| Jinsi (Gender) | Erkak / Ayol |
| Oilali (Married) | Ha / Yo'q |
| Qaramog'idagilar (Dependents) | Oila a'zolari soni |
| Ta'lim (Education) | Oliy ma'lumotli / Yo'q |
| O'z-o'ziga ish beruvchi (Self_Employed) | Ha / Yo'q |
| Ariza beruvchi daromadi (ApplicantIncome) | Oylik daromad |
| Qo'shma ariza beruvchi daromadi (CoapplicantIncome) | Hamkor daromadi |
| Kredit miqdori (LoanAmount) | So'ralgan kredit |
| Kredit muddati (Loan_Amount_Term) | Oylar |
| Kredit tarixi (Credit_History) | Yaxshi (1) / Yomon (0) |
| Mulk hududi (Property_Area) | Shahar / Qishloq / Shahar atrofi |

**Chiqish (Target):** Kredit holati (Loan_Status) - Tasdiqlangan (Y) / Rad etilgan (N)

#### 2.2 Oldindan Qayta Ishlash (Preprocessing)

**1. Yetishmayotgan qiymatlarni to'ldirish (Imputation):**
- Raqamli ustunlar → Median (o'rtacha qiymat)
- Kategorik ustunlar → Eng ko'p uchraydigan qiymat (Mode)

**2. Xususiyatlarni kodlash (Encoding):**
- Kategorik xususiyatlar One-Hot Encoding bilan raqamlarga aylantiriladi
- Masalan: Jinsi = [Erkak, Ayol] → [1,0] yoki [0,1]

**3. Masshtablash (Scaling):**
- Raqamli xususiyatlar StandardScaler bilan normallashtiriladi
- Bu modelning yaxshi ishlashiga yordam beradi

#### 2.3 Model Tanlash

Biz ikkita modelni solishtiramiz:

**1. Logistik Regressiya (Baseline):**
- Oddiy va tushuntirishga oson
- Chiziqli chegaralar bilan ishlaydi

**2. Random Forest (Kuchli model):**
- Ko'plab qaror daraxtlaridan tuzilgan
- Nochiziqli munosabatlarni topadi
- Odatda aniqroq natija beradi

**Tanlash usuli:** 5-fold Cross-Validation
- Ma'lumotlar 5 qismga bo'linadi
- Har bir qism navbatma-navbat test sifatida ishlatiladi
- O'rtacha aniqlik bo'yicha eng yaxshi model tanlanadi

#### 2.4 Baholash Metrikalari

| Metrika | Tavsifi |
|---------|---------|
| **Accuracy (Aniqlik)** | Umumiy to'g'ri bashoratlar foizi |
| **Precision** | Tasdiqlangan deb bashorat qilinganlardan qanchasi haqiqatda tasdiqlangan |
| **Recall** | Haqiqatda tasdiqlangalardan qanchasi to'g'ri topilgan |
| **F1-Score** | Precision va Recall o'rtasidagi muvozanat |
| **ROC-AUC** | Modelning farqlash qobiliyati (0.5 = tasodifiy, 1.0 = mukammal) |

#### 2.5 Chalkashlik Matritsasi (Confusion Matrix)

```
                    Bashorat
                 Rad     Tasdiqlangan
Haqiqiy  Rad      TN          FP
         Tasdiqlangan  FN          TP
```

- **TN (True Negative):** To'g'ri rad etilgan
- **FP (False Positive):** Noto'g'ri tasdiqlangan
- **FN (False Negative):** Noto'g'ri rad etilgan
- **TP (True Positive):** To'g'ri tasdiqlangan

---

### 3. Ilova Sahifalari

#### 3.1 O'qitish va Metrikalar (Train & Metrics)

**Vazifasi:**
- Modelni o'qitish tugmasi
- Cross-validation natijalari
- Baholash metrikalari (Accuracy, Precision, Recall, F1, ROC-AUC)
- Chalkashlik matritsasi grafigi
- ROC egri chizig'i grafigi
- Xususiyat ahamiyati grafigi

**Qanday ishlatiladi:**
1. "Modelni O'qitish" tugmasini bosing
2. Model o'qitiladi va saqlanadi
3. Natijalar avtomatik ko'rsatiladi

#### 3.2 Yakka Bashorat (Single Prediction)

**Vazifasi:**
- Bitta ariza beruvchi uchun kredit bashorati
- Forma orqali ma'lumotlarni kiritish
- Tasdiqlash/Rad etish natijasi
- Ehtimollik foizi
- Qaysi omillar muhim ekanligi

**Qanday ishlatiladi:**
1. Barcha maydonlarni to'ldiring
2. "Bashorat" tugmasini bosing
3. Natijani va tushuntirishni ko'ring

#### 3.3 Ommaviy Bashorat (Batch Prediction)

**Vazifasi:**
- CSV fayl yuklash
- Bir nechta arizalarni bir vaqtda baholash
- Natijalarni CSV formatida yuklab olish

**Qanday ishlatiladi:**
1. Namuna CSV ni yuklab oling
2. O'z ma'lumotlaringizni kiriting
3. Faylni yuklang
4. Natijalarni yuklab oling

#### 3.4 Ma'lumot (About)

**Vazifasi:**
- Loyiha haqida umumiy ma'lumot
- Ma'lumotlar to'plami tavsifi
- Model tushuntirishi
- Cheklovlar va axloqiy masalalar

---

### 4. Texnik Arxitektura

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit UI                              │
├─────────────────────────────────────────────────────────────┤
│  O'qitish  │  Yakka Bashorat  │  Ommaviy  │  Ma'lumot      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Python Backend                            │
├──────────────┬──────────────┬──────────────┬────────────────┤
│   train.py   │  predict.py  │ evaluate.py  │   explain.py   │
└──────────────┴──────────────┴──────────────┴────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               scikit-learn ML Pipeline                       │
├─────────────────────────────────────────────────────────────┤
│  Preprocessor (Imputer + Scaler + Encoder) → Classifier    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Ma'lumotlar                               │
├─────────────────────────────────────────────────────────────┤
│  train.csv (Kaggle)  │  loan_model.joblib  │  metadata.json │
└─────────────────────────────────────────────────────────────┘
```

---

### 5. Xususiyat Ahamiyati

Model qaror qabul qilishda quyidagi xususiyatlarga e'tibor beradi:

1. **Kredit Tarixi (Credit_History)** - ~30-40% ahamiyat
   - Eng muhim omil
   - Oldingi kreditlarni to'lagan bo'lsa, yangi kredit tasdiqlanishi ehtimoli yuqori

2. **Umumiy Daromad** - ~20-25% ahamiyat
   - Ariza beruvchi + Hamkor daromadi

3. **Kredit Miqdori** - ~15-20% ahamiyat
   - Kichik kredit = yuqori tasdiqlash ehtimoli

4. **Mulk Hududi** - ~10% ahamiyat
   - Shahar yoki shahar atrofi = biroz yuqori ehtimol

---

### 6. Cheklovlar va Kelajak Yaxshilashlar

**Joriy cheklovlar:**
- Ma'lumotlar to'plami kichik (~600 ta)
- Faqat asosiy xususiyatlar mavjud
- Vaqt bo'yicha validatsiya yo'q

**Kelajakda qo'shilishi mumkin:**
- Kredit bali (Credit Score)
- Ish tarixi
- Bank balansi
- Chuqurroq o'rganish modellari

---

### 7. Axloqiy Masalalar

⚠️ **Muhim eslatma:** Bu kurs ishi namoyishi, haqiqiy bankda ishlatish uchun emas!

- **Adolatlilik:** Model tarixiy ma'lumotlardagi noxolisliklarni o'rganishi mumkin
- **Shaffoflik:** Qarorlar tushuntirilishi kerak
- **Inson nazorati:** Model maslahat beradi, oxirgi qaror insonda

---

*📅 Yaratilgan sana: 2026-yil, Yanvar*

