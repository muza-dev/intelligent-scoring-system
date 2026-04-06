"""
Streamlit application for Intelligent Scoring.

Multi-page app with:
- Train & Metrics: Train model, view metrics, confusion matrix, ROC curve
- Single Prediction: Form input, predict approval + probability, show explanation
- Batch Prediction: Upload CSV, download results
- About: Dataset info, limitations, ethical notes

Supports: English, Uzbek, Russian

Run with: streamlit run main.py
"""
import sys
from pathlib import Path

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

import base64
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src import config
from src.utils import (
    setup_logging, model_exists, load_metadata,
    load_registry, set_active_model, get_active_model_key,
    inject_theme_css,
)
from src.predict import load_model, predict_single, predict_batch
from src.explain import get_aggregated_feature_importance, plot_feature_importance
from src.eda import render_eda_page
from src.i18n import LANGUAGES, DEFAULT_LANGUAGE, t
from src.auth import check_password, render_login_page, logout, get_role

logger = setup_logging("streamlit_app")

# =============================================================================
# Page Configuration
# =============================================================================
st.set_page_config(
    page_title="Intelligent Scoring",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

def get_base64_of_bin_file(bin_file):
    """
    Reads a binary file and returns its base64 encoded string.
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_sidebar_background(png_file):
    """
    Sets the sidebar background image using CSS.
    """
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set sidebar background
try:
    set_sidebar_background(PROJECT_ROOT / "assets/sidebar_bg.png")
except Exception:
    pass  # Fail silently if image not found

# =============================================================================
# Language State
# =============================================================================
if "lang" not in st.session_state:
    st.session_state.lang = DEFAULT_LANGUAGE


def get_lang() -> str:
    """Get current language from session state."""
    return st.session_state.lang


# =============================================================================
# Caching
# =============================================================================
@st.cache_resource
def get_model(model_key: str = ""):
    """Load and cache a model by key. Pass empty string to load the active model."""
    if not model_exists():
        return None
    return load_model(model_key if model_key else None)


@st.cache_data
def get_cached_metadata(model_key: str = ""):
    """Load and cache metadata for the given model key (empty = active model)."""
    try:
        return load_metadata(model_key if model_key else None)
    except (FileNotFoundError, Exception):
        return None


def clear_model_cache():
    """Clear cached model and metadata."""
    get_model.clear()
    get_cached_metadata.clear()
    get_cached_evaluation.clear()
    get_cached_feature_importance.clear()


@st.cache_data(show_spinner=False)
def get_cached_evaluation(model_key: str = ""):
    """
    Run evaluate_model() for the given model key and cache the result.
    Pass empty string to evaluate whichever model is currently active.
    """
    from src.evaluate import evaluate_model
    model = get_model(model_key)
    if model is None:
        return None
    return evaluate_model(model)


@st.cache_data(show_spinner=False)
def get_cached_feature_importance(model_key: str = ""):
    """
    Run get_aggregated_feature_importance() for the given model key and cache the result.
    Pass empty string to use the currently active model.
    """
    from src.explain import get_aggregated_feature_importance
    model = get_model(model_key)
    if model is None:
        return None
    return get_aggregated_feature_importance(model=model)



# =============================================================================
# Welcome Page
# =============================================================================
def render_welcome_page():
    """Render a welcoming landing page with instructions."""
    lang = get_lang()
    role = get_role()
    display_name = st.session_state.get("full_name", "User").title()
    
    st.title("👋 " + t("nav_welcome", lang))
    
    st.markdown(f"### {t('welcome_header', lang).format(name=display_name)}")
    
    st.markdown("---")
    
    # Feature highlights in sidebar order
    if role == "admin":
        st.markdown(f"_{t('welcome_admin_intro', lang)}_")
        
        # 1. Train & Metrics
        with st.container():
            st.subheader("📊 1. " + t("nav_train", lang))
            st.write(t("train_desc_short", lang))
            
        # 2. EDA
        with st.container():
            st.subheader("📈 2. " + t("nav_eda", lang))
            st.write(t("eda_desc_short", lang))
            
        # 3. Single Prediction
        with st.container():
            st.subheader("🔮 3. " + t("nav_single", lang))
            st.write(t("enter_details", lang))
            
        # 4. Batch Prediction
        with st.container():
            st.subheader("📁 4. " + t("nav_batch", lang))
            st.write(t("batch_description", lang))
            
        # 5. User Management
        with st.container():
            st.subheader("👥 5. " + t("nav_user_mgmt", lang))
            st.write(t("user_mgmt_desc_short", lang))
            
        # 6. About
        with st.container():
            st.subheader("ℹ️ 6. " + t("nav_about", lang))
            st.write(t("about_description", lang))

    else:
        # Bank Staff view (Prediction focused)
        st.markdown(f"#### {t('welcome_instructions', lang)}")
        
        # 1. Single Prediction
        with st.container():
            st.subheader("🔮 1. " + t("nav_single", lang))
            st.write(t("enter_details", lang))
            
        # 2. Batch Prediction
        with st.container():
            st.subheader("📁 2. " + t("nav_batch", lang))
            st.write(t("batch_description", lang))
    
    st.markdown("---")
    if role == "admin":
        st.caption(t("admin_dashboard_caption", lang))
    else:
        st.caption(t("welcome_contact_admin", lang))


# =============================================================================
# Sidebar Navigation
# =============================================================================
def render_sidebar():
    """Render the sidebar navigation (role-aware)."""
    lang = get_lang()
    role = get_role()

    st.sidebar.title(t("app_title", lang))
    
    # Selectors row
    col1, col2 = st.sidebar.columns([1, 1], gap="small")
    
    with col1:
        selected_lang = st.selectbox(
            t("language", lang),
            options=list(LANGUAGES.keys()),
            format_func=lambda x: LANGUAGES[x],
            index=list(LANGUAGES.keys()).index(lang),
            key="language_selector",
            label_visibility="collapsed" if role == "staff" else "visible"
        )
        
    with col2:
        theme_options = {
            "theme_system": "💻",
            "theme_dark": "🌙",
            "theme_light": "☀️"
        }
        current_theme = st.session_state.get("theme", "theme_system")
        selected_theme = st.selectbox(
            t("theme", lang),
            options=list(theme_options.keys()),
            format_func=lambda x: f"{theme_options[x]} {t(x, lang).split()[0]}",  # Use first word — unique across all languages
            index=list(theme_options.keys()).index(current_theme),
            key="dashboard_theme_selector",
            label_visibility="collapsed" if role == "staff" else "visible"
        )

    if selected_lang != lang:
        st.session_state.lang = selected_lang
        st.rerun()
        
    if selected_theme != current_theme:
        st.session_state.theme = selected_theme
        st.rerun()

    st.sidebar.markdown("---")

    # Role badge
    if role == "admin":
        st.sidebar.markdown(
            '<span style="background:#6c3483;color:white;padding:3px 10px;'
            'border-radius:12px;font-size:12px;font-weight:700;">🔐 Admin</span>',
            unsafe_allow_html=True
        )
        nav_options = [
            t("nav_welcome", lang),
            t("nav_train", lang),
            t("nav_eda", lang),
            t("nav_single", lang),
            t("nav_batch", lang),
            t("nav_user_mgmt", lang),
            t("nav_about", lang),
        ]
    else:
        st.sidebar.markdown(
            '<span style="background:#1a5276;color:white;padding:3px 10px;'
            'border-radius:12px;font-size:12px;font-weight:700;">🏦 Bank Staff</span>',
            unsafe_allow_html=True
        )
        nav_options = [
            t("nav_welcome", lang),
            t("nav_single", lang),
            t("nav_batch", lang),
        ]

    st.sidebar.markdown("")
    page = st.sidebar.radio(
        "Navigation",
        nav_options,
        index=0,
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")

    # Model status
    if role == "admin":
        registry = load_registry()
        trained_models = registry.get("models", {})
        active_key = registry.get("active")

        if trained_models:
            # Selectbox to switch active model
            model_keys = list(trained_models.keys())
            current_idx = model_keys.index(active_key) if active_key in model_keys else 0
            chosen = st.sidebar.selectbox(
                "🤖 Active Model",
                model_keys,
                index=current_idx,
                key="active_model_selector",
                format_func=lambda k: f"{k} ({trained_models[k].get('test_accuracy', 0):.2%})"
            )
            if chosen != active_key:
                set_active_model(chosen)
                get_model.clear()
                get_cached_metadata.clear()
                st.rerun()

            active_key = get_active_model_key()
            meta = get_cached_metadata(active_key or "")
            if meta:
                st.sidebar.success(t("model_trained", lang))
                st.sidebar.caption(f"{t('accuracy', lang)}: {meta.get('test_accuracy', 0):.2%}")
        else:
            st.sidebar.warning(t("no_model", lang))
        st.sidebar.markdown("---")

    if st.sidebar.button(t("logout", lang), use_container_width=True):
        logout()

    return page


# =============================================================================
# Page: Train & Metrics
# =============================================================================
def render_train_page():
    """Render the training and metrics page."""
    lang = get_lang()
    
    st.title(t("train_title", lang))
    
    # Check for data
    data_exists = config.TRAIN_DATA_PATH.exists()
    
    if not data_exists:
        st.error(
            f"{t('data_not_found', lang)}\n\n"
            f"{t('download_prompt', lang)}\n"
            f"`{config.RAW_DATA_DIR}/`"
        )
        st.info(
            f"{t('download_link', lang)}"
            "[Kaggle Loan Prediction Dataset]"
            "(https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)"
        )
        return
    
    # Training section
    st.header(t("model_training", lang))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if st.button(t("train_button", lang), type="primary", use_container_width=True):
            with st.spinner(t("training_progress", lang)):
                try:
                    from src.train import train_model
                    
                    model, metadata = train_model(save=True)
                    clear_model_cache()
                    
                    st.success(t("training_success", lang))
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"{t('training_failed', lang)}{e}")
                    logger.exception("Training error")
    
    with col2:
        # Show comparison table of all trained models
        registry = load_registry()
        trained_models = registry.get("models", {})
        active_key = registry.get("active")
        if trained_models:
            import pandas as pd
            rows = []
            for mkey, mmeta in trained_models.items():
                rows.append({
                    "Model": ("✅ " if mkey == active_key else "   ") + mkey,
                    "Test Acc": f"{mmeta.get('test_accuracy', 0):.2%}",
                    "CV Acc": f"{mmeta.get('cv_mean_accuracy', 0):.2%} ± {mmeta.get('cv_std_accuracy', 0):.2%}",
                    "Trained": str(mmeta.get('training_date', ''))[:10],
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    
    # Metrics section (only if model exists)
    if not model_exists():
        st.info(t("train_prompt", lang))
        return
    
    st.markdown("---")
    st.header(t("evaluation_results", lang))
    
    # Use cached evaluation for the currently active model
    results = get_cached_evaluation(active_key or "")
    
    if results is None:
        st.error("Could not evaluate the model. Please check the logs.")
        return

    try:
        
        # Metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        metrics = results["metrics"]
        col1.metric(t("accuracy", lang), f"{metrics['accuracy']:.2%}")
        col2.metric(t("precision", lang), f"{metrics['precision']:.2%}")
        col3.metric(t("recall", lang), f"{metrics['recall']:.2%}")
        col4.metric(t("f1_score", lang), f"{metrics['f1']:.2%}")
        col5.metric(t("roc_auc", lang), f"{metrics.get('roc_auc', 0):.3f}")
        
        # Plots
        st.markdown("---")
        
        plot_col1, plot_col2 = st.columns(2)
        
        with plot_col1:
            st.subheader(t("confusion_matrix", lang))
            st.pyplot(results["confusion_matrix_fig"])
        
        with plot_col2:
            st.subheader(t("roc_curve", lang))
            st.pyplot(results["roc_curve_fig"])
        
        # Feature importance
        st.markdown("---")
        st.subheader(t("feature_importance", lang))
        
        # Use cached feature importance for the currently active model
        importance_df = get_cached_feature_importance(active_key or "")
        
        if importance_df is None or importance_df.empty:
            st.info("Feature importance is not available for this model.")
            return

        importance_col1, importance_col2 = st.columns([2, 1])
        
        with importance_col1:
            fig = plot_feature_importance(importance_df, top_n=10)
            st.pyplot(fig)
        
        with importance_col2:
            st.dataframe(
                importance_df.head(10),
                use_container_width=True,
                hide_index=True
            )
        
        plt.close("all")
        
    except Exception as e:
        st.error(f"{t('evaluation_failed', lang)}{e}")
        logger.exception("Evaluation error")


# =============================================================================
# Page: Single Prediction
# =============================================================================
def render_prediction_page():
    """Render the single prediction page."""
    lang = get_lang()   
    
    st.title(t("prediction_title", lang))
    
    # Check model exists
    if not model_exists():
        st.warning(t("no_model_warning", lang))
        if st.button(t("nav_train", lang)):
            st.rerun()
        return
    
    st.markdown(t("enter_details", lang))
    
    # Define options with translations
    gender_options = {
        "Male": t("gender_male", lang),
        "Female": t("gender_female", lang)
    }
    married_options = {
        "Yes": t("yes", lang),
        "No": t("no", lang)
    }
    education_options = {
        "Graduate": t("graduate", lang),
        "Not Graduate": t("not_graduate", lang)
    }
    self_employed_options = {
        "Yes": t("yes", lang),
        "No": t("no", lang)
    }
    property_options = {
        "Urban": t("urban", lang),
        "Rural": t("rural", lang),
        "Semiurban": t("semiurban", lang)
    }
    credit_options = {
        1.0: t("credit_good", lang),
        0.0: t("credit_bad", lang)
    }
    
    # Input form
    with st.form("prediction_form"):
        st.subheader(t("applicant_info", lang))
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            gender_display = st.selectbox(t("gender", lang), list(gender_options.values()))
            gender = [k for k, v in gender_options.items() if v == gender_display][0]
            
            married_display = st.selectbox(t("married", lang), list(married_options.values()))
            married = [k for k, v in married_options.items() if v == married_display][0]
            
            dependents = st.selectbox(t("dependents", lang), ["0", "1", "2", "3+"])
            
            education_display = st.selectbox(t("education", lang), list(education_options.values()))
            education = [k for k, v in education_options.items() if v == education_display][0]
        
        with col2:
            self_employed_display = st.selectbox(t("self_employed", lang), list(self_employed_options.values()))
            self_employed = [k for k, v in self_employed_options.items() if v == self_employed_display][0]
            
            property_display = st.selectbox(t("property_area", lang), list(property_options.values()))
            property_area = [k for k, v in property_options.items() if v == property_display][0]
            
            credit_display = st.selectbox(t("credit_history", lang), list(credit_options.values()))
            credit_history = [k for k, v in credit_options.items() if v == credit_display][0]
        
        with col3:
            applicant_income = st.number_input(
                t("applicant_income", lang),
                min_value=0,
                max_value=1000000000,
                value=5000000,
                step=100000
            )
            coapplicant_income = st.number_input(
                t("coapplicant_income", lang),
                min_value=0,
                max_value=1000000000,
                value=0,
                step=100000
            )
            loan_amount = st.number_input(
                t("loan_amount", lang),
                min_value=100000,
                max_value=5000000000,
                value=15000000,
                step=500000
            )
            loan_term = st.number_input(
                t("loan_term", lang),
                min_value=1,
                max_value=600,
                value=1,
                step=1
            )
        
        submit = st.form_submit_button(t("predict_button", lang), type="primary", use_container_width=True)
    
    if submit:
        # Build input data
        input_data = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income / 1000,
            "CoapplicantIncome": coapplicant_income / 1000,
            "LoanAmount": loan_amount / 100000,
            "Loan_Amount_Term": loan_term,
            "Credit_History": credit_history,
            "Property_Area": property_area,
        }
        
        try:
            model = get_model()
            prediction, probability, label = predict_single(input_data, model)
            
            st.markdown("---")
            st.subheader(t("prediction_result", lang))
            
            result_col1, result_col2 = st.columns(2)
            
            with result_col1:
                if prediction == 1:
                    st.success(f"## ✅ {t('approved', lang)}")
                    st.metric(t("approval_probability", lang), f"{probability:.1%}")
                else:
                    st.error(f"## ❌ {t('rejected', lang)}")
                    st.metric(t("approval_probability", lang), f"{probability:.1%}")
                
                st.caption(t("probability_note", lang))
            
            with result_col2:
                st.markdown(f"**{t('input_summary', lang)}**")
                
                # Create translated summary
                translated_summary = {
                    t("gender", lang): gender_options[gender],
                    t("married", lang): married_options[married],
                    t("dependents", lang): dependents,
                    t("education", lang): education_options[education],
                    t("self_employed", lang): self_employed_options[self_employed],
                    t("applicant_income", lang): f"{int(applicant_income):,} UZS",
                    t("coapplicant_income", lang): f"{int(coapplicant_income):,} UZS",
                    t("loan_amount", lang): f"{int(loan_amount):,} UZS",
                    t("loan_term", lang): f"{loan_term}",
                    t("credit_history", lang): credit_options[credit_history],
                    t("property_area", lang): property_options[property_area],
                }
                
                summary_df = pd.DataFrame(list(translated_summary.items()), columns=[t("feature", lang), t("value", lang)])
                st.dataframe(summary_df, use_container_width=True, hide_index=True)
            
            # Feature importance
            st.markdown("---")
            st.subheader(t("factors_title", lang))
            
            importance_df = get_aggregated_feature_importance(model)
            fig = plot_feature_importance(importance_df, top_n=8, figsize=(8, 4))
            st.pyplot(fig)
            plt.close(fig)
            
            st.caption(t("factors_note", lang))
            
        except Exception as e:
            st.error(f"{t('prediction_failed', lang)}{e}")
            logger.exception("Prediction error")


# =============================================================================
# Page: Batch Prediction
# =============================================================================
def render_batch_page():
    """Render the batch prediction page."""
    lang = get_lang()
    
    st.title(t("batch_title", lang))
    
    # Check model exists
    if not model_exists():
        st.warning(t("no_model_warning", lang))
        return
    
    st.markdown(t("batch_description", lang))
    
    # Expected columns
    with st.expander(t("expected_format", lang)):
        # We show Translated (OriginalName) so users know what's in the CSV vs what it means
        num_features_str = ", ".join([f"{t(f, lang)} ({f})" for f in config.NUMERIC_FEATURES])
        cat_features_str = ", ".join([f"{t(f, lang)} ({f})" for f in config.CATEGORICAL_FEATURES])

        st.markdown(
            f"{t('columns_info', lang)}\n"
            f"- **{t('numeric_cols', lang)}**: {num_features_str}\n"
            f"- **{t('categorical_cols', lang)}**: {cat_features_str}"
        )
        
        # Sample data
        if config.SAMPLE_INPUT_PATH.exists():
            sample_df = pd.read_csv(config.SAMPLE_INPUT_PATH)
            st.markdown(f"**{t('sample_data', lang)}**")
            st.dataframe(sample_df.head(), use_container_width=True)
            
            csv_sample = sample_df.to_csv(index=False)
            st.download_button(
                t("download_sample", lang),
                csv_sample,
                "sample_input.csv",
                "text/csv"
            )
    
    # File upload
    uploaded_file = st.file_uploader(
        t("upload_csv", lang),
        type=["csv"],
        help=t("upload_help", lang)
    )
    
    if uploaded_file is not None:
        try:
            input_df = pd.read_csv(uploaded_file)
            
            st.subheader(t("uploaded_preview", lang))
            st.dataframe(input_df.head(10), use_container_width=True)
            st.caption(f"{t('total_rows', lang)}: {len(input_df)}")
            
            # Validate columns
            missing_cols = set(config.FEATURE_COLUMNS) - set(input_df.columns)
            if missing_cols:
                st.error(f"{t('missing_columns', lang)}{missing_cols}")
                return
            
            if st.button(t("generate_predictions", lang), type="primary"):
                with st.spinner(t("generating", lang)):
                    model = get_model()
                    result_df = predict_batch(input_df, model)
                
                st.success(t("predictions_complete", lang, count=len(result_df)))
                
                # Results summary
                st.subheader(t("results_summary", lang))
                
                summary_col1, summary_col2 = st.columns(2)
                
                with summary_col1:
                    approved = result_df["Prediction"].sum()
                    rejected = len(result_df) - approved
                    
                    st.metric(t("approved", lang), f"{approved} ({approved/len(result_df)*100:.1f}%)")
                    st.metric(t("rejected", lang), f"{rejected} ({rejected/len(result_df)*100:.1f}%)")
                
                with summary_col2:
                    st.metric(t("average_probability", lang), f"{result_df['Probability'].mean():.1%}")
                    st.metric(t("total_applications", lang), len(result_df))
                
                # Results preview
                st.subheader(t("predictions_header", lang))
                st.dataframe(result_df, use_container_width=True)
                
                # Download results
                csv_result = result_df.to_csv(index=False)
                st.download_button(
                    t("download_predictions", lang),
                    csv_result,
                    "loan_predictions.csv",
                    "text/csv",
                    type="primary"
                )
                
        except Exception as e:
            st.error(f"{t('batch_error', lang)}{e}")
            logger.exception("Batch prediction error")


# =============================================================================
# Page: About
# =============================================================================
def render_about_page():
    """Render the about page."""
    lang = get_lang()
    
    st.title(t("about_title", lang))
    
    st.markdown(f"""
    ## Intelligent Scoring
    
    {t("about_description", lang)}
    
    ### {t("dataset_title", lang)}
    
    {t("dataset_source", lang)}: [Kaggle](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
    
    | {t("feature", lang)} | {t("description", lang)} |
    |---------|-------------|
    | {t("gender", lang)} | {t("gender_male", lang)} / {t("gender_female", lang)} |
    | {t("married", lang)} | {t("yes", lang)} / {t("no", lang)} |
    | {t("dependents", lang)} | 0, 1, 2, 3+ |
    | {t("education", lang)} | {t("graduate", lang)} / {t("not_graduate", lang)} |
    | {t("self_employed", lang)} | {t("yes", lang)} / {t("no", lang)} |
    | {t("applicant_income", lang)} | UZS |
    | {t("coapplicant_income", lang)} | UZS |
    | {t("loan_amount", lang)} | UZS |
    | {t("loan_term", lang)} | {t("loan_term", lang)} |
    | {t("credit_history", lang)} | 1 = {t("credit_good", lang)}, 0 = {t("credit_bad", lang)} |
    | {t("property_area", lang)} | {t("urban", lang)} / {t("rural", lang)} / {t("semiurban", lang)} |
    
    ### {t("model_section", lang)}
    
    {t("models_compared", lang)}
    - **Logistic Regression** ({t("baseline", lang)})
    - **Random Forest** ({t("strong", lang)})
    - **Support Vector Machine (SVM)** ({t("svm_desc", lang)})
    - **MLP Classifier** ({t("mlp_desc", lang)})
    - **RBF Network** ({t("rbf_desc", lang)})
    
    {t("cv_selection", lang)}
    
    ### {t("preprocessing_title", lang)}
    
    - **{t("numeric_cols", lang)}**: {t("preprocessing_numeric", lang)}
    - **{t("categorical_cols", lang)}**: {t("preprocessing_categorical", lang)}
    - {t("preprocessing_note", lang)}
    
    ---
    
    ### {t("limitations_title", lang)}
    
    1. {t("limitation_size", lang)}
    2. {t("limitation_imbalance", lang)}
    3. {t("limitation_features", lang)}
    4. {t("limitation_temporal", lang)}
    
    ---
    
    *{t("coursework_note", lang)}*
    """)
    
    # Display metadata if available
    if model_exists():
        st.markdown("---")
        st.subheader(t("current_model_info", lang))
        
        metadata = get_cached_metadata()
        if metadata:
            col1, col2 = st.columns(2)
            
            with col1:
                st.json({
                    t("meta_model_name", lang): metadata.get("model_name"),
                    t("meta_training_date", lang): metadata.get("training_date"),
                    t("meta_test_accuracy", lang): metadata.get("test_accuracy"),
                    t("meta_random_state", lang): metadata.get("random_state"),
                })
            
            with col2:
                shape = metadata.get("dataset_shape", {})
                st.json({
                    t("meta_train_samples", lang): shape.get("train_samples"),
                    t("meta_test_samples", lang): shape.get("test_samples"),
                    t("meta_n_features", lang): shape.get("n_features"),
                })


# =============================================================================
# Page: User Management (Admin only)
# =============================================================================
def render_user_management_page():
    """Admin-only page to manage bank staff accounts."""
    from src.db import get_all_staff, add_user, delete_user
    from src.security import hash_password

    lang = get_lang()

    st.title(t("user_mgmt_title", lang))
    st.markdown("---")

    # --- Staff list ---
    st.subheader(t("staff_list", lang))
    staff_rows = get_all_staff()

    if not staff_rows:
        st.info(t("no_staff", lang))
    else:
        for row in staff_rows:
            col_name, col_user, col_email, col_phone, col_date, col_del = st.columns(
                [2, 1.5, 2, 1.5, 1.5, 0.8]
            )
            col_name.write(f"**{row['full_name']}**")
            col_user.write(f"`{row['username']}`")
            col_email.write(row['email'])
            col_phone.write(row['phone_number'])
            col_date.write(str(row['created_at'])[:10])
            if col_del.button(
                t("delete_staff", lang),
                key=f"del_{row['username']}",
                type="secondary",
                use_container_width=True,
            ):
                if delete_user(row['username']):
                    st.success(t("staff_deleted", lang))
                    st.rerun()

    st.markdown("---")

    # --- Add Staff form ---
    st.subheader(t("add_staff", lang))
    with st.form("add_staff_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            new_full_name    = st.text_input(t("full_name", lang))
            new_phone        = st.text_input("Phone Number")
            new_email        = st.text_input("Email")
            new_national_id  = st.text_input("National ID / Passport No")
        with col2:
            new_address      = st.text_input("Address")
            new_income       = st.text_input("Monthly Income")
            new_uname        = st.text_input("Username")

        new_pass  = st.text_input("Password",         type="password")
        new_pass2 = st.text_input("Confirm Password", type="password")

        submitted = st.form_submit_button(t("add_staff_btn", lang), type="primary", use_container_width=True)

        if submitted:
            required = [new_full_name, new_phone, new_email, new_national_id,
                        new_address, new_income, new_uname, new_pass, new_pass2]
            if not all(required):
                st.error("Please fill in all fields.")
            elif new_pass != new_pass2:
                st.error("Passwords do not match.")
            else:
                hashed = hash_password(new_pass)
                ok = add_user(
                    new_uname, hashed, new_pass,
                    new_full_name, new_phone, new_email,
                    new_national_id, new_address, new_income,
                    role="staff"
                )
                if ok:
                    st.success(t("staff_added", lang))
                    st.rerun()
                else:
                    st.error(t("staff_username_taken", lang))


# =============================================================================
# Main Application
# =============================================================================
def main():
    """Main application entry point."""
    # Ensure theme is initialized
    if "theme" not in st.session_state:
        st.session_state.theme = "theme_system"
        
    # Inject Theme early
    inject_theme_css(st.session_state.theme)

    if not check_password():
        render_login_page()
        return

    page = render_sidebar()
    lang = get_lang()
    role = get_role()

    # ---- Admin pages (all pages) ----
    if role == "admin":
        if page == t("nav_welcome", lang):
            render_welcome_page()
        elif page == t("nav_train", lang):
            render_train_page()
        elif page == t("nav_eda", lang):
            render_eda_page()
        elif page == t("nav_single", lang):
            render_prediction_page()
        elif page == t("nav_batch", lang):
            render_batch_page()
        elif page == t("nav_user_mgmt", lang):
            render_user_management_page()
        elif page == t("nav_about", lang):
            render_about_page()

    # ---- Bank Staff pages ----
    else:
        if page == t("nav_welcome", lang):
            render_welcome_page()
        elif page == t("nav_single", lang):
            render_prediction_page()
        elif page == t("nav_batch", lang):
            render_batch_page()


if __name__ == "__main__":
    main()
