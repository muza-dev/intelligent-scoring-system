import streamlit as st
import time
from src.i18n import t, LANGUAGES, DEFAULT_LANGUAGE
from src.db import init_admin, add_user, get_user, update_password
from src.security import hash_password, verify_password

# Initialize database and seed default admin on app startup
init_admin()


TIMEOUT_SECONDS = 10 * 60  # 10 minutes inactivity timeout

def check_password():
    """Returns True if the user is authenticated."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        
    if st.session_state.authenticated:
        now = time.time()
        # Default to now if not set so the first check passes
        last_activity = st.session_state.get("last_activity", now)
        
        if now - last_activity > TIMEOUT_SECONDS:
            # Session expired
            st.session_state.timeout_occurred = True
            logout()
            return False
            
        # Update last activity on every meaningful interaction/rerun
        st.session_state.last_activity = now
        
    return st.session_state.authenticated


def get_role():
    """Return the current user's role ('admin' | 'staff' | None)."""
    return st.session_state.get("role", None)


def is_admin():
    return get_role() == "admin"


def logout():
    """Clears authentication state and reruns the app."""
    for key in ("authenticated", "role", "username", "failed_attempts", "last_activity"):
        st.session_state.pop(key, None)
    st.rerun()


from .utils import inject_theme_css

def render_login_page():
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANGUAGE
        
    if "failed_attempts" not in st.session_state:
        st.session_state.failed_attempts = 0

    if "theme" not in st.session_state:
        st.session_state.theme = "theme_system"

    lang = st.session_state.lang
    current_theme = st.session_state.theme

    # Global Theme Injection
    inject_theme_css(current_theme, is_login=True)

    # -------------------------------------------------------------------------
    # Top Controls (Language & Theme Selectors)
    # -------------------------------------------------------------------------
    lang_info = {
        "UZ": {"flag": "🇺🇿", "name": "O'zbek"},
        "RU": {"flag": "🇷🇺", "name": "Русский"},
        "EN": {"flag": "🇺🇸", "name": "English"}
    }

    theme_options = {
        "theme_system": {"icon": "💻 "},
        "theme_dark": {"icon": "🌙 "},
        "theme_light": {"icon": "☀️ "}
    }

    st.markdown('<div class="top-controls-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="small")
    
    with col1:
        selected_lang = st.selectbox(
            "Language",
            options=list(LANGUAGES.keys()),
            format_func=lambda x: f"{lang_info[x]['flag']} {x}",
            index=list(LANGUAGES.keys()).index(lang),
            label_visibility="collapsed",
            key="login_language_selector"
        )
        
    with col2:
        selected_theme = st.selectbox(
            "Theme",
            options=list(theme_options.keys()),
            format_func=lambda x: f"{theme_options[x]['icon']} {t(x, lang)}",
            index=list(theme_options.keys()).index(current_theme),
            label_visibility="collapsed",
            key="login_theme_selector"
        )
    st.markdown('</div>', unsafe_allow_html=True)

    if selected_lang != lang:
        st.session_state.lang = selected_lang
        st.rerun()

    if selected_theme != current_theme:
        st.session_state.theme = selected_theme
        st.rerun()

    # -------------------------------------------------------------------------
    # Unified Login (Admin & Staff)
    # -------------------------------------------------------------------------
    st.markdown('<div class="login-title">Login</div>', unsafe_allow_html=True)

    if st.session_state.get("timeout_occurred"):
        st.warning(t("auth_timeout", lang), icon="⏱️")
        st.session_state.timeout_occurred = False

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
                    st.session_state.full_name = row["full_name"]
                    st.session_state.failed_attempts = 0  # reset on success
                    st.rerun()
                else:
                    st.session_state.failed_attempts += 1
                    if st.session_state.failed_attempts >= 3:
                        st.error(t('auth_invalid_credentials', lang))
                    else:
                        st.error(t("auth_invalid_credentials", lang))
            else:
                st.error(t("auth_error", lang))
