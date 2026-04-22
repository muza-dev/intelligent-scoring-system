"""
Model training module for the Intelligent Scoring application.
"""
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.kernel_approximation import Nystroem
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.base import BaseEstimator, ClassifierMixin

from . import config
from .data_loader import load_and_split
from .preprocessing import create_preprocessor, get_feature_names_after_preprocessing
from .utils import setup_logging, save_metadata, get_current_timestamp, _make_serializable

logger = setup_logging(__name__)


from .custom_models import RBFNetworkClassifier


def create_models() -> dict[str, Pipeline]:
    """
    Create candidate models with preprocessing pipeline.
    
    Returns:
        Dictionary of model name -> Pipeline
    """
    preprocessor = create_preprocessor()
    
    # Exact base learners definition from requirements
    base_learners = [
        ('lr',  LogisticRegression(max_iter=1000, C=1.0)),
        ('rf',  RandomForestClassifier(n_estimators=100, max_depth=10)),
        ('svm', SVC(probability=True, kernel='rbf')),
        ('mlp', MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500)),
        ('rbf', RBFNetworkClassifier(gamma='scale'))
    ]
    
    ensemble_soft = VotingClassifier(
        estimators=base_learners,
        voting='soft',
        weights=config.ENSEMBLE_SOFT_WEIGHTS
    )

    # Re-use pipelines to ensure preprocessor runs before everything
    # We provide the base models in pipelines as well to evaluate their individual performance
    models = {
        "LogisticRegression": Pipeline([
            ("preprocessor", create_preprocessor()),
            ("classifier", LogisticRegression(max_iter=1000, C=1.0)),
        ]),
        "RandomForest": Pipeline([
            ("preprocessor", create_preprocessor()),
            ("classifier", RandomForestClassifier(n_estimators=100, max_depth=10)),
        ]),
        "SVM": Pipeline([
            ("preprocessor", create_preprocessor()),
            ("classifier", SVC(probability=True, kernel='rbf')),
        ]),
        "MLP": Pipeline([
            ("preprocessor", create_preprocessor()),
            ("classifier", MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500)),
        ]),
        "RBFNetwork": Pipeline([
            ("preprocessor", create_preprocessor()),
            ("classifier", RBFNetworkClassifier(gamma='scale')),
        ]),
        "EnsembleSoft": Pipeline([
            ("preprocessor", create_preprocessor()),
            ("classifier", ensemble_soft),
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
    Train ALL candidate models, save each individually, and update the registry.
    The model with the best CV score is marked as active (unless admin already set one).

    Returns:
        Tuple of (best pipeline, best model metadata dict)
    """
    logger.info("=" * 50)
    logger.info("Starting model training — all models")
    logger.info("=" * 50)

    # Load and split data
    X_train, X_test, y_train, y_test = load_and_split()

    # Create all candidate models
    models = create_models()

    # Run CV to rank them (doesn't fit fully yet)
    best_name, _, cv_results = select_best_model(models, X_train, y_train)

    if save:
        config.MODELS_DIR.mkdir(parents=True, exist_ok=True)

    trained_pipelines: dict[str, Pipeline] = {}
    metadata_all: dict[str, dict] = {}

    for name, pipeline in models.items():
        logger.info(f"Fitting {name} on full training set...")
        pipeline.fit(X_train, y_train)
        test_score = pipeline.score(X_test, y_test)
        logger.info(f"  {name} test accuracy: {test_score:.4f}")

        try:
            feature_names = get_feature_names_after_preprocessing(
                pipeline.named_steps["preprocessor"]
            )
        except Exception as e:
            logger.warning(f"Could not get feature names for {name}: {e}")
            feature_names = []

        meta = {
            "model_name": name,
            "training_date": get_current_timestamp(),
            "dataset_shape": {
                "train_samples": len(X_train),
                "test_samples": len(X_test),
                "n_features": len(config.FEATURE_COLUMNS),
            },
            "feature_columns": config.FEATURE_COLUMNS,
            "feature_names_transformed": feature_names,
            "cv_mean_accuracy": cv_results.get(name, {}).get("mean_accuracy", 0),
            "cv_std_accuracy": cv_results.get(name, {}).get("std_accuracy", 0),
            "cv_results": cv_results.get(name, {}),
            "test_accuracy": test_score,
            "random_state": config.RANDOM_STATE,
        }

        trained_pipelines[name] = pipeline
        metadata_all[name] = meta

        if save:
            model_path = config.MODEL_PATHS.get(name)
            if model_path:
                joblib.dump(pipeline, model_path)
                logger.info(f"  Saved {name} → {model_path}")

    if save:
        from .utils import load_registry, save_registry
        registry = load_registry()

        # Preserve the admin's active choice if it still exists
        current_active = registry.get("active")
        registry["models"] = _make_serializable(metadata_all)
        if current_active not in metadata_all:
            registry["active"] = best_name  # default to CV winner
        save_registry(registry)
        logger.info(f"Registry updated — active model: {registry['active']}")

        # Legacy: also save the best model as loan_model.joblib
        joblib.dump(trained_pipelines[best_name], config.MODEL_PATH)
        save_metadata(metadata_all[best_name])

    logger.info("Training complete!")
    return trained_pipelines[best_name], metadata_all[best_name]



def main():
    """Main entry point for training."""
    train_model(save=True)


if __name__ == "__main__":
    main()
