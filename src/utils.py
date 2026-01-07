"""
Utility functions for the Loan Approval Prediction application.
"""
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from . import config


def setup_logging(name: str = "loan_approval") -> logging.Logger:
    """
    Set up and return a configured logger.
    
    Args:
        name: Logger name
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(getattr(logging, config.LOG_LEVEL))
        
        handler = logging.StreamHandler()
        handler.setLevel(getattr(logging, config.LOG_LEVEL))
        
        formatter = logging.Formatter(config.LOG_FORMAT)
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
    
    return logger


def model_exists() -> bool:
    """
    Check if a trained model exists on disk.
    
    Returns:
        True if model file exists, False otherwise
    """
    return config.MODEL_PATH.exists()


def metadata_exists() -> bool:
    """
    Check if model metadata exists on disk.
    
    Returns:
        True if metadata file exists, False otherwise
    """
    return config.METADATA_PATH.exists()


def load_metadata() -> dict[str, Any]:
    """
    Load model metadata from JSON file.
    
    Returns:
        Dictionary containing model metadata
        
    Raises:
        FileNotFoundError: If metadata file doesn't exist
    """
    if not metadata_exists():
        raise FileNotFoundError(f"Metadata file not found: {config.METADATA_PATH}")
    
    with open(config.METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_metadata(metadata: dict[str, Any]) -> None:
    """
    Save model metadata to JSON file.
    
    Args:
        metadata: Dictionary containing model metadata
    """
    # Ensure models directory exists
    config.MODELS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Convert any non-serializable types
    serializable = _make_serializable(metadata)
    
    with open(config.METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, default=str)


def _make_serializable(obj: Any) -> Any:
    """
    Recursively convert objects to JSON-serializable types.
    
    Args:
        obj: Object to convert
        
    Returns:
        JSON-serializable version of the object
    """
    if isinstance(obj, dict):
        return {k: _make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [_make_serializable(item) for item in obj]
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, Path):
        return str(obj)
    elif hasattr(obj, "tolist"):  # numpy arrays
        return obj.tolist()
    elif hasattr(obj, "item"):  # numpy scalars
        return obj.item()
    else:
        return obj


def get_current_timestamp() -> str:
    """
    Get current timestamp as ISO format string.
    
    Returns:
        Current timestamp string
    """
    return datetime.now().isoformat()


def ensure_directories() -> None:
    """
    Ensure all required directories exist.
    """
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    config.RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    config.MODELS_DIR.mkdir(parents=True, exist_ok=True)
