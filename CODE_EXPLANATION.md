# Kod Tushuntirish — Himoya uchun

**Loyiha nomi:** Iste'mol Kreditlari uchun Intellektual Skoring Modeli

Ushbu hujjat kodning har bir qismini oddiy so'zlar bilan tushuntiradi. Himoya davomida savollarni javoblash uchun foydalanishingiz mumkin.

---

## 1. Asosiy Ilova (`main.py`)

Bu fayl veb-ilovaning **kirish nuqtasi**. U foydalanuvchi interfeysini (UI) biznes logikasi bilan bog'laydi.

### Import va Sozlash
- `streamlit` — veb-sahifani quruvchi kutubxona.
- `pandas` va `numpy` — ma'lumotlar jadvallari va raqamlar bilan ishlash uchun.
- `src` papkasidan o'zimizning modullar: `train`, `predict`, `evaluate`, `explain`, `eda`, `i18n`, `auth`, `utils`.

### Sahifa Konfiguratsiyasi
- `st.set_page_config(...)` — brauzer yorlig'i sarlavhasi "Iste'mol Kreditlari uchun Intellektual Skoring Modeli", ikonka 🏦, keng (wide) tartib.

### Kesh (Caching)
- `@st.cache_resource` — modelni bir marta yuklab, keyingi har bir bosishda qayta yuklamaslik uchun.
- `get_model(model_key)` — faollashtirilen modelni diskdan yuklaydi.
- `get_cached_evaluation(model_key)` — berilgan model uchun baholash natijalarini keshga oladi.
- `get_cached_feature_importance(model_key)` — xususiyat ahamiyatini keshga oladi.
- `clear_model_cache()` — yangi o'qitishdan so'ng barcha keshni tozalaydi.

### Sidebar Navigatsiya (`render_sidebar()`)
- Til tanlash (UZ / RU / EN) va Mavzu tanlash (💻 / 🌙 / ☀️) — yon panelning yuqori qismida.
- **Rol belgisi**: Admin uchun 🔐 Admin, xodim uchun 🏦 Bank Xodimi.
- **Faol Model ro'yxati**: Admin o'qitilgan 6 ta model orasidan faolini almashtira oladi — tanlanganda kesh tozalanib sahifa yangilanadi.
- **Model holati**: Faol modelning aniqligi sidebar'da ko'rsatiladi.
- **Chiqish tugmasi**: Istalgan vaqtda sessiyani tugatish.

### Sahifalar
| Sahifa | Rol | Tavsif |
|---|---|---|
| Asosiy (Welcome) | Barcha | Rolga mos qisqacha ko'rsatma |
| O'qitish va Metrikalar | Faqat Admin | 6 model o'qitish, metrikalar, CM, ROC, xususiyat ahamiyati |
| Ma'lumotlar Tahlili (EDA) | Faqat Admin | Vizual dataset tahlili |
| Yakka Bashorat | Barcha | Bitta ariza bashorati, HITL, Feature Importance |
| Ommaviy Bashorat | Barcha | CSV yuklash, ko'plab arizalar, natija yuklab olish |
| Foydalanuvchilar | Faqat Admin | Xodim qo'shish, ko'rish, o'chirish |
| Haqida | Faqat Admin | Dataset, modellar, metodologiya |

---

## 2. Autentifikatsiya (`src/auth.py` + `src/security.py` + `src/db.py`)

### Kirish Jarayoni
1. Foydalanuvchi username va parol kiritadi.
2. `get_user(username)` — SQLite `users.db` dan foydalanuvchi topiladi.
3. `verify_password(stored_hash, provided)` — PBKDF2-SHA256 bilan parol tekshiriladi.
4. Muvaffaqiyatli bo'lsa: `role`, `username`, `full_name` session'ga saqlanadi.

### Xavfsizlik
- **PBKDF2-SHA256**: Har bir parol uchun 32-baytli tasodifiy tuz (`os.urandom(32)`) yaratiladi, 100 000 iteratsiya bilan xeshlanadi.
- **Sessiya Timeout**: 10 daqiqa harakatsizlik aniqlansa, sessiya avtomatik tugatiladi va timeout xabari ko'rsatiladi.
- **Noto'g'ri Urinishlar**: `failed_attempts` hisoblagichi har noto'g'ri kirishda oshadi.
- **Admin Himoyasi**: Admin akkaunt o'chirib bo'lmaydi (`DELETE ... WHERE role != 'admin'`).

### Foydalanuvchi Ma'lumotlar Bazasi
SQLite jadval: `id`, `full_name`, `phone_number`, `email`, `username`, `password_hash`, `national_id`, `address`, `monthly_income`, `role`, `created_at`.

---

## 3. Model O'qitish (`src/train.py`)

### `create_models()` — 6 ta Model
```python
models = {
    "LogisticRegression": Pipeline([preprocessor, LogisticRegression(...)]),
    "RandomForest":       Pipeline([preprocessor, RandomForestClassifier(...)]),
    "SVM":                Pipeline([preprocessor, SVC(probability=True, ...)]),
    "MLP":                Pipeline([preprocessor, MLPClassifier(...)]),
    "RBFNetwork":         Pipeline([preprocessor, RBFNetworkClassifier(...)]),
    "EnsembleSoft":       Pipeline([preprocessor, VotingClassifier(
                              estimators=base_learners,
                              voting='soft',
                              weights=[0.218, 0.210, 0.209, 0.160, 0.203]
                          )]),
}
```

Har bir model `Pipeline` ichida — preprocessor avval ishlaydi, so'ngra classifier.

### `select_best_model()` — 5-Fold Cross-Validation
- Ma'lumotlar 5 qismga bo'linadi.
- Har bir qism navbatma-navbat test sifatida ishlatiladi.
- O'rtacha aniqlik bo'yicha g'olib tanlanadi.

### `train_model()` — Barcha Modellarni O'qitish
1. Barcha 6 ta model CV orqali baholanadi.
2. Barcha 6 ta model to'liq o'qitish to'plamida fit qilinadi.
3. Har biri `models/` papkasiga alohida `.joblib` fayliga saqlanadi.
4. `registry.json` yangilanadi — barcha modellar metadatasi va faol model kaliti.

---

## 4. Bashorat Moduli (`src/predict.py`)

### `load_model(model_key)`
- `registry.json` dan faol model kalitini oladi.
- `config.MODEL_PATHS[key]` bo'yicha `.joblib` faylni yuklaydi.

### `predict_single(input_data, model)`
- Foydalanuvchi kiritgan ma'lumotlarni DataFrame'ga aylantiradi.
- `model.predict()` → 1 (Tasdiqlangan) yoki 0 (Rad etilgan).
- `model.predict_proba()` → ehtimollik (masalan 0.87).
- **HITL Logikasi**: `VotingClassifier` bo'lsa, 5 ta bazaviy model yakka bashoratlarini solishtiradi. Agar kelishmovchilik bo'lsa → "Edge Case / Manual Review Required".

### `predict_batch(df, model)`
- CSV fayl ma'lumotlarini to'liq baholaydi.
- `Prediction`, `Probability`, `Status`, `Confidence Level` ustunlarini qo'shadi.
- Natija DataFrame qayta yuklab olinadi.

---

## 5. Baholash (`src/evaluate.py`)

- **Metrikalar**: Accuracy, Precision, Recall, F1-Score, ROC-AUC.
- **Chalkashlik Matritsasi**: Seaborn Heatmap — TP, TN, FP, FN.
- **ROC Egri Chizig'i**: AUC qiymati bilan.
- Barcha hisob-kitoblar test to'plamida amalga oshiriladi (ma'lumotlar oqishi yo'q).

---

## 6. Xususiyat Ahamiyati (`src/explain.py`)

- `get_aggregated_feature_importance(model)` — turli model turlariga mos usulda xususiyat ahamiyatini chiqaradi:
  - **Random Forest / Ensemble**: `feature_importances_`
  - **Logistic Regression**: `|coef_|`
  - **SVM**: kernel asosida
- `plot_feature_importance(df, top_n)` — gorizontal bar chart.

---

## 7. Ma'lumotlar Reestrı (`models/registry.json`)

```json
{
  "active": "EnsembleSoft",
  "models": {
    "LogisticRegression": { "test_accuracy": 0.8618, ... },
    "RandomForest":       { "test_accuracy": 0.8130, ... },
    "SVM":                { "test_accuracy": 0.8537, ... },
    "MLP":                { "test_accuracy": 0.7967, ... },
    "RBFNetwork":         { "test_accuracy": 0.8618, ... },
    "EnsembleSoft":       { "test_accuracy": 0.8618, ... }
  }
}
```

Admin sidebar'dan faol modelni almashtirganda bu fayl yangilanadi.

---

## 8. Xalqarolashtirish (`src/i18n.py`)

- `TRANSLATIONS` — ulkan lug'at. Kalit → `{"UZ": "...", "RU": "...", "EN": "..."}`.
- `t(key, lang)` — qisqa yordamchi funksiya. Misol: `t("approved", "UZ")` → `"Tasdiqlandi"`.
- 1200+ qator, barcha UI matnlari uch tilda.

---

## 9. Konfiguratsiya (`src/config.py`)

- Model fayl yo'llari (`MODEL_PATHS`), dataset yo'llari, xususiyat ro'yxatlari.
- `ENSEMBLE_SOFT_WEIGHTS = [0.218, 0.210, 0.209, 0.160, 0.203]` — CV aniqligiga mutanosib vaznlar.
- `CV_FOLDS = 5`, `TEST_SIZE = 0.2`, `RANDOM_STATE = 42`.
