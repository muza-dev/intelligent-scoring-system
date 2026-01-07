"""
Preprocessing pipeline for the Loan Approval Prediction application.
"""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from . import config
from .utils import setup_logging

logger = setup_logging(__name__)


def create_preprocessor() -> ColumnTransformer:
    """
    Create a sklearn ColumnTransformer for preprocessing.
    
    Numeric features: Impute with median, then scale
    Categorical features: Impute with most frequent, then one-hot encode
    
    Returns:
        Configured ColumnTransformer
    """
    # Numeric pipeline: impute median, then standardize
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    
    # Categorical pipeline: impute most frequent, then one-hot encode
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    
    # Combine into ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, config.NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, config.CATEGORICAL_FEATURES),
        ],
        remainder="drop",  # Drop any columns not specified
        verbose_feature_names_out=True,
    )
    
    logger.info("Created preprocessing pipeline")
    logger.info(f"  Numeric features ({len(config.NUMERIC_FEATURES)}): {config.NUMERIC_FEATURES}")
    logger.info(f"  Categorical features ({len(config.CATEGORICAL_FEATURES)}): {config.CATEGORICAL_FEATURES}")
    
    return preprocessor


def get_feature_names_after_preprocessing(preprocessor: ColumnTransformer) -> list[str]:
    """
    Get feature names after preprocessing (including one-hot encoded names).
    
    Args:
        preprocessor: Fitted ColumnTransformer
        
    Returns:
        List of feature names after transformation
    """
    try:
        return list(preprocessor.get_feature_names_out())
    except Exception as e:
        logger.warning(f"Could not get feature names: {e}")
        return []
