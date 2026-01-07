"""
Configuration constants for the Loan Approval Prediction application.
"""
from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
MODELS_DIR = PROJECT_ROOT / "models"

# Data files
TRAIN_DATA_PATH = RAW_DATA_DIR / "train.csv"
SAMPLE_INPUT_PATH = DATA_DIR / "sample_input.csv"

# Model files
MODEL_PATH = MODELS_DIR / "loan_model.joblib"
METADATA_PATH = MODELS_DIR / "model_metadata.json"

# =============================================================================
# Dataset Configuration
# =============================================================================
# Target column
TARGET_COLUMN = "Loan_Status"

# ID column to drop (not used for modeling)
ID_COLUMN = "Loan_ID"

# Feature columns by type
NUMERIC_FEATURES = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
]

CATEGORICAL_FEATURES = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
]

# All feature columns (order matters for pipeline)
FEATURE_COLUMNS = NUMERIC_FEATURES + CATEGORICAL_FEATURES

# =============================================================================
# Model Configuration
# =============================================================================
RANDOM_STATE = 42
TEST_SIZE = 0.2
CV_FOLDS = 5

# Hyperparameters
LOGISTIC_REGRESSION_PARAMS = {
    "max_iter": 1000,
    "random_state": RANDOM_STATE,
    "solver": "lbfgs",
}

RANDOM_FOREST_PARAMS = {
    "n_estimators": 100,
    "max_depth": 10,
    "min_samples_split": 5,
    "min_samples_leaf": 2,
    "random_state": RANDOM_STATE,
    "n_jobs": -1,
}

# =============================================================================
# UI Configuration
# =============================================================================
# Mapping for user-friendly labels in the UI
GENDER_OPTIONS = ["Male", "Female"]
MARRIED_OPTIONS = ["Yes", "No"]
DEPENDENTS_OPTIONS = ["0", "1", "2", "3+"]
EDUCATION_OPTIONS = ["Graduate", "Not Graduate"]
SELF_EMPLOYED_OPTIONS = ["Yes", "No"]
PROPERTY_AREA_OPTIONS = ["Urban", "Rural", "Semiurban"]

# =============================================================================
# Logging Configuration
# =============================================================================
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"
