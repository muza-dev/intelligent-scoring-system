"""
Internationalization (i18n) module for the Loan Approval Prediction application.
Supports: English (EN), Uzbek (UZ), Russian (RU)
"""

# Available languages
LANGUAGES = {
    "EN": "English",
    "UZ": "O'zbek",
    "RU": "Русский",
}

DEFAULT_LANGUAGE = "UZ"

# Translation dictionary
TRANSLATIONS = {
    # ==========================================================================
    # Navigation & Common
    # ==========================================================================
    "app_title": {
        "EN": "🏦 Loan Approval",
        "UZ": "🏦 Kredit Tasdiqlash",
        "RU": "🏦 Одобрение Кредита",
    },
    "nav_train": {
        "EN": "Train & Metrics",
        "UZ": "O'qitish va Metrikalar",
        "RU": "Обучение и Метрики",
    },
    "nav_single": {
        "EN": "Single Prediction",
        "UZ": "Yakka Bashorat",
        "RU": "Единичный Прогноз",
    },
    "nav_batch": {
        "EN": "Batch Prediction",
        "UZ": "Ommaviy Bashorat",
        "RU": "Пакетный Прогноз",
    },
    "nav_about": {
        "EN": "About",
        "UZ": "Ma'lumot",
        "RU": "О Программе",
    },
    "language": {
        "EN": "Language",
        "UZ": "Til",
        "RU": "Язык",
    },
    "model_trained": {
        "EN": "✓ Model trained",
        "UZ": "✓ Model o'qitilgan",
        "RU": "✓ Модель обучена",
    },
    "no_model": {
        "EN": "⚠ No trained model",
        "UZ": "⚠ O'qitilgan model yo'q",
        "RU": "⚠ Модель не обучена",
    },
    "go_to_training": {
        "EN": "Go to 'Train & Metrics' to train",
        "UZ": "'O'qitish va Metrikalar' ga o'ting",
        "RU": "Перейдите в 'Обучение и Метрики'",
    },
    "model": {
        "EN": "Model",
        "UZ": "Model",
        "RU": "Модель",
    },
    "accuracy": {
        "EN": "Accuracy",
        "UZ": "Aniqlik",
        "RU": "Точность",
    },
    
    # ==========================================================================
    # Train & Metrics Page
    # ==========================================================================
    "train_title": {
        "EN": "📊 Train & Metrics",
        "UZ": "📊 O'qitish va Metrikalar",
        "RU": "📊 Обучение и Метрики",
    },
    "data_not_found": {
        "EN": "⚠️ Training data not found!",
        "UZ": "⚠️ O'qitish ma'lumotlari topilmadi!",
        "RU": "⚠️ Данные для обучения не найдены!",
    },
    "download_prompt": {
        "EN": "Please download `train.csv` from Kaggle and place it in:",
        "UZ": "Iltimos, Kaggle'dan `train.csv` ni yuklab, quyidagi joyga qo'ying:",
        "RU": "Пожалуйста, скачайте `train.csv` с Kaggle и поместите в:",
    },
    "download_link": {
        "EN": "📥 Download from: ",
        "UZ": "📥 Yuklab olish: ",
        "RU": "📥 Скачать с: ",
    },
    "model_training": {
        "EN": "🎯 Model Training",
        "UZ": "🎯 Modelni O'qitish",
        "RU": "🎯 Обучение Модели",
    },
    "train_button": {
        "EN": "🚀 Train Model",
        "UZ": "🚀 Modelni O'qitish",
        "RU": "🚀 Обучить Модель",
    },
    "training_progress": {
        "EN": "Training model... This may take a minute.",
        "UZ": "Model o'qitilmoqda... Bir oz vaqt olishi mumkin.",
        "RU": "Обучение модели... Это может занять минуту.",
    },
    "training_success": {
        "EN": "✓ Model trained successfully!",
        "UZ": "✓ Model muvaffaqiyatli o'qitildi!",
        "RU": "✓ Модель успешно обучена!",
    },
    "training_failed": {
        "EN": "Training failed: ",
        "UZ": "O'qitish muvaffaqiyatsiz: ",
        "RU": "Ошибка обучения: ",
    },
    "model_type": {
        "EN": "Model Type",
        "UZ": "Model Turi",
        "RU": "Тип Модели",
    },
    "test_accuracy": {
        "EN": "Test Accuracy",
        "UZ": "Test Aniqligi",
        "RU": "Точность Теста",
    },
    "train_prompt": {
        "EN": "👆 Train a model to see metrics and evaluation results.",
        "UZ": "👆 Metrikalar va baholash natijalarini ko'rish uchun modelni o'qiting.",
        "RU": "👆 Обучите модель, чтобы увидеть метрики.",
    },
    "evaluation_results": {
        "EN": "📈 Evaluation Results",
        "UZ": "📈 Baholash Natijalari",
        "RU": "📈 Результаты Оценки",
    },
    "evaluating": {
        "EN": "Evaluating model...",
        "UZ": "Model baholanmoqda...",
        "RU": "Оценка модели...",
    },
    "precision": {
        "EN": "Precision",
        "UZ": "Aniqlik",
        "RU": "Точность",
    },
    "recall": {
        "EN": "Recall",
        "UZ": "Qaytaruvchanlik",
        "RU": "Полнота",
    },
    "f1_score": {
        "EN": "F1 Score",
        "UZ": "F1 Ko'rsatkichi",
        "RU": "F1 Мера",
    },
    "roc_auc": {
        "EN": "ROC-AUC",
        "UZ": "ROC-AUC",
        "RU": "ROC-AUC",
    },
    "confusion_matrix": {
        "EN": "Confusion Matrix",
        "UZ": "Chalkashlik Matritsasi",
        "RU": "Матрица Ошибок",
    },
    "roc_curve": {
        "EN": "ROC Curve",
        "UZ": "ROC Egri Chizig'i",
        "RU": "ROC Кривая",
    },
    "feature_importance": {
        "EN": "🔍 Feature Importance",
        "UZ": "🔍 Xususiyat Ahamiyati",
        "RU": "🔍 Важность Признаков",
    },
    "evaluation_failed": {
        "EN": "Evaluation failed: ",
        "UZ": "Baholash muvaffaqiyatsiz: ",
        "RU": "Ошибка оценки: ",
    },
    
    # ==========================================================================
    # Single Prediction Page
    # ==========================================================================
    "prediction_title": {
        "EN": "🔮 Single Prediction",
        "UZ": "🔮 Yakka Bashorat",
        "RU": "🔮 Единичный Прогноз",
    },
    "no_model_warning": {
        "EN": "⚠️ No trained model found. Please train a model first.",
        "UZ": "⚠️ O'qitilgan model topilmadi. Avval modelni o'qiting.",
        "RU": "⚠️ Модель не найдена. Сначала обучите модель.",
    },
    "enter_details": {
        "EN": "Enter applicant details to predict loan approval.",
        "UZ": "Kredit tasdiqlashini bashorat qilish uchun ariza beruvchi ma'lumotlarini kiriting.",
        "RU": "Введите данные заявителя для прогноза одобрения кредита.",
    },
    "applicant_info": {
        "EN": "📝 Applicant Information",
        "UZ": "📝 Ariza Beruvchi Ma'lumotlari",
        "RU": "📝 Информация о Заявителе",
    },
    "gender": {
        "EN": "Gender",
        "UZ": "Jinsi",
        "RU": "Пол",
    },
    "gender_male": {
        "EN": "Male",
        "UZ": "Erkak",
        "RU": "Мужской",
    },
    "gender_female": {
        "EN": "Female",
        "UZ": "Ayol",
        "RU": "Женский",
    },
    "married": {
        "EN": "Married",
        "UZ": "Oilali",
        "RU": "Женат/Замужем",
    },
    "yes": {
        "EN": "Yes",
        "UZ": "Ha",
        "RU": "Да",
    },
    "no": {
        "EN": "No",
        "UZ": "Yo'q",
        "RU": "Нет",
    },
    "dependents": {
        "EN": "Dependents",
        "UZ": "Qaramog'idagilar",
        "RU": "Иждивенцы",
    },
    "education": {
        "EN": "Education",
        "UZ": "Ta'lim",
        "RU": "Образование",
    },
    "graduate": {
        "EN": "Graduate",
        "UZ": "Oliy ma'lumotli",
        "RU": "Высшее",
    },
    "not_graduate": {
        "EN": "Not Graduate",
        "UZ": "Oliy ma'lumotsiz",
        "RU": "Без высшего",
    },
    "self_employed": {
        "EN": "Self Employed",
        "UZ": "O'z-o'ziga ish beruvchi",
        "RU": "Самозанятый",
    },
    "property_area": {
        "EN": "Property Area",
        "UZ": "Mulk Hududi",
        "RU": "Район Недвижимости",
    },
    "urban": {
        "EN": "Urban",
        "UZ": "Shahar",
        "RU": "Городской",
    },
    "rural": {
        "EN": "Rural",
        "UZ": "Qishloq",
        "RU": "Сельский",
    },
    "semiurban": {
        "EN": "Semiurban",
        "UZ": "Shahar atrofi",
        "RU": "Пригород",
    },
    "credit_history": {
        "EN": "Credit History",
        "UZ": "Kredit Tarixi",
        "RU": "Кредитная История",
    },
    "credit_good": {
        "EN": "Good (1)",
        "UZ": "Yaxshi (1)",
        "RU": "Хорошая (1)",
    },
    "credit_bad": {
        "EN": "Bad (0)",
        "UZ": "Yomon (0)",
        "RU": "Плохая (0)",
    },
    "applicant_income": {
        "EN": "Applicant Income ($)",
        "UZ": "Ariza Beruvchi Daromadi ($)",
        "RU": "Доход Заявителя ($)",
    },
    "coapplicant_income": {
        "EN": "Coapplicant Income ($)",
        "UZ": "Qo'shma Ariza Beruvchi Daromadi ($)",
        "RU": "Доход Созаявителя ($)",
    },
    "loan_amount": {
        "EN": "Loan Amount (in thousands)",
        "UZ": "Kredit Miqdori (minglab)",
        "RU": "Сумма Кредита (в тысячах)",
    },
    "loan_term": {
        "EN": "Loan Term (months)",
        "UZ": "Kredit Muddati (oylar)",
        "RU": "Срок Кредита (месяцы)",
    },
    "predict_button": {
        "EN": "🔍 Predict",
        "UZ": "🔍 Bashorat",
        "RU": "🔍 Прогноз",
    },
    "prediction_result": {
        "EN": "📋 Prediction Result",
        "UZ": "📋 Bashorat Natijasi",
        "RU": "📋 Результат Прогноза",
    },
    "approved": {
        "EN": "Approved",
        "UZ": "Tasdiqlandi",
        "RU": "Одобрено",
    },
    "rejected": {
        "EN": "Rejected",
        "UZ": "Rad etildi",
        "RU": "Отклонено",
    },
    "approval_probability": {
        "EN": "Approval Probability",
        "UZ": "Tasdiqlash Ehtimoli",
        "RU": "Вероятность Одобрения",
    },
    "probability_note": {
        "EN": "Higher probability indicates higher likelihood of approval.",
        "UZ": "Yuqori ehtimollik tasdiqlash imkoniyati yuqoriligini ko'rsatadi.",
        "RU": "Более высокая вероятность означает большую вероятность одобрения.",
    },
    "input_summary": {
        "EN": "Input Summary:",
        "UZ": "Kiritilgan Ma'lumotlar:",
        "RU": "Введённые Данные:",
    },
    "value": {
        "EN": "Value",
        "UZ": "Qiymat",
        "RU": "Значение",
    },
    "factors_title": {
        "EN": "🔍 What Factors Mattered Most?",
        "UZ": "🔍 Qaysi Omillar Eng Muhim?",
        "RU": "🔍 Какие Факторы Важнее?",
    },
    "factors_note": {
        "EN": "This chart shows which features are generally most important in the model's decision-making process.",
        "UZ": "Bu grafik modelning qaror qabul qilish jarayonida qaysi xususiyatlar eng muhim ekanligini ko'rsatadi.",
        "RU": "Эта диаграмма показывает, какие признаки наиболее важны в процессе принятия решений модели.",
    },
    "prediction_failed": {
        "EN": "Prediction failed: ",
        "UZ": "Bashorat muvaffaqiyatsiz: ",
        "RU": "Ошибка прогноза: ",
    },
    
    # ==========================================================================
    # Batch Prediction Page
    # ==========================================================================
    "batch_title": {
        "EN": "📁 Batch Prediction",
        "UZ": "📁 Ommaviy Bashorat",
        "RU": "📁 Пакетный Прогноз",
    },
    "batch_description": {
        "EN": "Upload a CSV file with applicant data to get batch predictions.",
        "UZ": "Ommaviy bashoratlar olish uchun ariza beruvchilar ma'lumotlari bilan CSV fayl yuklang.",
        "RU": "Загрузите CSV файл с данными заявителей для пакетного прогноза.",
    },
    "expected_format": {
        "EN": "📋 Expected CSV Format",
        "UZ": "📋 Kutilgan CSV Formati",
        "RU": "📋 Ожидаемый Формат CSV",
    },
    "columns_info": {
        "EN": "Your CSV should contain the following columns:",
        "UZ": "CSV faylingiz quyidagi ustunlarni o'z ichiga olishi kerak:",
        "RU": "Ваш CSV должен содержать следующие столбцы:",
    },
    "numeric_cols": {
        "EN": "Numeric",
        "UZ": "Raqamli",
        "RU": "Числовые",
    },
    "categorical_cols": {
        "EN": "Categorical",
        "UZ": "Kategorik",
        "RU": "Категориальные",
    },
    "sample_data": {
        "EN": "Sample data:",
        "UZ": "Namuna ma'lumotlari:",
        "RU": "Пример данных:",
    },
    "download_sample": {
        "EN": "📥 Download Sample CSV",
        "UZ": "📥 Namuna CSV ni Yuklash",
        "RU": "📥 Скачать Пример CSV",
    },
    "upload_csv": {
        "EN": "Upload CSV file",
        "UZ": "CSV fayl yuklash",
        "RU": "Загрузить CSV файл",
    },
    "upload_help": {
        "EN": "Upload a CSV file with applicant information",
        "UZ": "Ariza beruvchi ma'lumotlari bilan CSV fayl yuklang",
        "RU": "Загрузите CSV файл с информацией о заявителях",
    },
    "uploaded_preview": {
        "EN": "📊 Uploaded Data Preview",
        "UZ": "📊 Yuklangan Ma'lumotlar Ko'rinishi",
        "RU": "📊 Предпросмотр Загруженных Данных",
    },
    "total_rows": {
        "EN": "Total rows",
        "UZ": "Jami qatorlar",
        "RU": "Всего строк",
    },
    "missing_columns": {
        "EN": "⚠️ Missing required columns: ",
        "UZ": "⚠️ Etishmayotgan kerakli ustunlar: ",
        "RU": "⚠️ Отсутствуют обязательные столбцы: ",
    },
    "generate_predictions": {
        "EN": "🔍 Generate Predictions",
        "UZ": "🔍 Bashoratlarni Yaratish",
        "RU": "🔍 Сгенерировать Прогнозы",
    },
    "generating": {
        "EN": "Generating predictions...",
        "UZ": "Bashoratlar yaratilmoqda...",
        "RU": "Генерация прогнозов...",
    },
    "predictions_complete": {
        "EN": "✓ Predictions generated for {count} rows!",
        "UZ": "✓ {count} qator uchun bashoratlar yaratildi!",
        "RU": "✓ Прогнозы сгенерированы для {count} строк!",
    },
    "results_summary": {
        "EN": "📈 Results Summary",
        "UZ": "📈 Natijalar Qisqacha",
        "RU": "📈 Сводка Результатов",
    },
    "total_applications": {
        "EN": "Total Applications",
        "UZ": "Jami Arizalar",
        "RU": "Всего Заявок",
    },
    "average_probability": {
        "EN": "Average Probability",
        "UZ": "O'rtacha Ehtimollik",
        "RU": "Средняя Вероятность",
    },
    "predictions_header": {
        "EN": "📋 Predictions",
        "UZ": "📋 Bashoratlar",
        "RU": "📋 Прогнозы",
    },
    "download_predictions": {
        "EN": "📥 Download Predictions CSV",
        "UZ": "📥 Bashoratlar CSV ni Yuklash",
        "RU": "📥 Скачать CSV с Прогнозами",
    },
    "batch_error": {
        "EN": "Error processing file: ",
        "UZ": "Faylni qayta ishlashda xatolik: ",
        "RU": "Ошибка обработки файла: ",
    },
    
    # ==========================================================================
    # About Page
    # ==========================================================================
    "about_title": {
        "EN": "ℹ️ About",
        "UZ": "ℹ️ Ma'lumot",
        "RU": "ℹ️ О Программе",
    },
    "about_description": {
        "EN": "This application uses machine learning to predict whether a loan application will be approved based on applicant characteristics.",
        "UZ": "Bu ilova ariza beruvchi xususiyatlariga asoslanib kredit arizasi tasdiqlanishini bashorat qilish uchun mashinaviy o'rganishdan foydalanadi.",
        "RU": "Это приложение использует машинное обучение для прогнозирования одобрения кредитной заявки на основе характеристик заявителя.",
    },
    "dataset_title": {
        "EN": "Dataset",
        "UZ": "Ma'lumotlar To'plami",
        "RU": "Набор Данных",
    },
    "dataset_source": {
        "EN": "The model is trained on the Kaggle Loan Prediction Dataset",
        "UZ": "Model Kaggle Kredit Bashorat ma'lumotlar to'plamida o'qitilgan",
        "RU": "Модель обучена на наборе данных Kaggle Loan Prediction",
    },
    "feature": {
        "EN": "Feature",
        "UZ": "Xususiyat",
        "RU": "Признак",
    },
    "description": {
        "EN": "Description",
        "UZ": "Tavsif",
        "RU": "Описание",
    },
    "model_section": {
        "EN": "Model",
        "UZ": "Model",
        "RU": "Модель",
    },
    "models_compared": {
        "EN": "The application compares two models:",
        "UZ": "Ilova ikki modelni solishtiradi:",
        "RU": "Приложение сравнивает две модели:",
    },
    "baseline": {
        "EN": "baseline",
        "UZ": "asosiy",
        "RU": "базовая",
    },
    "strong": {
        "EN": "strong",
        "UZ": "kuchli",
        "RU": "сильная",
    },
    "cv_selection": {
        "EN": "The best model is selected automatically via 5-fold cross-validation.",
        "UZ": "Eng yaxshi model 5-fold cross-validation orqali avtomatik tanlanadi.",
        "RU": "Лучшая модель выбирается автоматически с помощью 5-кратной перекрёстной проверки.",
    },
    "preprocessing_title": {
        "EN": "Preprocessing",
        "UZ": "Oldindan Qayta Ishlash",
        "RU": "Предобработка",
    },
    "preprocessing_numeric": {
        "EN": "Numeric features: Missing values imputed with median, then standardized",
        "UZ": "Raqamli xususiyatlar: Etishmayotgan qiymatlar median bilan to'ldiriladi, keyin standartlashtiriladi",
        "RU": "Числовые признаки: Пропущенные значения заполняются медианой, затем стандартизируются",
    },
    "preprocessing_categorical": {
        "EN": "Categorical features: Missing values imputed with most frequent, then one-hot encoded",
        "UZ": "Kategorik xususiyatlar: Etishmayotgan qiymatlar eng ko'p uchraydigan qiymat bilan to'ldiriladi, keyin one-hot kodlanadi",
        "RU": "Категориальные признаки: Пропущенные значения заполняются наиболее частым значением, затем one-hot кодируются",
    },
    "preprocessing_note": {
        "EN": "All preprocessing is done inside a sklearn Pipeline to prevent data leakage",
        "UZ": "Barcha oldindan qayta ishlash ma'lumotlar oqishini oldini olish uchun sklearn Pipeline ichida amalga oshiriladi",
        "RU": "Вся предобработка выполняется внутри Pipeline sklearn для предотвращения утечки данных",
    },
    "limitations_title": {
        "EN": "⚠️ Limitations",
        "UZ": "⚠️ Cheklovlar",
        "RU": "⚠️ Ограничения",
    },
    "limitation_size": {
        "EN": "Small dataset: ~600 samples is limited for production ML",
        "UZ": "Kichik ma'lumotlar to'plami: ~600 namuna ishlab chiqarish ML uchun cheklangan",
        "RU": "Маленький набор данных: ~600 примеров недостаточно для продакшн ML",
    },
    "limitation_imbalance": {
        "EN": "Class imbalance: More approvals than rejections in the data",
        "UZ": "Sinf muvozanatsizligi: Ma'lumotlarda rad etilganlarga qaraganda ko'proq tasdiqlar",
        "RU": "Дисбаланс классов: В данных больше одобрений, чем отказов",
    },
    "limitation_features": {
        "EN": "Missing features: Real-world would include credit score, employment history",
        "UZ": "Etishmayotgan xususiyatlar: Haqiqiy dunyoda kredit bali, ish tarixi kiritiladi",
        "RU": "Отсутствующие признаки: В реальности нужны кредитный рейтинг, история занятости",
    },
    "limitation_temporal": {
        "EN": "No temporal validation: No time-based train/test split",
        "UZ": "Vaqtga asoslangan tekshiruv yo'q: Vaqtga asoslangan train/test bo'linishi yo'q",
        "RU": "Нет временной валидации: Нет разделения train/test по времени",
    },
    "ethics_title": {
        "EN": "🔒 Ethical Considerations",
        "UZ": "🔒 Axloqiy Masalalar",
        "RU": "🔒 Этические Соображения",
    },
    "ethics_warning": {
        "EN": "⚠️ This is a coursework demonstration, NOT for production use.",
        "UZ": "⚠️ Bu kurs ishi namoyishi, ishlab chiqarish uchun EMAS.",
        "RU": "⚠️ Это демонстрация для курсовой работы, НЕ для продакшн использования.",
    },
    "ethics_fairness": {
        "EN": "Fairness: ML models may learn biases present in historical data",
        "UZ": "Adolatlilik: ML modellari tarixiy ma'lumotlardagi noto'g'ri yondashuvlarni o'rganishi mumkin",
        "RU": "Справедливость: ML модели могут перенимать предубеждения из исторических данных",
    },
    "ethics_transparency": {
        "EN": "Transparency: Important to explain predictions to applicants",
        "UZ": "Shaffoflik: Bashoratlarni ariza beruvchilarga tushuntirish muhim",
        "RU": "Прозрачность: Важно объяснять прогнозы заявителям",
    },
    "ethics_regulation": {
        "EN": "Regulation: Real loan decisions must comply with fair lending laws",
        "UZ": "Tartibga solish: Haqiqiy kredit qarorlari adolatli kreditlash qonunlariga mos kelishi kerak",
        "RU": "Регулирование: Реальные кредитные решения должны соответствовать законам о справедливом кредитовании",
    },
    "ethics_oversight": {
        "EN": "Human oversight: ML should assist, not replace, human judgment",
        "UZ": "Inson nazorati: ML inson fikriga yordam berishi kerak, uni almashtirmasligi kerak",
        "RU": "Человеческий контроль: ML должен помогать, а не заменять человеческое суждение",
    },
    "tech_details": {
        "EN": "👨‍💻 Technical Details",
        "UZ": "👨‍💻 Texnik Ma'lumotlar",
        "RU": "👨‍💻 Технические Детали",
    },
    "current_model_info": {
        "EN": "📊 Current Model Info",
        "UZ": "📊 Joriy Model Ma'lumotlari",
        "RU": "📊 Информация о Текущей Модели",
    },
    "coursework_note": {
        "EN": "Built for coursework demonstration purposes.",
        "UZ": "Kurs ishi namoyishi maqsadlarida yaratilgan.",
        "RU": "Создано для демонстрации курсовой работы.",
    },
}


def get_text(key: str, lang: str = DEFAULT_LANGUAGE) -> str:
    """
    Get translated text for a given key.
    
    Args:
        key: Translation key
        lang: Language code (EN, UZ, RU)
        
    Returns:
        Translated text or key if not found
    """
    if key not in TRANSLATIONS:
        return key
    
    translation = TRANSLATIONS[key]
    
    if lang in translation:
        return translation[lang]
    elif DEFAULT_LANGUAGE in translation:
        return translation[DEFAULT_LANGUAGE]
    else:
        return key


def t(key: str, lang: str = DEFAULT_LANGUAGE, **kwargs) -> str:
    """
    Shorthand for get_text with optional string formatting.
    
    Args:
        key: Translation key
        lang: Language code
        **kwargs: Format arguments
        
    Returns:
        Translated and formatted text
    """
    text = get_text(key, lang)
    
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass
    
    return text
