"""
Model evaluation module for the Loan Approval Prediction application.
"""
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve,
)

from . import config
from .data_loader import load_and_split
from .utils import setup_logging, model_exists

logger = setup_logging(__name__)


def load_model():
    """
    Load trained model from disk.
    
    Returns:
        Trained sklearn Pipeline
        
    Raises:
        FileNotFoundError: If model doesn't exist
    """
    if not model_exists():
        raise FileNotFoundError(
            f"Model not found at {config.MODEL_PATH}. "
            "Please train the model first using: python -m src.train"
        )
    
    return joblib.load(config.MODEL_PATH)


def calculate_metrics(y_true, y_pred, y_proba=None) -> dict:
    """
    Calculate classification metrics.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_proba: Predicted probabilities (optional)
        
    Returns:
        Dictionary of metric name -> value
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }
    
    if y_proba is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_proba)
    
    return metrics


def plot_confusion_matrix(y_true, y_pred, figsize=(8, 6)):
    """
    Create a confusion matrix plot.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        figsize: Figure size tuple
        
    Returns:
        Matplotlib figure
    """
    cm = confusion_matrix(y_true, y_pred)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Rejected (0)", "Approved (1)"],
        yticklabels=["Rejected (0)", "Approved (1)"],
        ax=ax
    )
    
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    
    plt.tight_layout()
    
    return fig


def plot_roc_curve(y_true, y_proba, figsize=(8, 6)):
    """
    Create a ROC curve plot.
    
    Args:
        y_true: True labels
        y_proba: Predicted probabilities for positive class
        figsize: Figure size tuple
        
    Returns:
        Matplotlib figure
    """
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    auc = roc_auc_score(y_true, y_proba)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(fpr, tpr, color="blue", lw=2, label=f"ROC curve (AUC = {auc:.3f})")
    ax.plot([0, 1], [0, 1], color="gray", lw=1, linestyle="--", label="Random")
    
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend(loc="lower right")
    
    plt.tight_layout()
    
    return fig


def evaluate_model(model=None):
    """
    Evaluate the trained model and return metrics and plots.
    
    Args:
        model: Trained model. If None, loads from disk.
        
    Returns:
        Dictionary containing metrics, confusion matrix figure, and ROC figure
    """
    logger.info("=" * 50)
    logger.info("Starting model evaluation")
    logger.info("=" * 50)
    
    # Load model if not provided
    if model is None:
        model = load_model()
    
    # Load test data
    _, X_test, _, y_test = load_and_split()
    
    # Predictions
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    metrics = calculate_metrics(y_test, y_pred, y_proba)
    
    logger.info("Evaluation Metrics:")
    for name, value in metrics.items():
        logger.info(f"  {name}: {value:.4f}")
    
    # Classification report
    report = classification_report(
        y_test, y_pred,
        target_names=["Rejected", "Approved"],
        output_dict=True
    )
    
    logger.info("\nClassification Report:")
    logger.info(classification_report(
        y_test, y_pred,
        target_names=["Rejected", "Approved"]
    ))
    
    # Create plots
    cm_fig = plot_confusion_matrix(y_test, y_pred)
    roc_fig = plot_roc_curve(y_test, y_proba)
    
    return {
        "metrics": metrics,
        "classification_report": report,
        "confusion_matrix_fig": cm_fig,
        "roc_curve_fig": roc_fig,
        "y_test": y_test,
        "y_pred": y_pred,
        "y_proba": y_proba,
    }


def main():
    """Main entry point for evaluation."""
    results = evaluate_model()
    
    # Show plots
    plt.show()


if __name__ == "__main__":
    main()
