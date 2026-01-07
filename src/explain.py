"""
Model explanation module for the Loan Approval Prediction application.
"""
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance

from . import config
from .data_loader import load_and_split
from .preprocessing import get_feature_names_after_preprocessing
from .utils import setup_logging, model_exists

logger = setup_logging(__name__)


def load_model():
    """
    Load trained model from disk.
    
    Returns:
        Trained sklearn Pipeline
    """
    if not model_exists():
        raise FileNotFoundError(
            f"Model not found at {config.MODEL_PATH}. "
            "Please train the model first using: python -m src.train"
        )
    
    return joblib.load(config.MODEL_PATH)


def get_feature_importance(model=None, X_test=None, y_test=None) -> pd.DataFrame:
    """
    Get feature importance from the model.
    
    For tree-based models (RandomForest, GradientBoosting), uses built-in
    feature_importances_. For other models, uses permutation importance.
    
    Args:
        model: Trained pipeline. If None, loads from disk.
        X_test: Test features. If None, loads from data.
        y_test: Test labels. If None, loads from data.
        
    Returns:
        DataFrame with feature names and importance scores
    """
    if model is None:
        model = load_model()
    
    if X_test is None or y_test is None:
        _, X_test, _, y_test = load_and_split()
    
    classifier = model.named_steps["classifier"]
    preprocessor = model.named_steps["preprocessor"]
    
    # Get feature names after preprocessing
    try:
        feature_names = get_feature_names_after_preprocessing(preprocessor)
    except Exception:
        feature_names = [f"feature_{i}" for i in range(len(config.FEATURE_COLUMNS))]
    
    # Try to get built-in feature importance (tree models)
    if hasattr(classifier, "feature_importances_"):
        logger.info("Using built-in feature_importances_ from classifier")
        importances = classifier.feature_importances_
        
        # Map back to transformed feature names
        importance_df = pd.DataFrame({
            "feature": feature_names,
            "importance": importances
        })
        
    else:
        # Use permutation importance for other models
        logger.info("Using permutation importance")
        
        perm_importance = permutation_importance(
            model, X_test, y_test,
            n_repeats=10,
            random_state=config.RANDOM_STATE,
            n_jobs=-1
        )
        
        importance_df = pd.DataFrame({
            "feature": config.FEATURE_COLUMNS,
            "importance": perm_importance.importances_mean,
            "importance_std": perm_importance.importances_std
        })
    
    # Sort by importance
    importance_df = importance_df.sort_values("importance", ascending=False).reset_index(drop=True)
    
    return importance_df


def get_aggregated_feature_importance(model=None, X_test=None, y_test=None, top_n: int = None) -> pd.DataFrame:
    """
    Get feature importance aggregated by original feature (before one-hot encoding).
    
    Args:
        model: Trained pipeline
        X_test: Test features
        y_test: Test labels
        top_n: Number of top features to return. If None, returns all.
        
    Returns:
        DataFrame with original feature names and aggregated importance
    """
    raw_importance = get_feature_importance(model, X_test, y_test)
    
    # Aggregate importance by original feature name
    aggregated = {}
    
    for _, row in raw_importance.iterrows():
        feature_name = row["feature"]
        importance = row["importance"]
        
        # Extract original feature name from transformed name
        # e.g., "categorical__Gender_Male" -> "Gender"
        original_name = feature_name
        
        if "__" in feature_name:
            parts = feature_name.split("__")
            if len(parts) >= 2:
                original_name = parts[1].split("_")[0]
        
        # For numeric features: "numeric__ApplicantIncome" -> "ApplicantIncome"
        for num_feat in config.NUMERIC_FEATURES:
            if num_feat in feature_name:
                original_name = num_feat
                break
        
        # For categorical features: extract base name
        for cat_feat in config.CATEGORICAL_FEATURES:
            if cat_feat in feature_name:
                original_name = cat_feat
                break
        
        if original_name in aggregated:
            aggregated[original_name] += importance
        else:
            aggregated[original_name] = importance
    
    # Create DataFrame
    agg_df = pd.DataFrame([
        {"feature": k, "importance": v}
        for k, v in aggregated.items()
    ])
    
    agg_df = agg_df.sort_values("importance", ascending=False).reset_index(drop=True)
    
    if top_n is not None:
        agg_df = agg_df.head(top_n)
    
    return agg_df


def plot_feature_importance(importance_df: pd.DataFrame, top_n: int = 10, figsize=(10, 6)):
    """
    Create a bar plot of feature importance.
    
    Args:
        importance_df: DataFrame with feature and importance columns
        top_n: Number of top features to plot
        figsize: Figure size tuple
        
    Returns:
        Matplotlib figure
    """
    # Get top N features
    plot_df = importance_df.head(top_n).copy()
    
    # Reverse order for horizontal bar plot
    plot_df = plot_df.iloc[::-1]
    
    fig, ax = plt.subplots(figsize=figsize)
    
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(plot_df)))[::-1]
    
    bars = ax.barh(plot_df["feature"], plot_df["importance"], color=colors)
    
    ax.set_xlabel("Importance")
    ax.set_ylabel("Feature")
    ax.set_title(f"Top {top_n} Feature Importance")
    
    # Add value labels
    for bar, val in zip(bars, plot_df["importance"]):
        ax.text(
            bar.get_width() + 0.001,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.3f}",
            va="center",
            fontsize=9
        )
    
    plt.tight_layout()
    
    return fig


def explain_prediction(input_data: dict, model=None) -> dict:
    """
    Explain a single prediction by showing which features contributed most.
    
    This is a simplified explanation based on global feature importance
    and the input values.
    
    Args:
        input_data: Dictionary of feature values
        model: Trained model
        
    Returns:
        Dictionary with prediction and feature contributions
    """
    from .predict import predict_single
    
    if model is None:
        model = load_model()
    
    # Get prediction
    prediction, probability, label = predict_single(input_data, model)
    
    # Get feature importance
    importance_df = get_aggregated_feature_importance(model)
    
    # Create explanation
    explanation = {
        "prediction": prediction,
        "probability": probability,
        "label": label,
        "feature_importance": importance_df.to_dict(orient="records"),
        "input_values": input_data,
    }
    
    return explanation


def main():
    """Main entry point for explanation module."""
    logger.info("=" * 50)
    logger.info("Generating feature importance explanation")
    logger.info("=" * 50)
    
    importance = get_aggregated_feature_importance()
    
    print("\nFeature Importance (Aggregated):")
    print(importance.to_string())
    
    fig = plot_feature_importance(importance)
    plt.show()


if __name__ == "__main__":
    main()
