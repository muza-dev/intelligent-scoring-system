"""
Internationalization (i18n) module for the Intelligent Scoring application.
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
        "UZ": "🏦 Intellektual skoring",
        "RU": "🏦 Интеллектуальный скоринг",
        "EN": "🏦 Intelligent Scoring",
    },
    "nav_welcome": {
        "UZ": "Xush Kelibsiz",
        "RU": "Добро Пожаловать",
        "EN": "Welcome",
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
    "theme": {
        "UZ": "Mavzu",
        "RU": "Тема",
        "EN": "Theme",
    },
    "theme_system": {
        "UZ": "Tizim standart",
        "RU": "Системная тема",
        "EN": "System Default",
    },
    "theme_dark": {
        "UZ": "Tungi rejim",
        "RU": "Темная тема",
        "EN": "Dark Mode",
    },
    "theme_light": {
        "UZ": "Kunduzgi rejim",
        "RU": "Светлая тема",
        "EN": "Light Mode",
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
    # Welcome Page
    # ==========================================================================
    "welcome_header": {
        "UZ": "Iste'mol kreditlari uchun intellektual skoring platformasiga xush kelibsiz, {name}!",
        "RU": "Добро пожаловать на платформу интеллектуального скоринга для потребительских кредитов, {name}!",
        "EN": "Welcome to the platform for intelligent scoring of consumer loans, {name}!",
    },
    "welcome_subtitle": {
        "UZ": "Iste'mol kreditlari uchun intellektual skoring platformasiga xush kelibsiz.",
        "RU": "Добро пожаловать на платформу интеллектуального скоринга для потребительских кредитов.",
        "EN": "Welcome to the platform for intelligent scoring of consumer loans.",
    },
    "welcome_instructions": {
        "UZ": "Siz ushbu tizim orqali mijozlaringiz uchun kredit arizalarini tahlil qilishingiz va natijalar olishingiz mumkin.",
        "RU": "С помощью этой системы вы можете анализировать кредитные заявки и получать результаты для ваших клиентов.",
        "EN": "With this system, you can analyze loan applications and get results for your clients.",
    },
    "welcome_step_1": {
        "UZ": "1. Chap tarafdagi menyu orqali 'Yakka Bashorat' yoki 'Ommaviy Bashorat' bo'limini tanlang.",
        "RU": "1. Выберите в меню слева раздел 'Единичный Прогноз' или 'Пакетный Прогноз'.",
        "EN": "1. Select 'Single Prediction' or 'Batch Prediction' from the menu on the left.",
    },
    "welcome_step_2": {
        "UZ": "2. Mijoz ma'lumotlarini kiriting yoki CSV faylni yuklang.",
        "RU": "2. Введите данные клиента или загрузите CSV-файл.",
        "EN": "2. Enter client information or upload a CSV file.",
    },
    "welcome_step_3": {
        "UZ": "3. 'Bashorat' tugmasini bosing va natijalarni ko'ring.",
        "RU": "3. Нажмите кнопку 'Прогноз' и посмотрите результаты.",
        "EN": "3. Press the 'Predict' button and view the results.",
    },
    "welcome_contact_admin": {
        "UZ": "Agar sizda biror savol yoki muammo bo'lsa, iltimos, Administratorga murojaat qiling.",
        "RU": "Если у вас возникли вопросы или проблемы, пожалуйста, обратитесь к администратору.",
        "EN": "If you have any questions or issues, please contact the Administrator.",
    },
    "admin_dashboard_caption": {
        "UZ": "🏦 Iste'mol kreditlari uchun intellektual skoring tizimi | Admin Dashboard",
        "RU": "🏦 Интеллектуальная система скоринга для потребительских кредитов | Панель Администратора",
        "EN": "🏦 Intelligent Scoring System for Consumer Loans | Admin Dashboard",
    },
    "welcome_admin_intro": {
        "UZ": "Admin sifatida sizda modelni boshqarish va tizim sozlamalariga kirish huquqi bor.",
        "RU": "Как администратор, вы имеете доступ к управлению моделями и системным настройкам.",
        "EN": "As an Administrator, you have access to model management and system settings.",
    },
    "train_desc_short": {
        "UZ": "Yangi modelni o'qiting va uning samaradorligini baholang.",
        "RU": "Обучите новую модель и оцените её эффективность.",
        "EN": "Train a new model and evaluate its performance metrics.",
    },
    "eda_desc_short": {
        "UZ": "Ma'lumotlar to'plamini vizual tahlil qiling.",
        "RU": "Визуализируйте и анализируйте наборы данных.",
        "EN": "Visualize and analyze the dataset distributions and correlations.",
    },
    "user_mgmt_desc_short": {
        "UZ": "Tizim foydalanuvchilarini boshqarish.",
        "RU": "Управление пользователями системы.",
        "EN": "Manage system users and their roles.",
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
    "edge_cases_alert": {
        "UZ": "⚠️ **{count}** ta shubhali holat (Edge Case) aniqlandi. Inson nazorati talab etiladi.",
        "RU": "⚠️ Обнаружено **{count}** пограничных случаев (Edge Cases). Требуется проверка человеком.",
        "EN": "⚠️ **{count}** Edge Cases detected. Human review required for these.",
    },
    "model_type": {
        "UZ": "Model Turi",
        "RU": "Тип Модели",
        "EN": "Model Type",
    },
    "edge_case_single_alert": {
        "UZ": "⚠️ **Shubhali holat - Inson nazorati talab etiladi**",
        "RU": "⚠️ **Пограничный случай - Требуется проверка человеком**",
        "EN": "⚠️ **Edge Case - Human Review Required**",
    },
    "edge_case_single_caption": {
        "UZ": "Ansambl modellari ushbu ariza bo'yicha turli xulosalar bergan. Iltimos, mutaxassisga yo'naltiring.",
        "RU": "Ансамблевые модели разошлись во мнениях. Пожалуйста, передайте эксперту.",
        "EN": "Ensemble models disagree on this application. Please route to a human expert.",
    },
    "high_confidence_alert": {
        "UZ": "🎯 **Yuqori ishonchli qaror**",
        "RU": "🎯 **Высокая степень уверенности**",
        "EN": "🎯 **High Confidence Decision**",
    },
    "high_confidence_caption": {
        "UZ": "Barcha ansambl modellari bir ovozdan rozilik berishgan.",
        "RU": "Все ансамблевые модели единогласно согласны.",
        "EN": "All ensemble models unanimously agree.",
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
    "roc_not_available": {
        "UZ": "Bu model ehtimollik bashoratini qo'llab-quvvatlamaydi (Hard Voting). ROC egri chizig'i mavjud emas.",
        "RU": "Эта модель не поддерживает вероятностные прогнозы (Hard Voting). ROC кривая недоступна.",
        "EN": "This model does not support probability predictions (Hard Voting). ROC curve is unavailable.",
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
        "UZ": "Ariza Beruvchi Daromadi (UZS)",
        "RU": "Доход Заявителя (UZS)",
        "EN": "Applicant Income (UZS)",
    },
    "coapplicant_income": {
        "UZ": "Qo'shma Ariza Beruvchi Daromadi (UZS)",
        "RU": "Доход Созаявителя (UZS)",
        "EN": "Coapplicant Income (UZS)",
    },
    "loan_amount": {
        "UZ": "Kredit Miqdori (UZS)",
        "RU": "Сумма Кредита (UZS)",
        "EN": "Loan Amount (UZS)",
    },
    "loan_term": {
        "UZ": "Kredit Muddati (oylar)",
        "RU": "Срок Кредита (месяцы)",
        "EN": "Loan Term (months)",
    },
    "loan_term_min": {
        "UZ": " (Min Oylar)",
        "RU": " (Мин. Месяцы)",
        "EN": " (Min Months)",
    },
    "loan_term_help": {
        "UZ": "Kreditning boshlanish (eng kam) muddati — maoshingizdan kelib chiqib eng kami bilan necha oyga olish mumkinligi avtomatik belgilandi.",
        "RU": "Начальный срок кредита — исходя из вашего дохода автоматически определен минимальный срок, на который можно получить кредит.",
        "EN": "Starting loan term — based on your income, the minimum possible term to take the loan has been automatically determined.",
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
        "UZ": "⚠️ Yetishmayotgan kerakli ustunlar: ",
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
        "UZ": "Yetishmayotgan Qiymatlar",
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
        "UZ": "Ushbu ilova iste'mol kreditlari uchun intellektual skoring orqali ariza beruvchi xususiyatlariga asoslanib kredit arizasini baholash uchun mashinaviy o'rganishdan foydalanadi.",
        "RU": "Это приложение использует машинное обучение для оценки кредитных заявок на основе характеристик заявителя путем создания интеллектуальной модели скоринга для потребительских кредитов.",
        "EN": "This application uses machine learning to evaluate loan applications based on applicant characteristics by developing an intelligent scoring model for consumer loans.",
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
        "UZ": "Ilova olti mashinaviy o'rganish modelini solishtiradi:",
        "RU": "Приложение сравнивает шесть моделей машинного обучения:",
        "EN": "The application compares six machine learning models:",
    },
    "baseline": {
        "UZ": "asosiy",
        "RU": "базовая",
        "EN": "baseline",
    },
    "strong": {
        "UZ": "kuchli daraxtlar qatori",
        "RU": "ансамбль деревьев",
        "EN": "tree ensemble",
    },
    "svm_desc": {
        "UZ": "chiziqsiz klassifikator",
        "RU": "нелинейный классификатор",
        "EN": "non-linear classifier",
    },
    "mlp_desc": {
        "UZ": "ko'p qatlamli neyron tarmoq",
        "RU": "многослойная нейронная сеть",
        "EN": "multi-layer neural network",
    },
    "rbf_desc": {
        "UZ": "radial bazis funksiyasi tarmog'i",
        "RU": "сеть радиальной базисной функции",
        "EN": "radial basis function network",
    },
    "ensemble_soft_desc": {
        "UZ": "og'irlangan yumshoq ovoz berish ansambli (5 ta bazaviy model)",
        "RU": "ансамбль взвешенного мягкого голосования (5 базовых моделей)",
        "EN": "weighted soft-voting ensemble of all 5 base models",
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
        "UZ": "Raqamli xususiyatlar: Yetishmayotgan qiymatlar median bilan to'ldiriladi, keyin standartlashtiriladi",
        "RU": "Числовые признаки: Пропущенные значения заполняются медианой, затем стандартизируются",
        "EN": "Numeric features: Missing values imputed with median, then standardized",
    },
    "preprocessing_categorical": {
        "UZ": "Kategorik xususiyatlar: Yetishmayotgan qiymatlar eng ko'p uchraydigan qiymat bilan to'ldiriladi, keyin one-hot kodlanadi",
        "RU": "Категориальные признаки: Пропущенные значения заполняются наиболее частым значением, затем one-hot кодируются",
        "EN": "Categorical features: Missing values imputed with most frequent, then one-hot encoded",
    },
    "preprocessing_note": {
        "UZ": "Barcha oldindan qayta ishlash ma'lumotlar oqishini oldini olish uchun sklearn Pipeline ichida amalga oshiriladi",
        "RU": "Вся предобработка выполняется внутри Pipeline sklearn для предотвращения утечки данных",
        "EN": "All preprocessing is done inside a sklearn Pipeline to prevent data leakage",
    },
    "about_ensemble_title": {
        "UZ": "Ansambl va Avtomatlashtirish",
        "RU": "Ансамбль и Автоматизация",
        "EN": "Ensemble & Automation",
    },
    "about_dynamic_loan": {
        "UZ": "**DTI asosi bilan Dinamik Muddat:** Kredit muddati endi mijoz daromadining 35% qoidasi asosida avtomatik hisoblanadi. Bu iqtisodiy qaltis muddatlarning oldini oladi.",
        "RU": "**Динамический Срок на базе DTI:** Срок кредита теперь автоматически рассчитывается на основе правила 35% от дохода. Это предотвращает выбор экономически рискованных сроков.",
        "EN": "**DTI-based Dynamic Term:** Loan terms are now dynamically calculated based on a 35% debt-to-income limit, preventing financially impossible short-term loans.",
    },
    "about_hitl": {
        "UZ": "**Human-in-the-Loop (HITL):** Turli bazaviy modellar bir-biriga qarama-qarshi xulosa bildirsa, tizim buni sezib shubhali (Edge Case) holat sifatida belgicha taqadi va uni ko'rib chiqishga taklif etadi.",
        "RU": "**Человек-в-цикле (HITL):** Если базовые модели кардинально расходятся во мнениях, система помечает это как 'Edge Case', требующий ручной проверки.",
        "EN": "**Human-in-the-Loop (HITL):** If base models strongly disagree, the system flags the application as an 'Edge Case' requiring manual review.",
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
        "UZ": "Yetishmayotgan xususiyatlar: Haqiqiy dunyoda kredit bali, ish tarixi kiritiladi",
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
    
    # ==========================================================================
    # Authentication Page
    # ==========================================================================
    "auth_login": {
        "UZ": "Tizimga kirish",
        "RU": "Войти",
        "EN": "Sign in",
    },
    "auth_username": {
        "UZ": "Foydalanuvchi nomi",
        "RU": "Имя пользователя",
        "EN": "Username",
    },
    "auth_password": {
        "UZ": "Parol",
        "RU": "Пароль",
        "EN": "Password",
    },
    "auth_login_btn": {
        "UZ": "Kirish",
        "RU": "Войти",
        "EN": "Login",
    },
    "auth_error": {
        "UZ": "Iltimos foydalanuvchi nomi va parolni kiriting",
        "RU": "Пожалуйста, введите имя пользователя и пароль",
        "EN": "Please enter both username and password",
    },
    "auth_invalid_credentials": {
        "UZ": "Foydalanuvchi nomi yoki parol noto'g'ri.",
        "RU": "Неверное имя пользователя или пароль.",
        "EN": "Invalid username or password.",
    },
    "auth_timeout": {
        "UZ": "Sizning seansingiz harakatsizlik tufayli yakunlandi. Iltimos, tizimga qayta kiring.",
        "RU": "Ваш сеанс истек из-за неактивности. Пожалуйста, войдите снова.",
        "EN": "Your session has expired due to inactivity. Please log in again.",
    },
    "logout": {
        "UZ": "Chiqish",
        "RU": "Выход",
        "EN": "Logout",
    },

    # ==========================================================================
    # User Management Page (Admin only)
    # ==========================================================================
    "nav_user_mgmt": {
        "UZ": "Foydalanuvchilar",
        "RU": "Пользователи",
        "EN": "User Management",
    },
    "user_mgmt_title": {
        "UZ": "👥 Bank Xodimlarini Boshqarish",
        "RU": "👥 Управление Сотрудниками",
        "EN": "👥 Bank Staff Management",
    },
    "staff_list": {
        "UZ": "Xodimlar Ro'yxati",
        "RU": "Список Сотрудников",
        "EN": "Staff List",
    },
    "add_staff": {
        "UZ": "Yangi Xodim Qo'shish",
        "RU": "Добавить Сотрудника",
        "EN": "Add New Staff",
    },
    "add_staff_btn": {
        "UZ": "Xodim Qo'shish",
        "RU": "Добавить",
        "EN": "Add Staff",
    },
    "delete_staff": {
        "UZ": "O'chirish",
        "RU": "Удалить",
        "EN": "Delete",
    },
    "role_admin": {
        "UZ": "Administrator",
        "RU": "Администратор",
        "EN": "Admin",
    },
    "role_staff": {
        "UZ": "Bank Xodimi",
        "RU": "Сотрудник Банка",
        "EN": "Bank Staff",
    },
    "staff_deleted": {
        "UZ": "✓ Xodim muvaffaqiyatli o'chirildi.",
        "RU": "✓ Сотрудник успешно удалён.",
        "EN": "✓ Staff member deleted successfully.",
    },
    "staff_added": {
        "UZ": "✓ Yangi xodim muvaffaqiyatli qo'shildi.",
        "RU": "✓ Новый сотрудник успешно добавлен.",
        "EN": "✓ New staff member added successfully.",
    },
    "staff_username_taken": {
        "UZ": "Bu foydalanuvchi nomi allaqachon band.",
        "RU": "Это имя пользователя уже занято.",
        "EN": "That username is already taken.",
    },
    "no_staff": {
        "UZ": "Hozircha hech qanday xodim yo'q.",
        "RU": "Пока нет ни одного сотрудника.",
        "EN": "No staff members yet.",
    },
    "confirm_delete": {
        "UZ": "Haqiqatan ham o'chirmoqchimisiz?",
        "RU": "Вы уверены, что хотите удалить?",
        "EN": "Are you sure you want to delete?",
    },
    "full_name": {
        "UZ": "To'liq Ism",
        "RU": "Полное Имя",
        "EN": "Full Name",
    },
    "phone_label": {
        "UZ": "Telefon Raqami",
        "RU": "Номер Телефона",
        "EN": "Phone Number",
    },
    "email_label": {
        "UZ": "Elektron Pochta",
        "RU": "Электронная Почта",
        "EN": "Email",
    },
    "national_id_label": {
        "UZ": "Pasport Raqami / JSHSHIR",
        "RU": "Серия Паспорта / ПИНФЛ",
        "EN": "National ID / Passport No",
    },
    "address_label": {
        "UZ": "Manzil",
        "RU": "Адрес",
        "EN": "Address",
    },
    "income_label": {
        "UZ": "Oylik Daromad",
        "RU": "Ежемесячный Доход",
        "EN": "Monthly Income",
    },
    "username_label": {
        "UZ": "Foydalanuvchi Nomi",
        "RU": "Имя пользователя",
        "EN": "Username",
    },
    "password_label": {
        "UZ": "Parol",
        "RU": "Пароль",
        "EN": "Password",
    },
    "confirm_password_label": {
        "UZ": "Parolni Tasdiqlang",
        "RU": "Подтвердите Пароль",
        "EN": "Confirm Password",
    },
    "fill_all_fields_err": {
        "UZ": "Iltimos, barcha maydonlarni to'ldiring.",
        "RU": "Пожалуйста, заполните все поля.",
        "EN": "Please fill in all fields.",
    },
    "passwords_mismatch_err": {
        "UZ": "Parollar mos kelmadi.",
        "RU": "Пароли не совпадают.",
        "EN": "Passwords do not match.",
    },
    "created_at": {
        "UZ": "Ro'yxatdan o'tgan sana",
        "RU": "Дата регистрации",
        "EN": "Registered On",
    },
    "actions": {
        "UZ": "Harakatlar",
        "RU": "Действия",
        "EN": "Actions",
    },

    # ==========================================================================
    # s
    # ==========================================================================
    "theme": {
        "UZ": "Mavzu",
        "RU": "Тема",
        "EN": "Theme",
    },
    "theme_system": {
        "UZ": "Tizim standart",
        "RU": "Системная",
        "EN": "System default",
    },
    "theme_dark": {
        "UZ": "To'q mavzu",
        "RU": "Темная тема",
        "EN": "Dark mode",
    },
    "theme_light": {
        "UZ": "Oq mavzu",
        "RU": "Светлая тема",
        "EN": "White mode",
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
