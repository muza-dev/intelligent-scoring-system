import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src import config
from src.i18n import t, DEFAULT_LANGUAGE

def get_lang():
    """Get current language from session state."""
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANGUAGE
    return st.session_state.lang

def load_data():
    """Load training data from the configured path."""
    if not config.TRAIN_DATA_PATH.exists():
        return None
    return pd.read_csv(config.TRAIN_DATA_PATH)

def render_eda_page():
    """Render the Exploratory Data Analysis page."""
    lang = get_lang()
    
    st.title(t("eda_title", lang))
    st.markdown(t("eda_subtitle", lang))

    df = load_data()

    if df is None:
        st.error(f"{t('data_not_found', lang)}\n`{config.TRAIN_DATA_PATH}`")
        return

    # Sidebar Filters (local to this page)
    show_raw = st.checkbox(t("show_raw_data", lang), False)

    # 1. Dataset Overview
    st.header(t("dataset_overview", lang))
    col1, col2, col3 = st.columns(3)
    col1.metric(t("rows", lang), df.shape[0])
    col2.metric(t("columns", lang), df.shape[1])
    col3.metric(t("missing_values", lang), df.isna().sum().sum())

    if show_raw:
        st.subheader(t("raw_data_sample", lang))
        st.dataframe(df.head())

    st.markdown("---")

    # 2. Target Distribution
    st.header(t("target_dist", lang))
    
    fig_target, ax_target = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Loan_Status', data=df, palette='viridis', ax=ax_target)
    ax_target.set_title(t("approval_counts", lang))
    st.pyplot(fig_target)

    st.markdown("---")

    # 3. Categorical Distributions
    st.header(t("categorical_vars", lang))
    
    # Create mapping of translated names to internal names
    cat_options = {t(col, lang): col for col in config.CATEGORICAL_FEATURES}
    
    # Add a unique key to prevent duplicate ID errors if page is re-rendered
    selected_cat_label = st.selectbox(t("select_cat", lang), list(cat_options.keys()), key="eda_cat_select")
    selected_cat = cat_options[selected_cat_label]

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(t("distribution_of", lang, feature=selected_cat_label))
        fig_cat, ax_cat = plt.subplots()
        sns.countplot(x=selected_cat, data=df, palette='pastel', ax=ax_cat)
        plt.xticks(rotation=45)
        st.pyplot(fig_cat)

    with col2:
        st.subheader(t("vs_loan_status", lang, feature=selected_cat_label))
        fig_cat_hue, ax_cat_hue = plt.subplots()
        sns.countplot(x=selected_cat, hue='Loan_Status', data=df, palette='viridis', ax=ax_cat_hue)
        plt.xticks(rotation=45)
        st.pyplot(fig_cat_hue)

    st.markdown("---")

    # 4. Numerical Distributions
    st.header(t("numerical_vars", lang))
    
    # Create mapping of translated names to internal names
    num_options = {t(col, lang): col for col in config.NUMERIC_FEATURES}
    
    selected_num_label = st.selectbox(t("select_num", lang), list(num_options.keys()), key="eda_num_select")
    selected_num = num_options[selected_num_label]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(t("distribution_of", lang, feature=selected_num_label))
        fig_num, ax_num = plt.subplots()
        sns.histplot(df[selected_num].dropna(), kde=True, ax=ax_num)
        st.pyplot(fig_num)

    with col2:
        st.subheader(t("by_loan_status", lang, feature=selected_num_label))
        fig_box, ax_box = plt.subplots()
        sns.boxplot(x='Loan_Status', y=selected_num, data=df, ax=ax_box)
        st.pyplot(fig_box)

    st.markdown("---")

    # 5. Correlation Matrix
    st.header(t("correlation_heatmap", lang))
    
    # Select only numeric
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    if not numeric_df.empty:
        fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax_corr)
        st.pyplot(fig_corr)
    else:
        st.info(t("no_numeric_corr", lang))
