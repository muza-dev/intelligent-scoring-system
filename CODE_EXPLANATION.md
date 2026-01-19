# Codebase Explanation for Defense

This document explains every part of the code in simple words. You can use this to answer questions during your defense.

## 1. Main Application (`main.py`)

This file is the **entry point** of the web application. It connects the user interface (UI) to the logic.

### **Imports & Setup (Lines 1-35)**
- **Lines 14-19:** We tell Python where to look for our code folders. It adds the project root to the "path".
- **Lines 21-25:** Import libraries:
    - `streamlit`: The library that builds the website.
    - `base64`: Helps us load images (like the sidebar background).
    - `pandas` & `numpy`: Tools for working with data tables and numbers.
- **Lines 27-32:** Import our own custom code modules from the `src` folder (like `eda`, `predict`, `i18n` for translations).

### **Page Configuration (Lines 39-44)**
- `st.set_page_config(...)`: Sets the browser tab title to "Loan Approval Prediction", adds a bank icon (🏦), and sets the layout to "wide" (uses full screen).

### **Sidebar Background (Lines 46-76)**
- **What it does:** Shows the multicolor background picture in the sidebar.
- **`get_base64_of_bin_file()`**: Reads the image file and turns it into a long text string (Base64) so the browser can read it.
- **`set_sidebar_background()`**: Uses CSS (web design code) to "inject" this image into the specific sidebar part of the page (`data-testid="stSidebar"`).

### **Language Support (Lines 81-88)**
- Checks if a language is selected. If not, it sets the default to Uzbek (`DEFAULT_LANGUAGE`).
- `get_lang()`: A simple helper to ask "What language is currently selected?".

### **Caching (Lines 93-108)**
- **`@st.cache_resource`**: This is very important! It tells Streamlit: "Run this function ONCE and save the result."
- **`get_model()`**: Loads the AI model from the file. We cache it so we don't reload the heavy model file every time you click a button (which would be slow).
- **`get_cached_metadata()`**: Similar to above, but for the "About" page info (like accuracy score).

### **Sidebar Navigation (Lines 119-161)**
- **`render_sidebar()`**: Draws the left sidebar menu.
- **Line 127:** Dropdown to pick Language (Uzbek, Russian, English).
- **Line 135:** Reloads the app immediately if you change the language (`st.rerun()`).
- **Line 141:** The "Radio Button" menu that lets you switch between pages:
    - Train & Metrics (Modelni O'qitish)
    - EDA (Ma'lumotlar Tahlili)
    - Single Prediction (Yakka Bashorat)
    - Batch Prediction (Ommaviy Bashorat)
    - About (Haqida)

### **Training Page Logic (Lines 167-242)**
- **`render_train_page()`**: Runs when you select "Train & Metrics".
- **Lines 176-187:** Checks if `train.csv` exists. If not, shows an error and explains how to download it.
- **Line 195 (Button):** If you click "Train Model":
    - Shows a spinner ("Training model...").
    - Calls `train_model()` (from our `train.py` file) which actually does the ML work.
    - If successful, it shows a success message ("Model trained!").
    - **Line 204:** Reloads the page so the new model is loaded immediately.
- **Lines 214-215:** Shows the current model name (e.g., "LogisticRegression") and its accuracy score.
- **Line 229:** Uses `evaluate_model()` to calculate how good the model is.
- **Lines 234-239:** Shows the **Metrics** (Accuracy, Precision, Recall, F1, ROC-AUC) in big numbers.
- **Lines 246-250:** Draws the **Confusion Matrix** (where did the model make mistakes?) and **ROC Curve** charts.

### **Prediction Logic (Lines 245-364)**
*Note: This starts later in the file around line 260*
- **`render_prediction_page()`**: Runs when you select "Single Prediction".
- **Step 1:** Checks if a model exists. If no model, warns you to go train one first.
- **Step 2:** Creates input forms for the user:
    - **Number Inputs:** Income, Loan Amount, Term.
    - **Select Boxes (Dropdowns):** Gender, Married, Education, Property Area, etc.
- **Step 3:** "Predict" button.
- **Step 4:** Collects all inputs into a dictionary (`input_data`).
- **Step 5:** Calls `predict_single()` which asks the model for a result.
- **Step 6:** Shows the result:
    - Green box if Approved.
    - Red box if Rejected.
    - Shows a probability bar (e.g., "85% certainty").

### **Main Execution (Lines 640-664)**
- **`main()`**: The "boss" function.
- It calls `render_sidebar()` to see which page you want.
- Then use `if/elif` to run the correct function for that page (`render_train_page`, `render_eda_page`, etc.).
### Main Execution (Lines 640-664)
- **`main()`**: The "boss" function.
- It calls `render_sidebar()` to see which page you want.
- Then use `if/elif` to run the correct function for that page (`render_train_page`, `render_eda_page`, etc.).
- **Line 665:** Standard Python pattern `if __name__ == "__main__": main()` ensures this only runs if you execute the file directly.

---

## 2. Exploratory Data Analysis (`src/eda.py`)

This file handles the visual analysis part of the app (the "Ma'lumotlar Tahlili" page).

### **Imports & Data Loading (Lines 1-18)**
- Imports plotting libraries (`seaborn`, `matplotlib`) and our `config`.
- **`load_data()`**: Tries to read `train.csv`. If the file is missing, it returns `None`.

### **Page Rendering (Lines 20-30)**
- **`render_eda_page()`**: The main function for this page.
- Sets the title (translated).
- Loads the data. If data is missing (`df is None`), it shows an error message.

### **Visualization Sections**
1.  **Overview (Lines 37-41):** Displays 3 key numbers: Total rows (records), Total columns (features), and Missing values (empty cells).
2.  **Raw Data (Lines 34 & 43):** A checkbox. If checked, it shows the first 5 rows of the actual table.
3.  **Target Distribution (Lines 50-55):** A bar chart showing how many Loans were Approved (Y) vs Rejected (N). This is important to see if our dataset is balanced.
4.  **Categorical Features (Lines 60-83):**
    - A dropdown lets you pick a feature like "Gender" or "Education".
    - **Fig 1 (Left):** Shows the count of that feature (e.g., how many Males vs Females).
    - **Fig 2 (Right):** Shows the relationship with Loan Status (e.g., Do Males get approved more often?).
5.  **Numerical Features (Lines 88-108):**
    - Similar dropdown for numbers like "Income".
    - **Fig 1 (Left):** Histogram (distribution).
    - **Fig 2 (Right):** Box plot (shows outliers and median) split by Approved/Rejected.
6.  **Correlation (Lines 113-121):**
    - Shows a "Heatmap". Red means high positive correlation (they go up together), Blue means negative.

---

## 3. Model Training (`src/train.py`)

This is the "Brain" of the project where learning happens.

### **Pipeline Creation (Lines 18-38)**
- **`create_models()`**: Defines two AI candidates:
    1.  **Logistic Regression:** Good, simple baseline model.
    2.  **Random Forest:** More complex, powerful "ensemble" of decision trees.
- It uses a **Pipeline**. This is a wrapper that says: "First, clean the data (Preprocessor), THEN train the model (Classifier)". This ensures we always process data the exact same way.

### **Model Selection (Lines 41-86)**
- **`select_best_model()`**:
    - We don't just pick one. We try both!
    - **Cross-Validation (CV):** We split data into 5 parts. We train on 4 and test on 1, then rotate. This gives us 5 scores.
    - We take the average accuracy.
    - The model with the highest average score wins and is returned as the `best_model`.

### **Training Function (Lines 89-157)**
- **`train_model()`**:
    - Loads data.
    - Calls `select_best_model()` to find the winner.
    - **Line 114:** Retrains the winner on the *entire* dataset to make it as smart as possible.
    - **Line 148:** Saves the trained model to a file (`loan_model.joblib`) so we can use it later without retraining.
    - **Line 152:** Saves "metadata" (info about accuracy, date, etc.) to a JSON file.

---

## 4. Prediction Logic (`src/predict.py`)

This file uses the saved model to guess "Yes" or "No" for new people.

### **Loading (Lines 15-32)**
- **`load_model()`**: Reads the `loan_model.joblib` file from disk. If missing, it complains (raises Error).

### **Single Prediction (Lines 35-63)**
- **`predict_single(input_data)`**:
    - Takes user input (dictionary).
    - Converts it to a DataFrame (table).
    - **Line 56:** `model.predict()` -> Returns 1 (Yes) or 0 (No).
    - **Line 57:** `model.predict_proba()` -> Returns the confidence score (e.g., 0.85).
    - Returns the result so the UI can show it.

### **Batch Prediction (Lines 66-99)**
- **`predict_batch(df)`**:
    - Takes a big CSV file of many applicants.
    - Runs the model on all of them at once.
    - Adds "Status" and "Probability" columns to the file.
    - Returns the new table for the user to download.

---

## 5. Internationalization (`src/i18n.py`)

This file handles the translations (Uzbek, Russian, English).

### **Data Structure (Lines 6-11)**
- **`LANGUAGES`**: A simple dictionary mapping codes ("UZ") to names ("O'zbek").

### **Translation Storage (Lines 16-Feature End)**
- **`TRANSLATIONS`**: A huge dictionary.
    - **Keys** (e.g., `"app_title"`) are the internal IDs we use in code.
    - **Values** are dictionaries containing the text for "UZ", "RU", and "EN".

### **Helper Functions (Lines 619-664)**
- **`get_text(key, lang)`**:
    - Looks up the `key` in the big dictionary.
    - Returns the text for the requested `lang`.
    - If the translation is missing, it returns the key itself (so the app doesn't crash).
- **`t(key, lang)`**:
    - A short, easy-to-type nickname for `get_text`.
    - Usage: `t("hello", "UZ")` -> "Salom".
