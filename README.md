# Intelligent Scoring Application (Loan Approval App)

An interactive, multi-role Streamlit application designed for bank staff and administrators to train machine learning models and predict loan approvals. The application is fully localized (English, Russian, Uzbek) and supports an advanced multi-model registry.

## Key Features

- **Role-Based Authentication**: Separated views for `Admin` (full access to training, user management, EDA) and `Bank Staff` (access focused on executing single and batch predictions).
- **Multi-Model Registry**: Train, evaluate, and seamlessly toggle between multiple machine learning models (Logistic Regression, Random Forest, SVM, MLP) to find the best performing model.
- **Single & Batch Predictions**: 
  - Predict individual loan applications with detailed probability metrics and feature importance breakdowns.
  - Upload CSV files for batch prediction processing and download the scored results.
- **Exploratory Data Analysis (EDA)**: Admins can explore the dataset visually.
- **Internationalization (i18n)**: Full UI localization for English, Russian, and Uzbek, including proper regional currency formatting (UZS).
- **Customizable Themes**: Seamlessly switch between System, Light, and Dark themes.
- **Session Security**: Built-in inactivity session timeouts to ensure data security.

## Technology Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **Machine Learning**: Scikit-Learn
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Dependency Management**: `uv` / `pip` (Python >= 3.11)

## Setup & Installation

1. **Clone or Download the Repository**

2. **Create a Virtual Environment**
   It is recommended to use `uv` for faster dependency resolution, or standard `venv`:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or on Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the necessary packages using the `requirements.txt` or `pyproject.toml`:
   ```bash
   pip install -r requirements.txt
   ```
   *(Alternatively, `uv pip install -r requirements.txt`)*

4. **Add the Dataset**
   The application requires the [Kaggle Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset). Place the downloaded data in the `data/raw/` directory (if not already present or created by the app).

5. **Run the Application**
   ```bash
   streamlit run main.py
   ```

## Usage Notes

- **Login**: Use the built-in login interface. Admin credentials are required to initiate model training and user management.
- **Training**: Before making predictions, an Admin must visit the **Train & Metrics** tab to compute and activate a model.
- **Themes & Languages**: Can be adjusted via the top-right of the dashboard interface or selectively on the login screen.
