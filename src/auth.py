import streamlit as st
import time
from src.i18n import t, LANGUAGES, DEFAULT_LANGUAGE
from src.db import init_admin, add_user, get_user, update_password
from src.security import hash_password, verify_password

# Initialize database and seed default admin on app startup
init_admin()


def check_password():
    """Returns True if the user is authenticated."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    return st.session_state.authenticated


def get_role():
    """Return the current user's role ('admin' | 'staff' | None)."""
    return st.session_state.get("role", None)


def is_admin():
    return get_role() == "admin"


def logout():
    """Clears authentication state and reruns the app."""
    for key in ("authenticated", "role", "username", "failed_attempts"):
        st.session_state.pop(key, None)
    st.rerun()


def render_login_page():
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANGUAGE
        
    if "failed_attempts" not in st.session_state:
        st.session_state.failed_attempts = 0

    if "login_theme" not in st.session_state:
        st.session_state.login_theme = "theme_system"

    lang = st.session_state.lang
    current_theme = st.session_state.login_theme

    BASE_CSS = """
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
        top: 20px !important;
        right: 20px !important;
        z-index: 99999 !important;
        display: flex;
        gap: 15px;
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
        width: 100% !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        padding: 10px !important;
        margin-top: 30px !important;
        min-height: 50px !important;
        height: 50px !important;
        margin-bottom: 0 !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    button[kind="primaryFormSubmit"]:hover, button[kind="primary"]:hover {
        transform: translateY(-3px);
    }
    
    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
    }

    /* Target columns for top controls */
    div[data-testid="column"] {
        width: 150px !important;
        min-width: 130px !important;
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

    DARK_CSS = """
    /* Background */
    .stApp {
        background: radial-gradient(circle at 15% 50%, rgba(14, 165, 233, 0.15), transparent 50%),
                    radial-gradient(circle at 85% 30%, rgba(99, 102, 241, 0.15), transparent 50%),
                    radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
        background-color: #020617 !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }

    /* Typography */
    .login-title { color: white; }
    .input-label { color: rgba(255, 255, 255, 0.9); }
    .stCheckbox p { color: white !important; }

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

    /* Selectboxes top */
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
    
    /* Popover/Dropdown overrides */
    div[data-baseweb="popover"] > div {
        background-color: #0f172a !important;
    }
    """

    LIGHT_CSS = """
    /* Background */
    .stApp {
        background: radial-gradient(circle at 15% 50%, rgba(14, 165, 233, 0.1), transparent 50%),
                    radial-gradient(circle at 85% 30%, rgba(99, 102, 241, 0.1), transparent 50%),
                    radial-gradient(circle at center, #f8fafc 0%, #e2e8f0 100%) !important;
        background-color: #f8fafc !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }

    /* Typography */
    .login-title { color: #0f172a; }
    .input-label { color: rgba(15, 23, 42, 0.9); }
    .stCheckbox p { color: #0f172a !important; }

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

    /* Selectboxes top */
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
    
    /* Popover/Dropdown overrides */
    div[data-baseweb="popover"] > div {
        background-color: #f8fafc !important;
    }
    """

    if current_theme == "theme_dark":
        injected_css = BASE_CSS + DARK_CSS
    elif current_theme == "theme_light":
        injected_css = BASE_CSS + LIGHT_CSS
    else:
        injected_css = BASE_CSS + f"@media (prefers-color-scheme: dark) {{ {DARK_CSS} }} @media (prefers-color-scheme: light) {{ {LIGHT_CSS} }}"

    st.markdown(f"<style>{injected_css}</style>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # Top Controls (Language & Theme Selectors)
    # -------------------------------------------------------------------------
    lang_info = {
        "UZ": {"flag": "🇺🇿", "name": "O'zbek"},
        "RU": {"flag": "🇷🇺", "name": "Русский"},
        "EN": {"flag": "🇺🇸", "name": "English"}
    }

    theme_options = {
        "theme_system": {"icon": "💻"},
        "theme_dark": {"icon": "🌙"},
        "theme_light": {"icon": "☀️"}
    }

    st.markdown('<div class="top-controls-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        selected_theme = st.selectbox(
            "Theme",
            options=list(theme_options.keys()),
            format_func=lambda x: f"{theme_options[x]['icon']} {t(x, lang)}",
            index=list(theme_options.keys()).index(current_theme),
            label_visibility="collapsed",
            key="login_theme_selector"
        )
        
    with col2:
        selected_lang = st.selectbox(
            "Language",
            options=list(LANGUAGES.keys()),
            format_func=lambda x: f"{lang_info[x]['flag']} {x}",
            index=list(LANGUAGES.keys()).index(lang),
            label_visibility="collapsed",
            key="login_language_selector"
        )
    st.markdown('</div>', unsafe_allow_html=True)

    if selected_lang != lang:
        st.session_state.lang = selected_lang
        st.rerun()

    if selected_theme != current_theme:
        st.session_state.login_theme = selected_theme
        st.rerun()

    # -------------------------------------------------------------------------
    # Unified Login (Admin & Staff)
    # -------------------------------------------------------------------------
    st.markdown('<div class="login-title">Login</div>', unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        st.markdown(f'<div class="input-label">{t("auth_username", lang)}</div>', unsafe_allow_html=True)
        username = st.text_input("Username", label_visibility="collapsed")

        st.markdown(f'<div class="input-label">{t("auth_password", lang)}</div>', unsafe_allow_html=True)
        password = st.text_input("Password", type="password", label_visibility="collapsed")

        st.markdown('<br>', unsafe_allow_html=True)
        submit_login = st.form_submit_button(t("auth_login_btn", lang), type="primary", use_container_width=True)

        if submit_login:
            if username and password:
                row = get_user(username)
                if row and verify_password(row["password_hash"], password):
                    st.session_state.authenticated = True
                    st.session_state.role = row["role"]
                    st.session_state.username = username
                    st.session_state.failed_attempts = 0  # reset on success
                    st.rerun()
                else:
                    st.session_state.failed_attempts += 1
                    if st.session_state.failed_attempts >= 3:
                        st.error(f"{t('auth_invalid_credentials', lang)} {t('auth_contact_admin', lang)}")
                    else:
                        st.error(t("auth_invalid_credentials", lang))
            else:
                st.error(t("auth_error", lang))
