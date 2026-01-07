"""
Model training module for the Loan Approval Prediction application.
"""
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline

from . import config
from .data_loader import load_and_split
from .preprocessing import create_preprocessor, get_feature_names_after_preprocessing
from .utils import setup_logging, save_metadata, get_current_timestamp

logger = setup_logging(__name__)


def create_models() -> dict[str, Pipeline]:
    """
    Create candidate models with preprocessing pipeline.
    
    Returns:
        Dictionary of model name -> Pipeline
    """
    preprocessor = create_preprocessor()
    
    models = {
        "LogisticRegression": Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(**config.LOGISTIC_REGRESSION_PARAMS)),
        ]),
        "RandomForest": Pipeline([
            ("preprocessor", create_preprocessor()),  # Each pipeline needs its own preprocessor
            ("classifier", RandomForestClassifier(**config.RANDOM_FOREST_PARAMS)),
        ]),
    }
    
    return models


def select_best_model(
    models: dict[str, Pipeline],
    X_train,
    y_train
) -> tuple[str, Pipeline, dict[str, float]]:
    """
    Select best model using cross-validation.
    
    Args:
        models: Dictionary of model name -> Pipeline
        X_train: Training features
        y_train: Training target
        
    Returns:
        Tuple of (best model name, best pipeline, cv scores dict)
    """
    cv_results = {}
    
    for name, pipeline in models.items():
        logger.info(f"Evaluating {name} with {config.CV_FOLDS}-fold CV...")
        
        scores = cross_val_score(
            pipeline, X_train, y_train,
            cv=config.CV_FOLDS,
            scoring="accuracy",
            n_jobs=-1
        )
        
        mean_score = scores.mean()
        std_score = scores.std()
        
        cv_results[name] = {
            "mean_accuracy": mean_score,
            "std_accuracy": std_score,
            "cv_scores": scores.tolist(),
        }
        
        logger.info(f"  {name}: {mean_score:.4f} (+/- {std_score:.4f})")
    
    # Select best model
    best_name = max(cv_results, key=lambda k: cv_results[k]["mean_accuracy"])
    best_pipeline = models[best_name]
    
    logger.info(f"Best model: {best_name}")
    
    return best_name, best_pipeline, cv_results


def train_model(save: bool = True) -> tuple[Pipeline, dict]:
    """
    Train the best model and optionally save to disk.
    
    Args:
        save: Whether to save the trained model to disk
        
    Returns:
        Tuple of (trained pipeline, metadata dict)
    """
    logger.info("=" * 50)
    logger.info("Starting model training")
    logger.info("=" * 50)
    
    # Load and split data
    X_train, X_test, y_train, y_test = load_and_split()
    
    # Create models
    models = create_models()
    
    # Select best model via cross-validation
    best_name, best_pipeline, cv_results = select_best_model(models, X_train, y_train)
    
    # Fit best model on full training set
    logger.info(f"Training {best_name} on full training set...")
    best_pipeline.fit(X_train, y_train)
    
    # Calculate test score
    test_score = best_pipeline.score(X_test, y_test)
    logger.info(f"Test accuracy: {test_score:.4f}")
    
    # Get feature names after preprocessing
    try:
        feature_names = get_feature_names_after_preprocessing(
            best_pipeline.named_steps["preprocessor"]
        )
    except Exception as e:
        logger.warning(f"Could not get feature names: {e}")
        feature_names = []
    
    # Build metadata
    metadata = {
        "model_name": best_name,
        "training_date": get_current_timestamp(),
        "dataset_shape": {
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "n_features": len(config.FEATURE_COLUMNS),
        },
        "feature_columns": config.FEATURE_COLUMNS,
        "feature_names_transformed": feature_names,
        "cv_results": cv_results,
        "test_accuracy": test_score,
        "random_state": config.RANDOM_STATE,
    }
    
    if save:
        # Save model
        config.MODELS_DIR.mkdir(parents=True, exist_ok=True)
        joblib.dump(best_pipeline, config.MODEL_PATH)
        logger.info(f"Model saved to {config.MODEL_PATH}")
        
        # Save metadata
        save_metadata(metadata)
        logger.info(f"Metadata saved to {config.METADATA_PATH}")
    
    logger.info("Training complete!")
    
    return best_pipeline, metadata


def main():
    """Main entry point for training."""
    train_model(save=True)


if __name__ == "__main__":
    main()
