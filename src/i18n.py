"""
Internationalization (i18n) module for the Loan Approval Prediction application.
Supports: English (EN), Uzbek (UZ), Russian (RU)
"""

# Available languages
LANGUAGES = {
    "UZ": "O'zbek",
    "RU": "Русский",
    "EN": "English",
}

DEFAULT_LANGUAGE = "UZ"

# Translation dictionary
TRANSLATIONS = {
    # ==========================================================================
    # Navigation & Common
    # ==========================================================================
    "app_title": {
        "UZ": "🏦 Kredit Tasdiqlash",
        "RU": "🏦 Одобрение Кредита",
        "EN": "🏦 Loan Approval",
    },
    "nav_train": {
        "UZ": "O'qitish va Metrikalar",
        "RU": "Обучение и Метрики",
        "EN": "Train & Metrics",
    },
    "nav_single": {
        "UZ": "Yakka Bashorat",
        "RU": "Единичный Прогноз",
        "EN": "Single Prediction",
    },
    "nav_batch": {
        "UZ": "Ommaviy Bashorat",
        "RU": "Пакетный Прогноз",
        "EN": "Batch Prediction",
    },
    "nav_about": {
        "UZ": "Haqida",
        "RU": "О Программе",
        "EN": "About",
    },
    "nav_eda": {
        "UZ": "Ma'lumotlar Tahlili (EDA)",
        "RU": "Исследовательский Анализ (EDA)",
        "EN": "Exploratory Data Analysis",
    },
    "language": {
        "UZ": "Til",
        "RU": "Язык",
        "EN": "Language",
    },
    "model_trained": {
        "UZ": "✓ Model o'qitilgan",
        "RU": "✓ Модель обучена",
        "EN": "✓ Model trained",
    },
    "no_model": {
        "UZ": "⚠ O'qitilgan model yo'q",
        "RU": "⚠ Модель не обучена",
        "EN": "⚠ No trained model",
    },
    "go_to_training": {
        "UZ": "'O'qitish va Metrikalar' ga o'ting",
        "RU": "Перейдите в 'Обучение и Метрики'",
        "EN": "Go to 'Train & Metrics' to train",
    },
    "model": {
        "UZ": "Model",
        "RU": "Модель",
        "EN": "Model",
    },
    "accuracy": {
        "UZ": "Aniqlik",
        "RU": "Точность",
        "EN": "Accuracy",
    },
    
    # ==========================================================================
    # Train & Metrics Page
    # ==========================================================================
    "train_title": {
        "UZ": "📊 O'qitish va Metrikalar",
        "RU": "📊 Обучение и Метрики",
        "EN": "📊 Train & Metrics",
    },
    "data_not_found": {
        "UZ": "⚠️ O'qitish ma'lumotlari topilmadi!",
        "RU": "⚠️ Данные для обучения не найдены!",
        "EN": "⚠️ Training data not found!",
    },
    "download_prompt": {
        "UZ": "Iltimos, Kaggle'dan `train.csv` ni yuklab, quyidagi joyga qo'ying:",
        "RU": "Пожалуйста, скачайте `train.csv` с Kaggle и поместите в:",
        "EN": "Please download `train.csv` from Kaggle and place it in:",
    },
    "download_link": {
        "UZ": "📥 Yuklab olish: ",
        "RU": "📥 Скачать с: ",
        "EN": "📥 Download from: ",
    },
    "model_training": {
        "UZ": "🎯 Modelni O'qitish",
        "RU": "🎯 Обучение Модели",
        "EN": "🎯 Model Training",
    },
    "train_button": {
        "UZ": "🚀 Modelni O'qitish",
        "RU": "🚀 Обучить Модель",
        "EN": "🚀 Train Model",
    },
    "training_progress": {
        "UZ": "Model o'qitilmoqda... Bir oz vaqt olishi mumkin.",
        "RU": "Обучение модели... Это может занять минуту.",
        "EN": "Training model... This may take a minute.",
    },
    "training_success": {
        "UZ": "✓ Model muvaffaqiyatli o'qitildi!",
        "RU": "✓ Модель успешно обучена!",
        "EN": "✓ Model trained successfully!",
    },
    "training_failed": {
        "UZ": "O'qitish muvaffaqiyatsiz: ",
        "RU": "Ошибка обучения: ",
        "EN": "Training failed: ",
    },
    "model_type": {
        "UZ": "Model Turi",
        "RU": "Тип Модели",
        "EN": "Model Type",
    },
    "test_accuracy": {
        "UZ": "Test Aniqligi",
        "RU": "Точность Теста",
        "EN": "Test Accuracy",
    },
    "train_prompt": {
        "UZ": "👆 Metrikalar va baholash natijalarini ko'rish uchun modelni o'qiting.",
        "RU": "👆 Обучите модель, чтобы увидеть метрики.",
        "EN": "👆 Train a model to see metrics and evaluation results.",
    },
    "evaluation_results": {
        "UZ": "📈 Baholash Natijalari",
        "RU": "📈 Результаты Оценки",
        "EN": "📈 Evaluation Results",
    },
    "evaluating": {
        "UZ": "Model baholanmoqda...",
        "RU": "Оценка модели...",
        "EN": "Evaluating model...",
    },
    "precision": {
        "UZ": "Aniqlik",
        "RU": "Точность",
        "EN": "Precision",
    },
    "recall": {
        "UZ": "Qaytaruvchanlik",
        "RU": "Полнота",
        "EN": "Recall",
    },
    "f1_score": {
        "UZ": "F1 Ko'rsatkichi",
        "RU": "F1 Мера",
        "EN": "F1 Score",
    },
    "roc_auc": {
        "UZ": "ROC-AUC",
        "RU": "ROC-AUC",
        "EN": "ROC-AUC",
    },
    "confusion_matrix": {
        "UZ": "Chalkashlik Matritsasi",
        "RU": "Матрица Ошибок",
        "EN": "Confusion Matrix",
    },
    "roc_curve": {
        "UZ": "ROC Egri Chizig'i",
        "RU": "ROC Кривая",
        "EN": "ROC Curve",
    },
    "feature_importance": {
        "UZ": "🔍 Xususiyat Ahamiyati",
        "RU": "🔍 Важность Признаков",
        "EN": "🔍 Feature Importance",
    },
    "evaluation_failed": {
        "UZ": "Baholash muvaffaqiyatsiz: ",
        "RU": "Ошибка оценки: ",
        "EN": "Evaluation failed: ",
    },
    
    # ==========================================================================
    # Single Prediction Page
    # ==========================================================================
    "prediction_title": {
        "UZ": "🔮 Yakka Bashorat",
        "RU": "🔮 Единичный Прогноз",
        "EN": "🔮 Single Prediction",
    },
    "no_model_warning": {
        "UZ": "⚠️ O'qitilgan model topilmadi. Avval modelni o'qiting.",
        "RU": "⚠️ Модель не найдена. Сначала обучите модель.",
        "EN": "⚠️ No trained model found. Please train a model first.",
    },
    "enter_details": {
        "UZ": "Kredit tasdiqlashini bashorat qilish uchun ariza beruvchi ma'lumotlarini kiriting.",
        "RU": "Введите данные заявителя для прогноза одобрения кредита.",
        "EN": "Enter applicant details to predict loan approval.",
    },
    "applicant_info": {
        "UZ": "📝 Ariza Beruvchi Ma'lumotlari",
        "RU": "📝 Информация о Заявителе",
        "EN": "📝 Applicant Information",
    },
    "gender": {
        "UZ": "Jinsi",
        "RU": "Пол",
        "EN": "Gender",
    },
    "gender_male": {
        "UZ": "Erkak",
        "RU": "Мужской",
        "EN": "Male",
    },
    "gender_female": {
        "UZ": "Ayol",
        "RU": "Женский",
        "EN": "Female",
    },
    "married": {
        "UZ": "Oilali",
        "RU": "Женат/Замужем",
        "EN": "Married",
    },
    "yes": {
        "UZ": "Ha",
        "RU": "Да",
        "EN": "Yes",
    },
    "no": {
        "UZ": "Yo'q",
        "RU": "Нет",
        "EN": "No",
    },
    "dependents": {
        "UZ": "Qaramog'idagilar",
        "RU": "Иждивенцы",
        "EN": "Dependents",
    },
    "education": {
        "UZ": "Ta'lim",
        "RU": "Образование",
        "EN": "Education",
    },
    "graduate": {
        "UZ": "Oliy ma'lumotli",
        "RU": "Высшее",
        "EN": "Graduate",
    },
    "not_graduate": {
        "UZ": "Oliy ma'lumotsiz",
        "RU": "Без высшего",
        "EN": "Not Graduate",
    },
    "self_employed": {
        "UZ": "O'z-o'ziga ish beruvchi",
        "RU": "Самозанятый",
        "EN": "Self Employed",
    },
    "property_area": {
        "UZ": "Mulk Hududi",
        "RU": "Район Недвижимости",
        "EN": "Property Area",
    },
    "urban": {
        "UZ": "Shahar",
        "RU": "Городской",
        "EN": "Urban",
    },
    "rural": {
        "UZ": "Qishloq",
        "RU": "Сельский",
        "EN": "Rural",
    },
    "semiurban": {
        "UZ": "Shahar atrofi",
        "RU": "Пригород",
        "EN": "Semiurban",
    },
    "credit_history": {
        "UZ": "Kredit Tarixi",
        "RU": "Кредитная История",
        "EN": "Credit History",
    },
    "credit_good": {
        "UZ": "Yaxshi (1)",
        "RU": "Хорошая (1)",
        "EN": "Good (1)",
    },
    "credit_bad": {
        "UZ": "Yomon (0)",
        "RU": "Плохая (0)",
        "EN": "Bad (0)",
    },
    "applicant_income": {
        "UZ": "Ariza Beruvchi Daromadi ($)",
        "RU": "Доход Заявителя ($)",
        "EN": "Applicant Income ($)",
    },
    "coapplicant_income": {
        "UZ": "Qo'shma Ariza Beruvchi Daromadi ($)",
        "RU": "Доход Созаявителя ($)",
        "EN": "Coapplicant Income ($)",
    },
    "loan_amount": {
        "UZ": "Kredit Miqdori (minglar)",
        "RU": "Сумма Кредита (в тысячах)",
        "EN": "Loan Amount (in thousands)",
    },
    "loan_term": {
        "UZ": "Kredit Muddati (oylar)",
        "RU": "Срок Кредита (месяцы)",
        "EN": "Loan Term (months)",
    },
    "predict_button": {
        "UZ": "🔍 Bashorat",
        "RU": "🔍 Прогноз",
        "EN": "🔍 Predict",
    },
    "prediction_result": {
        "UZ": "📋 Bashorat Natijasi",
        "RU": "📋 Результат Прогноза",
        "EN": "📋 Prediction Result",
    },
    "approved": {
        "UZ": "Tasdiqlandi",
        "RU": "Одобрено",
        "EN": "Approved",
    },
    "rejected": {
        "UZ": "Rad etildi",
        "RU": "Отклонено",
        "EN": "Rejected",
    },
    "approval_probability": {
        "UZ": "Tasdiqlash Ehtimoli",
        "RU": "Вероятность Одобрения",
        "EN": "Approval Probability",
    },
    "probability_note": {
        "UZ": "Yuqori ehtimollik tasdiqlash imkoniyati yuqoriligini ko'rsatadi.",
        "RU": "Более высокая вероятность означает большую вероятность одобрения.",
        "EN": "Higher probability indicates higher likelihood of approval.",
    },
    "input_summary": {
        "UZ": "Kiritilgan Ma'lumotlar:",
        "RU": "Введённые Данные:",
        "EN": "Input Summary:",
    },
    "value": {
        "UZ": "Qiymat",
        "RU": "Значение",
        "EN": "Value",
    },
    "factors_title": {
        "UZ": "🔍 Qaysi Omillar Eng Muhim?",
        "RU": "🔍 Какие Факторы Важнее?",
        "EN": "🔍 What Factors Mattered Most?",
    },
    "factors_note": {
        "UZ": "Bu grafik modelning qaror qabul qilish jarayonida qaysi xususiyatlar eng muhim ekanligini ko'rsatadi.",
        "RU": "Эта диаграмма показывает, какие признаки наиболее важны в процессе принятия решений модели.",
        "EN": "This chart shows which features are generally most important in the model's decision-making process.",
    },
    "prediction_failed": {
        "UZ": "Bashorat muvaffaqiyatsiz: ",
        "RU": "Ошибка прогноза: ",
        "EN": "Prediction failed: ",
    },
    
    # ==========================================================================
    # Batch Prediction Page
    # ==========================================================================
    "batch_title": {
        "UZ": "📁 Ommaviy Bashorat",
        "RU": "📁 Пакетный Прогноз",
        "EN": "📁 Batch Prediction",
    },
    "batch_description": {
        "UZ": "Ommaviy bashoratlar olish uchun ariza beruvchilar ma'lumotlari bilan CSV fayl yuklang.",
        "RU": "Загрузите CSV файл с данными заявителей для пакетного прогноза.",
        "EN": "Upload a CSV file with applicant data to get batch predictions.",
    },
    "expected_format": {
        "UZ": "📋 Kutilgan CSV Formati",
        "RU": "📋 Ожидаемый Формат CSV",
        "EN": "📋 Expected CSV Format",
    },
    "columns_info": {
        "UZ": "CSV faylingiz quyidagi ustunlarni o'z ichiga olishi kerak:",
        "RU": "Ваш CSV должен содержать следующие столбцы:",
        "EN": "Your CSV should contain the following columns:",
    },
    "numeric_cols": {
        "UZ": "Raqamli",
        "RU": "Числовые",
        "EN": "Numeric",
    },
    "categorical_cols": {
        "UZ": "Kategorik",
        "RU": "Категориальные",
        "EN": "Categorical",
    },
    "sample_data": {
        "UZ": "Namuna ma'lumotlari:",
        "RU": "Пример данных:",
        "EN": "Sample data:",
    },
    "download_sample": {
        "UZ": "📥 Namuna CSV ni Yuklash",
        "RU": "📥 Скачать Пример CSV",
        "EN": "📥 Download Sample CSV",
    },
    "upload_csv": {
        "UZ": "CSV fayl yuklash",
        "RU": "Загрузить CSV файл",
        "EN": "Upload CSV file",
    },
    "upload_help": {
        "UZ": "Ariza beruvchi ma'lumotlari bilan CSV fayl yuklang",
        "RU": "Загрузите CSV файл с информацией о заявителях",
        "EN": "Upload a CSV file with applicant information",
    },
    "uploaded_preview": {
        "UZ": "📊 Yuklangan Ma'lumotlar Ko'rinishi",
        "RU": "📊 Предпросмотр Загруженных Данных",
        "EN": "📊 Uploaded Data Preview",
    },
    "total_rows": {
        "UZ": "Jami qatorlar",
        "RU": "Всего строк",
        "EN": "Total rows",
    },
    "missing_columns": {
        "UZ": "⚠️ Etishmayotgan kerakli ustunlar: ",
        "RU": "⚠️ Отсутствуют обязательные столбцы: ",
        "EN": "⚠️ Missing required columns: ",
    },
    "generate_predictions": {
        "UZ": "🔍 Bashoratlarni Yaratish",
        "RU": "🔍 Сгенерировать Прогнозы",
        "EN": "🔍 Generate Predictions",
    },
    "generating": {
        "UZ": "Bashoratlar yaratilmoqda...",
        "RU": "Генерация прогнозов...",
        "EN": "Generating predictions...",
    },
    "predictions_complete": {
        "UZ": "✓ {count} qator uchun bashoratlar yaratildi!",
        "RU": "✓ Прогнозы сгенерированы для {count} строк!",
        "EN": "✓ Predictions generated for {count} rows!",
    },
    "results_summary": {
        "UZ": "📈 Natijalar Qisqacha",
        "RU": "📈 Сводка Результатов",
        "EN": "📈 Results Summary",
    },
    "total_applications": {
        "UZ": "Jami Arizalar",
        "RU": "Всего Заявок",
        "EN": "Total Applications",
    },
    "average_probability": {
        "UZ": "O'rtacha Ehtimollik",
        "RU": "Средняя Вероятность",
        "EN": "Average Probability",
    },
    "predictions_header": {
        "UZ": "📋 Bashoratlar",
        "RU": "📋 Прогнозы",
        "EN": "📋 Predictions",
    },
    "download_predictions": {
        "UZ": "📥 Bashoratlar CSV ni Yuklash",
        "RU": "📥 Скачать CSV с Прогнозами",
        "EN": "📥 Download Predictions CSV",
    },
    "batch_error": {
        "UZ": "Faylni qayta ishlashda xatolik: ",
        "RU": "Ошибка обработки файла: ",
        "EN": "Error processing file: ",
    },
    
    # ==========================================================================
    # EDA Page
    # ==========================================================================
    "eda_title": {
        "UZ": "📊 Kredit Ma'lumotlari Tahlili",
        "RU": "📊 Исследовательский Анализ Данных",
        "EN": "📊 Loan Data Exploratory Analysis",
    },
    "eda_subtitle": {
        "UZ": "O'qitish ma'lumotlari taqsimoti va bog'liqliklarini o'rganing.",
        "RU": "Изучите распределение и взаимосвязи обучающих данных.",
        "EN": "Explore the training dataset distribution and relationships.",
    },
    "show_raw_data": {
        "UZ": "Xom ma'lumotlarni ko'rsatish",
        "RU": "Показать сырые данные",
        "EN": "Show Raw Data",
    },
    "dataset_overview": {
        "UZ": "1. Ma'lumotlar To'plami Umumiy Ko'rinishi",
        "RU": "1. Обзор Набора Данных",
        "EN": "1. Dataset Overview",
    },
    "rows": {
        "UZ": "Qatorlar",
        "RU": "Строки",
        "EN": "Rows",
    },
    "columns": {
        "UZ": "Ustunlar",
        "RU": "Столбцы",
        "EN": "Columns",
    },
    "missing_values": {
        "UZ": "Etishmayotgan Qiymatlar",
        "RU": "Пропущенные Значения",
        "EN": "Missing Values",
    },
    "raw_data_sample": {
        "UZ": "Xom Ma'lumot Namuna",
        "RU": "Пример Сырых Данных",
        "EN": "Raw Data Sample",
    },
    "target_dist": {
        "UZ": "2. Maqsadli O'zgaruvchi Taqsimoti (Kredit Holati)",
        "RU": "2. Распределение Целевой Переменной (Статус Кредита)",
        "EN": "2. Target Distribution (Loan Status)",
    },
    "approval_counts": {
        "UZ": "Kredit Tasdiqlash Soni",
        "RU": "Количество Одобрений Кредита",
        "EN": "Loan Approval Counts",
    },
    "categorical_vars": {
        "UZ": "3. Kategorik O'zgaruvchilar",
        "RU": "3. Категориальные Переменные",
        "EN": "3. Categorical Variables",
    },
    "select_cat": {
        "UZ": "Kategorik Xususiyatni Tanlang",
        "RU": "Выберите Категориальный Признак",
        "EN": "Select Categorical Feature",
    },
    "distribution_of": {
        "UZ": "{feature} Taqsimoti",
        "RU": "Распределение {feature}",
        "EN": "{feature} Distribution",
    },
    "vs_loan_status": {
        "UZ": "{feature} va Kredit Holati",
        "RU": "{feature} vs Статус Кредита",
        "EN": "{feature} vs Loan Status",
    },
    "numerical_vars": {
        "UZ": "4. Raqamli O'zgaruvchilar",
        "RU": "4. Числовые Переменные",
        "EN": "4. Numerical Variables",
    },
    "select_num": {
        "UZ": "Raqamli Xususiyatni Tanlang",
        "RU": "Выберите Числовой Признак",
        "EN": "Select Numerical Feature",
    },
    "by_loan_status": {
        "UZ": "{feature} Kredit Holati Bo'yicha",
        "RU": "{feature} по Статусу Кредита",
        "EN": "{feature} by Loan Status",
    },
    "correlation_heatmap": {
        "UZ": "5. Korrelyatsiya Issiqlik xaritasi (Raqamli)",
        "RU": "5. Тепловая Карта Корреляции (Числовые)",
        "EN": "5. Correlation Heatmap (Numerical)",
    },
    "no_numeric_corr": {
        "UZ": "Korrelyatsiya uchun raqamli ustunlar topilmadi.",
        "RU": "Не найдено числовых столбцов для корреляции.",
        "EN": "No numeric columns found for correlation.",
    },

    # ==========================================================================
    # About Page
    # ==========================================================================
    "about_title": {
        "UZ": "ℹ️ Haqida",
        "RU": "ℹ️ О Программе",
        "EN": "ℹ️ About",
    },
    "about_description": {
        "UZ": "Bu ilova ariza beruvchi xususiyatlariga asoslanib kredit arizasi tasdiqlanishini bashorat qilish uchun mashinaviy o'rganishdan foydalanadi.",
        "RU": "Это приложение использует машинное обучение для прогнозирования одобрения кредитной заявки на основе характеристик заявителя.",
        "EN": "This application uses machine learning to predict whether a loan application will be approved based on applicant characteristics.",
    },
    "dataset_title": {
        "UZ": "Ma'lumotlar To'plami",
        "RU": "Набор Данных",
        "EN": "Dataset",
    },
    "dataset_source": {
        "UZ": "Model Kaggle Kredit Bashorat ma'lumotlar to'plamida o'qitilgan",
        "RU": "Модель обучена на наборе данных Kaggle Loan Prediction",
        "EN": "The model is trained on the Kaggle Loan Prediction Dataset",
    },
    "feature": {
        "UZ": "Xususiyat",
        "RU": "Признак",
        "EN": "Feature",
    },
    "description": {
        "UZ": "Tavsif",
        "RU": "Описание",
        "EN": "Description",
    },
    "model_section": {
        "UZ": "Model",
        "RU": "Модель",
        "EN": "Model",
    },
    "models_compared": {
        "UZ": "Ilova ikki modelni solishtiradi:",
        "RU": "Приложение сравнивает две модели:",
        "EN": "The application compares two models:",
    },
    "baseline": {
        "UZ": "asosiy",
        "RU": "базовая",
        "EN": "baseline",
    },
    "strong": {
        "UZ": "kuchli",
        "RU": "сильная",
        "EN": "strong",
    },
    "cv_selection": {
        "UZ": "Eng yaxshi model 5-fold cross-validation orqali avtomatik tanlanadi.",
        "RU": "Лучшая модель выбирается автоматически с помощью 5-кратной перекрёстной проверки.",
        "EN": "The best model is selected automatically via 5-fold cross-validation.",
    },
    "preprocessing_title": {
        "UZ": "Oldindan Qayta Ishlash",
        "RU": "Предобработка",
        "EN": "Preprocessing",
    },
    "preprocessing_numeric": {
        "UZ": "Raqamli xususiyatlar: Etishmayotgan qiymatlar median bilan to'ldiriladi, keyin standartlashtiriladi",
        "RU": "Числовые признаки: Пропущенные значения заполняются медианой, затем стандартизируются",
        "EN": "Numeric features: Missing values imputed with median, then standardized",
    },
    "preprocessing_categorical": {
        "UZ": "Kategorik xususiyatlar: Etishmayotgan qiymatlar eng ko'p uchraydigan qiymat bilan to'ldiriladi, keyin one-hot kodlanadi",
        "RU": "Категориальные признаки: Пропущенные значения заполняются наиболее частым значением, затем one-hot кодируются",
        "EN": "Categorical features: Missing values imputed with most frequent, then one-hot encoded",
    },
    "preprocessing_note": {
        "UZ": "Barcha oldindan qayta ishlash ma'lumotlar oqishini oldini olish uchun sklearn Pipeline ichida amalga oshiriladi",
        "RU": "Вся предобработка выполняется внутри Pipeline sklearn для предотвращения утечки данных",
        "EN": "All preprocessing is done inside a sklearn Pipeline to prevent data leakage",
    },
    "limitations_title": {
        "UZ": "⚠️ Cheklovlar",
        "RU": "⚠️ Ограничения",
        "EN": "⚠️ Limitations",
    },
    "limitation_size": {
        "UZ": "Kichik ma'lumotlar to'plami: ~600 namuna ishlab chiqarish ML uchun cheklangan",
        "RU": "Маленький набор данных: ~600 примеров недостаточно для продакшн ML",
        "EN": "Small dataset: ~600 samples is limited for production ML",
    },
    "limitation_imbalance": {
        "UZ": "Sinf muvozanatsizligi: Ma'lumotlarda rad etilganlarga qaraganda ko'proq tasdiqlar",
        "RU": "Дисбаланс классов: В данных больше одобрений, чем отказов",
        "EN": "Class imbalance: More approvals than rejections in the data",
    },
    "limitation_features": {
        "UZ": "Etishmayotgan xususiyatlar: Haqiqiy dunyoda kredit bali, ish tarixi kiritiladi",
        "RU": "Отсутствующие признаки: В реальности нужны кредитный рейтинг, история занятости",
        "EN": "Missing features: Real-world would include credit score, employment history",
    },
    "limitation_temporal": {
        "UZ": "Vaqtga asoslangan tekshiruv yo'q: Vaqtga asoslangan train/test bo'linishi yo'q",
        "RU": "Нет временной валидации: Нет разделения train/test по времени",
        "EN": "No temporal validation: No time-based train/test split",
    },
    "tech_details": {
        "UZ": "👨‍💻 Texnik Ma'lumotlar",
        "RU": "👨‍💻 Технические Детали",
        "EN": "👨‍💻 Technical Details",
    },
    # ==========================================================================
    # Feature Names (for EDA dropdowns)
    # ==========================================================================
    "ApplicantIncome": {
        "UZ": "Ariza Beruvchi Daromadi",
        "RU": "Доход Заявителя",
        "EN": "Applicant Income",
    },
    "CoapplicantIncome": {
        "UZ": "Qo'shma Ariza Beruvchi Daromadi",
        "RU": "Доход Созаявителя",
        "EN": "Coapplicant Income",
    },
    "LoanAmount": {
        "UZ": "Kredit Miqdori",
        "RU": "Сумма Кредита",
        "EN": "Loan Amount",
    },
    "Loan_Amount_Term": {
        "UZ": "Kredit Muddati",
        "RU": "Срок Кредита",
        "EN": "Loan Term",
    },
    "Credit_History": {
        "UZ": "Kredit Tarixi",
        "RU": "Кредитная История",
        "EN": "Credit History",
    },
    "Gender": {
        "UZ": "Jinsi",
        "RU": "Пол",
        "EN": "Gender",
    },
    "Married": {
        "UZ": "Oilaviy Holati",
        "RU": "Семейное Положение",
        "EN": "Married",
    },
    "Dependents": {
        "UZ": "Qaramog'idagilar",
        "RU": "Иждивенцы",
        "EN": "Dependents",
    },
    "Education": {
        "UZ": "Ma'lumoti",
        "RU": "Образование",
        "EN": "Education",
    },
    "Self_Employed": {
        "UZ": "Bandlik Holati",
        "RU": "Занятость",
        "EN": "Self Employed",
    },
    "Property_Area": {
        "UZ": "Mulk Hududi",
        "RU": "Район Недвижимости",
        "EN": "Property Area",
    },
    
    "coursework_note": {
        "UZ": "Kurs ishi namoyishi maqsadlarida yaratilgan.",
        "RU": "Создано для демонстрации курсовой работы.",
        "EN": "Built for coursework demonstration purposes.",
    },
    
    # ==========================================================================
    # Metadata Keys
    # ==========================================================================
    "meta_model_name": {
        "UZ": "Model Nomi",
        "RU": "Название Модели",
        "EN": "Model Name",
    },
    "meta_training_date": {
        "UZ": "O'qitilgan Sana",
        "RU": "Дата Обучения",
        "EN": "Training Date",
    },
    "meta_test_accuracy": {
        "UZ": "Test Aniqligi",
        "RU": "Точность Теста",
        "EN": "Test Accuracy",
    },
    "meta_random_state": {
        "UZ": "Tasodifiy Holat (Seed)",
        "RU": "Случайное Состояние (Seed)",
        "EN": "Random State (Seed)",
    },
    "meta_train_samples": {
        "UZ": "O'qitish Namunalari",
        "RU": "Обучающие Примеры",
        "EN": "Training Samples",
    },
    "meta_test_samples": {
        "UZ": "Test Namunalari",
        "RU": "Тестовые Примеры",
        "EN": "Test Samples",
    },
    "meta_n_features": {
        "UZ": "Xususiyatlar Soni",
        "RU": "Количество Признаков",
        "EN": "Number of Features",
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
