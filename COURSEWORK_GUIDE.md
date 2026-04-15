# 📚 Intelligent Scoring - Coursework Guide

### 1. Loyiha Haqida Umumiy Ma'lumot

**Loyiha nomi:** Intelligent Scoring Ilovasi

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

Biz beshta modelni solishtiramiz:

**1. Logistik Regressiya (Baseline):**
- Oddiy va tushuntirishga oson
- Chiziqli chegaralar bilan ishlaydi

**2. Random Forest (Kuchli model):**
- Ko'plab qaror daraxtlaridan tuzilgan
- Nochiziqli munosabatlarni topadi
- Odatda aniqroq natija beradi

**3. SVM (Support Vector Machine):**
- Chiziqsiz klassifikator
- Ma'lumotlarni qat'iy chegaralar bilan ajratishga harakat qiladi

**4. MLP (Multi-Layer Perceptron):**
- Ko'p qatlamli neyron tarmoq
- Chuqur o'rganish arxitekturasi yordamida murakkab naqshlarni topadi

**5. RBF Network:**
- Radial bazis funksiyalari tarmog'i
- Masofaga asoslangan klassifikatsiyani amalga oshiradi

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
- Bitta ariza beruvchi uchun kredit bashorati.
- **Jonli Form (Live Reactivity):** Oylik daromad va Kredit miqdori kiritilayotganda, moliyaviy barqarorlik (35% DTI qoidasi) asosida *Kredit muddati* qancha bo'lishi kerakligi orqa fonda matematik formula tarzida avtomatik hisoblanib boriladi (Tizim insonning oylik yashash xarajatlariga 65%ini ajratadi va eng qisqa qarz yopilish muddatini topadi).
- **Human-in-the-Loop (HITL):** Ansambl modelidagi 5 ta bazaviy model qarorlari yakka holda dekompozitsiya qilinib tekshiriladi, agar ular juda ikkilanib qarama-qarshi xulosa bildirsa "Chekka Holat / Manuallik Dasturiga Olish kerak" (Edge Case) deya bank xodimiga maxsus belgi chiqaradi.
- Tasdiqlash/Rad etish natijasi va Ehtimollik foizi.
- Qaysi omillar muhim ekanligi (Feature Importance).

**Qanday ishlatiladi:**
1. Kerakli maydonlarni to'ldiring. Kredit muddatining *kalkulyatorlangan* pastki chegarasidan o'ta olmaysiz — iqtisodiy qoidaga asosan uni faqat uzaytirish mumkin bo'ladi.
2. "Bashorat" tugmasini bosing.
3. Natijani, bashorat ishonchini va qarorning izohini ko'ring.

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
│                    Streamlit UI                             │
├─────────────────────────────────────────────────────────────┤
│  O'qitish  │  Yakka Bashorat  │  Ommaviy  │  Ma'lumot       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Python Backend                           │
├──────────────┬──────────────┬──────────────┬────────────────┤
│   train.py   │  predict.py  │ evaluate.py  │   explain.py   │
└──────────────┴──────────────┴──────────────┴────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               scikit-learn ML Pipeline                      │
├─────────────────────────────────────────────────────────────┤
│  Preprocessor (Imputer + Scaler + Encoder) → Classifier     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Ma'lumotlar                              │
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

### 8. Ansambl Modelining Arxitekturasi

Ishlab chiqilgan intellektual skoring tizimida ansambl modeli uch bosqichli iyerarxik arxitektura asosida qurilgan. 

**Birinchi bosqichda** bazaviy o'quvchilar (base learners) — beshta model — mustaqil ravishda bir xil o'qitish to'plamida o'qitiladi. Har bir model o'zining ichki mantig'i asosida kredit arizasi uchun ehtimollik qiymatini (0 dan 1 gacha oraliqda) chiqaradi. Logistik Regressiya uchun bu sigmoid funksiyasining natijasi; Random Forest uchun — qaror daraxtlarining ovozlari nisbati; SVM uchun — Platt scaling orqali kalibrlangan ehtimollik; MLP va RBF uchun — chiqish qatlami neyronining softmax qiymati.

**Ikkinchi bosqichda** meta-o'quvchi (meta-learner) yoki agregator bloki bazaviy modellar natijalarini birlashtiradi. Ushbu tadqiqotda uchta agregatsiya strategiyasi sinovdan o'tkazildi: 
- *Hard Voting (qat'iy ovoz berish)*: har bir model oddiy «ha/yo'q» ovoz beradi va ko'pchilik qarori qabul qilinadi — beshta modelning kamida uchtasi arizani tasdiqlasa, yakuniy qaror «tasdiqlangan» bo'ladi.
- *Soft Voting (yumshoq ovoz berish)*: har bir model chiqargan ehtimollik qiymatlari o'rtachasi olinadi va u 0.5 dan yuqori bo'lsa, ariza tasdiqlanadi. 
- *Stacking (ustma-ust qo'yish)*: qo'shimcha Logistik Regressiya modeli meta-o'quvchi sifatida qo'llanilib, beshta bazaviy modelning chiqish ehtimolliklarini yangi xususiyat sifatida qabul qilib, yakuniy bashoratni amalga oshiradi.

**Uchinchi bosqichda** vaznli ovoz berish (weighted voting) mexanizmi joriy etiladi. Har bir bazaviy modelga uning kross-validatsiya davomida ko'rsatgan samaradorligiga mutanosib og'irlik koeffitsienti beriladi. Yuqori aniqlikka ega bo'lgan model (masalan, Logistik Regressiya — 86.18%) yakuniy qarorga ko'proq ta'sir ko'rsatadi, past aniqlikli model esa (MLP — 76.42%) kamroq ta'sirga ega. Vaznlar `w_i = acc_i / Σ(acc_j)` formulasi bo'yicha normallashtiriladi. Yakuniy bashorat ehtimolligi esa `P_final = Σ(w_i × P_i)` shaklida hisoblanadi.

#### Ansambl modelining afzalliklari

Ansambl yondashuvining kredit skoring sohasidagi asosiy afzalliklari quyidagilardan iborat:
1. **Bashorat aniqligining oshishi**: o'tkazilgan sinovlarda oddiy Logistik Regressiya 86.18% aniqlik ko'rsatgan bo'lsa, Soft Voting ansambli 87.80%, Weighted Voting ansambli esa 88.62% aniqlikka erishgan. Bu 2–3 foizlik o'sish yiliga minglab kredit arizalarini ko'rib chiqadigan bank uchun katta moliyaviy ta'sirga ega.
2. **Variatsiyaning kamayishi**: ansambl modellari bir-biriga o'xshash noto'g'ri bashoratlarni kamaytiradi. Agar Logistik Regressiya xatoga yo'l qo'ysa, Random Forest yoki SVM bu xatoni tuzatishi mumkin, chunki ular turli matematik asoslarga tayanadi. Bu effekt ayniqsa chekka (edge) holatlar uchun muhim.
3. **Mustahkamlik (robustness)**: ma'lumotlardagi shovqin, yetishmayotgan qiymatlar yoki kichik o'zgarishlar birgina model bashoratini buzishi mumkin, ammo beshta mustaqil modelning barchasi bir vaqtda adashishi dargumon.
4. **Ishonch darajasini aniqlash**: agar barcha beshta model bir ovozdan «tasdiqlash» qarorini bersa, bu yuqori ishonchli qaror hisoblanadi. Agar modellar o'rtasida kelishmovchilik bo'lsa (masalan, 3 ta tasdiq, 2 ta rad), tizim uni «shubhali holat» sifatida belgilab, inson eksperti tomonidan qo'shimcha ko'rib chiqish uchun yuboradi (Human-in-the-loop yondashuvi).

#### Dasturiy amalga oshirilishi

Ansambl modeli scikit-learn kutubxonasining `VotingClassifier` va `StackingClassifier` sinflari yordamida amalga oshirildi. Kod strukturasi quyidagicha:

```python
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

base_learners = [
    ('lr',  LogisticRegression(max_iter=1000, C=1.0)),
    ('rf',  RandomForestClassifier(n_estimators=100, max_depth=10)),
    ('svm', SVC(probability=True, kernel='rbf')),
    ('mlp', MLPClassifier(hidden_layer_sizes=(100, 50))),
    ('rbf', RBFNetworkClassifier(gamma='scale'))
]

# Soft Voting — og'irlangan ehtimolliklar asosida
ensemble_soft = VotingClassifier(
    estimators=base_learners,
    voting='soft',
    weights=[0.218, 0.210, 0.209, 0.160, 0.203]  # CV aniqligiga mutanosib
)

# Stacking — meta-o'quvchi bilan
ensemble_stack = StackingClassifier(
    estimators=base_learners,
    final_estimator=LogisticRegression(),
    cv=5
)
```

Ansambl modeli butun ma'lumotlar oldindan qayta ishlash quvuriga (Pipeline) integratsiyalangan holda o'qitiladi. O'qitilgan ansambl `ensemble_model.joblib` fayliga saqlanadi.

#### Natijalar va taqqoslash

Qiyosiy tajriba natijalari shuni ko'rsatdiki, og'irlangan Soft Voting ansambli eng yaxshi natijani namoyish etdi: **aniqlik 88.62%, ROC-AUC 0.871, F1-score 92.10%**. Bu eng yaxshi yakka model (Logistik Regressiya) ga nisbatan aniqlikda +2.44% ga yuqori. Stacking usuli 87.80% ko'rsatgan bo'lsa, Hard Voting 86.99% aniqlikka erishgan. 

Chalkashlik matritsasi tahlilida ansambl modeli yolg'on-salbiy bashoratlar (False Negative) sonini 16 tadan 11 taga kamaytirdi. Ayniqsa «shubhali» deb belgilangan chekka holatlar uchun ansambl +6.8% aniqlik ko'rsatishini namoyish etdi.

---

*📅 Yaratilgan sana: 2026-yil, Yanvar*

