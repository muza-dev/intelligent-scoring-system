"""
Configuration constants for the Intelligent Scoring application.
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

# Legacy single-model files (kept for backward compat)
MODEL_PATH = MODELS_DIR / "loan_model.joblib"
METADATA_PATH = MODELS_DIR / "model_metadata.json"

# Multi-model registry
MODEL_REGISTRY_PATH = MODELS_DIR / "registry.json"

# Per-model artifact paths (add new models here as needed)
MODEL_PATHS = {
    "LogisticRegression": MODELS_DIR / "logistic_regression.joblib",
    "RandomForest":       MODELS_DIR / "random_forest.joblib",
    "SVM":                MODELS_DIR / "svm.joblib",
    "MLP":                MODELS_DIR / "mlp.joblib",
    "RBFNetwork":         MODELS_DIR / "rbf_network.joblib",
    "EnsembleHard":       MODELS_DIR / "ensemble_hard.joblib",
    "EnsembleSoft":       MODELS_DIR / "ensemble_model.joblib",
    "EnsembleStack":      MODELS_DIR / "ensemble_stack.joblib",
}

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
ENSEMBLE_SOFT_WEIGHTS = [0.218, 0.210, 0.209, 0.160, 0.203]

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
