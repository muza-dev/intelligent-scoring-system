"""
Utility functions for the Loan Approval Prediction application.
"""
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from . import config

import streamlit as st


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


# =============================================================================
# Theme & Styling Utilities
# =============================================================================

BASE_CSS = """
/* Global Unibody Background */
.stApp {
    background-attachment: fixed !important;
}

/* Sidebar Customization */
[data-testid="stSidebar"] {
    border-right: none !important;
    background-attachment: fixed !important;
}

[data-testid="stSidebarNav"] {
    padding-top: 2rem !important;
}

/* Modern Pill-style Radio Buttons */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 8px !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.03) !important;
    border-radius: 12px !important;
    padding: 10px 15px !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    transform: translateX(5px);
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-selected="true"] {
    background: linear-gradient(90deg, rgba(14, 165, 233, 0.2), rgba(99, 102, 241, 0.2)) !important;
    border: 1px solid rgba(14, 165, 233, 0.3) !important;
}

/* Sidebar Control Labels */
[data-testid="stSidebar"] .stSelectbox label {
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    margin-bottom: 4px !important;
    opacity: 0.8;
}

/* Custom input fields styling base */
.input-label {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 6px;
    display: block;
    margin-top: 15px;
    padding-left: 10px;
}

.stTextInput {
    margin-bottom: 0 !important;
    padding-bottom: 0 !important;
}

.stTextInput div[data-baseweb="input"] {
    border-radius: 25px !important;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    transition: all 0.3s ease !important;
    min-height: 48px !important;
    padding: 0px 10px !important;
}

.stTextInput input {
    background-color: transparent !important;
    font-size: 15px !important;
}

.stTextInput > div > div {
    border: none !important;
    background-color: transparent !important;
    box-shadow: none !important;
}

/* Checkbox base */
.stCheckbox { padding-top: 0 !important; display: inline-block; padding-left: 5px; }
.stCheckbox label { padding-top: 0 !important; margin-top: 0 !important; }
.stCheckbox p {
    font-weight: 600 !important;
    font-size: 20px !important;
    line-height: 1 !important;
}

/* Primary Actions base */
button[kind="primaryFormSubmit"], button[kind="primary"] {
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border-radius: 30px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: 10px !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}
button[kind="primaryFormSubmit"]:hover, button[kind="primary"]:hover {
    transform: translateY(-2px);
}

/* Selectboxes base styling */
div[data-baseweb="select"] > div {
    backdrop-filter: blur(10px) !important;
    border-radius: 20px !important;
    cursor: pointer !important;
}
div[data-baseweb="select"] span {
    font-weight: 600 !important;
    font-size: 13px !important;
}
"""

LOGIN_SPECIFIC_CSS = """
/* Hide sidebar and header while logged out */
[data-testid="stSidebar"] { display: none; }
header[data-testid="stHeader"] { display: none; }
.stApp > header { display: none; }

/* Force main block to center glass card natively */
[data-testid="stMainBlockContainer"] {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 0 !important;
    overflow: hidden;
    position: relative;
}

/* Fixed Top Controls Selector Container */
.top-controls-container {
    position: absolute !important;
    top: 15px !important;
    right: 10px !important;
    z-index: 99999 !important;
    display: flex;
    gap: 8px;
    width: 280px !important;
    justify-content: flex-end !important;
}

/* Constrain main block child width */
div[data-testid="stMainBlockContainer"] > div:first-child {
    max-width: 780px !important;
    margin: 0 auto !important;
    width: 100% !important;
    margin-top: -5vh !important;
}

/* Titles */
.login-title {
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 30px;
    letter-spacing: 0.5px;
}

/* Primary buttons specific to login form */
button[kind="primaryFormSubmit"], button[kind="primary"] {
    width: 100% !important;
    margin-top: 30px !important;
    min-height: 50px !important;
    height: 50px !important;
    margin-bottom: 0 !important;
}

[data-testid="stForm"] {
    border: none !important;
    padding: 0 !important;
    background: transparent !important;
}

/* Target columns for top controls - login page specific */
div[data-testid="column"]:nth-child(1) {
    width: 100px !important;
    min-width: 100px !important;
    flex: none !important;
}
div[data-testid="column"]:nth-child(2) {
    width: 160px !important;
    min-width: 160px !important;
    flex: none !important;
}
"""

DARK_CSS = """
/* Background Sync */
.stApp, [data-testid="stSidebar"] {
    background: radial-gradient(circle at 15% 50%, rgba(14, 165, 233, 0.15), transparent 50%),
                radial-gradient(circle at 85% 30%, rgba(99, 102, 241, 0.15), transparent 50%),
                radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
    background-color: #020617 !important;
    background-size: cover !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}

/* Sidebar Specific Overrides for Dark Mode */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #020617 100%) !important;
    box-shadow: 5px 0 30px rgba(0, 0, 0, 0.5) !important;
}

/* Typography */
.login-title, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, .stRadio label p { color: white !important; }
.input-label, [data-testid="stSidebar"] label { color: rgba(255, 255, 255, 0.9) !important; }
.stCheckbox p { color: white !important; }

/* Sidebar Radio/Navigation Text color */
[data-testid="stSidebar"] .stRadio label p {
    color: rgba(255, 255, 255, 0.8) !important;
    font-weight: 500 !important;
}

/* TextInput */
.stTextInput div[data-baseweb="input"] {
    background-color: rgba(255, 255, 255, 0.07) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05), 0 4px 10px rgba(0,0,0,0.1) !important;
}
.stTextInput div[data-baseweb="input"]:focus-within {
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    background-color: rgba(255, 255, 255, 0.15) !important;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.2), inset 0 2px 4px rgba(0, 0, 0, 0.05) !important;
}
.stTextInput input {
    color: white !important;
    -webkit-text-fill-color: white !important;
    caret-color: white !important;
}
.stTextInput input::placeholder {
    color: rgba(255, 255, 255, 0.5) !important;
    -webkit-text-fill-color: rgba(255, 255, 255, 0.5) !important;
    opacity: 1 !important;
}

/* Buttons */
button[kind="primaryFormSubmit"], button[kind="primary"] {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.1)) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.4) !important;
    box-shadow: 0 8px 25px 0 rgba(0, 0, 0, 0.2), inset 0 2px 2px rgba(255,255,255,0.4) !important;
}
button[kind="primaryFormSubmit"]:hover, button[kind="primary"]:hover {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.2)) !important;
    box-shadow: 0 10px 30px 0 rgba(255, 255, 255, 0.3), inset 0 2px 2px rgba(255,255,255,0.5) !important;
}

/* Selectboxes */
div[data-baseweb="select"] > div {
    background-color: rgba(255, 255, 255, 0.12) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    color: white !important;
}
div[data-baseweb="select"] span {
    color: white !important;
}
div[data-testid="stVirtualDropdown"] li { color: white !important; }
div[data-testid="stVirtualDropdown"] { background-color: #0f172a !important; border: 1px solid rgba(255,255,255,0.2) !important; }
div[data-baseweb="popover"] > div { background-color: #0f172a !important; }
"""

LIGHT_CSS = """
/* Background Sync */
.stApp, [data-testid="stSidebar"] {
    background: radial-gradient(circle at 15% 50%, rgba(14, 165, 233, 0.1), transparent 50%),
                radial-gradient(circle at 85% 30%, rgba(99, 102, 241, 0.1), transparent 50%),
                radial-gradient(circle at center, #f8fafc 0%, #e2e8f0 100%) !important;
    background-color: #f8fafc !important;
    background-size: cover !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}

/* Sidebar Specific Overrides for Light Mode */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%) !important;
    box-shadow: 5px 0 30px rgba(0, 0, 0, 0.05) !important;
}

/* Typography */
.login-title, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, .stRadio label p { color: #0f172a !important; }
.input-label, [data-testid="stSidebar"] label { color: rgba(15, 23, 42, 0.9) !important; }
.stCheckbox p { color: #0f172a !important; }

/* Sidebar Radio/Navigation Text color */
[data-testid="stSidebar"] .stRadio label p {
    color: rgba(15, 23, 42, 0.8) !important;
    font-weight: 500 !important;
}

/* TextInput */
.stTextInput div[data-baseweb="input"] {
    background-color: rgba(255, 255, 255, 0.6) !important;
    border: 1px solid rgba(0, 0, 0, 0.15) !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.03), 0 4px 10px rgba(0,0,0,0.05) !important;
}
.stTextInput div[data-baseweb="input"]:focus-within {
    border: 1px solid rgba(14, 165, 233, 0.6) !important;
    background-color: rgba(255, 255, 255, 0.95) !important;
    box-shadow: 0 0 15px rgba(14, 165, 233, 0.15), inset 0 2px 4px rgba(0, 0, 0, 0.05) !important;
}
.stTextInput input {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
    caret-color: #0f172a !important;
}
.stTextInput input::placeholder {
    color: rgba(15, 23, 42, 0.5) !important;
    -webkit-text-fill-color: rgba(15, 23, 42, 0.5) !important;
    opacity: 1 !important;
}

/* Buttons */
button[kind="primaryFormSubmit"], button[kind="primary"] {
    background: linear-gradient(135deg, rgba(14, 165, 233, 0.9), rgba(99, 102, 241, 0.9)) !important;
    color: white !important;
    border: 1px solid rgba(14, 165, 233, 0.4) !important;
    box-shadow: 0 8px 25px 0 rgba(14, 165, 233, 0.25), inset 0 2px 2px rgba(255,255,255,0.2) !important;
}
button[kind="primaryFormSubmit"]:hover, button[kind="primary"]:hover {
    background: linear-gradient(135deg, rgba(56, 189, 248, 1), rgba(129, 140, 248, 1)) !important;
    box-shadow: 0 10px 30px 0 rgba(14, 165, 233, 0.35), inset 0 2px 2px rgba(255,255,255,0.3) !important;
}

/* Selectboxes */
div[data-baseweb="select"] > div {
    background-color: rgba(255, 255, 255, 0.7) !important;
    border: 1px solid rgba(0, 0, 0, 0.15) !important;
    color: #0f172a !important;
}
div[data-baseweb="select"] span {
    color: #0f172a !important;
}
div[data-testid="stVirtualDropdown"] li { color: #0f172a !important; }
div[data-testid="stVirtualDropdown"] { background-color: #f8fafc !important; border: 1px solid #e2e8f0 !important; }
div[data-baseweb="popover"] > div { background-color: #f8fafc !important; }
"""

def inject_theme_css(theme_key, is_login=False):
    """
    Injects the custom CSS for the specified theme.
    """
    css = BASE_CSS
    if is_login:
        css += LOGIN_SPECIFIC_CSS
        
    if theme_key == "theme_dark":
        css += DARK_CSS
    elif theme_key == "theme_light":
        css += LIGHT_CSS
    else:
        # System theme
        css += f"@media (prefers-color-scheme: dark) {{ {DARK_CSS} }} @media (prefers-color-scheme: light) {{ {LIGHT_CSS} }}"
        
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
