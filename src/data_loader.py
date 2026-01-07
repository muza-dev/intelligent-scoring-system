"""
Data loading utilities for the Loan Approval Prediction application.
"""
import pandas as pd
from sklearn.model_selection import train_test_split

from . import config
from .utils import setup_logging

logger = setup_logging(__name__)


def load_raw_data(filepath: str | None = None) -> pd.DataFrame:
    """
    Load raw CSV data from file.
    
    Args:
        filepath: Path to CSV file. If None, uses default train.csv path.
        
    Returns:
        DataFrame containing raw data
        
    Raises:
        FileNotFoundError: If the data file doesn't exist
    """
    path = filepath if filepath else config.TRAIN_DATA_PATH
    
    logger.info(f"Loading data from {path}")
    
    if not path.exists() if hasattr(path, 'exists') else not pd.io.common.file_exists(path):
        raise FileNotFoundError(
            f"Data file not found: {path}\n"
            f"Please download the dataset from Kaggle and place it in data/raw/"
        )
    
    df = pd.read_csv(path)
    logger.info(f"Loaded {len(df)} rows with {len(df.columns)} columns")
    
    return df


def prepare_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """
    Prepare data for modeling: drop ID, convert target.
    
    Args:
        df: Raw DataFrame
        
    Returns:
        Tuple of (features DataFrame, target Series)
    """
    df = df.copy()
    
    # Drop Loan_ID if present
    if config.ID_COLUMN in df.columns:
        df = df.drop(columns=[config.ID_COLUMN])
        logger.info(f"Dropped {config.ID_COLUMN} column")
    
    # Convert target: Y -> 1, N -> 0
    if config.TARGET_COLUMN in df.columns:
        df[config.TARGET_COLUMN] = df[config.TARGET_COLUMN].map({"Y": 1, "N": 0})
        
        # Check for unmapped values
        if df[config.TARGET_COLUMN].isna().any():
            raise ValueError(
                f"Target column contains values other than 'Y' or 'N'"
            )
        
        y = df[config.TARGET_COLUMN]
        X = df.drop(columns=[config.TARGET_COLUMN])
        
        logger.info(f"Target distribution: {y.value_counts().to_dict()}")
    else:
        # No target column (for prediction)
        X = df
        y = None
    
    # Ensure only expected feature columns are used
    available_features = [col for col in config.FEATURE_COLUMNS if col in X.columns]
    X = X[available_features]
    
    logger.info(f"Features shape: {X.shape}")
    
    return X, y


def split_data(
    X: pd.DataFrame, 
    y: pd.Series
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split data into train and test sets with stratification.
    
    Args:
        X: Features DataFrame
        y: Target Series
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config.TEST_SIZE,
        random_state=config.RANDOM_STATE,
        stratify=y
    )
    
    logger.info(f"Train set size: {len(X_train)}")
    logger.info(f"Test set size: {len(X_test)}")
    
    return X_train, X_test, y_train, y_test


def load_and_split() -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Convenience function to load data and split in one step.
    
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    df = load_raw_data()
    X, y = prepare_data(df)
    return split_data(X, y)


def validate_input_data(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Validate input data for prediction.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = []
    
    # Check for required columns
    missing_cols = set(config.FEATURE_COLUMNS) - set(df.columns)
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    # Check numeric columns are numeric
    for col in config.NUMERIC_FEATURES:
        if col in df.columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                # Try to convert
                try:
                    pd.to_numeric(df[col])
                except (ValueError, TypeError):
                    errors.append(f"Column {col} must be numeric")
    
    is_valid = len(errors) == 0
    
    return is_valid, errors
