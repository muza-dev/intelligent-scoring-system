"""
Prediction module for the Intelligent Scoring application.
"""
import argparse
import joblib
import pandas as pd
import numpy as np

from . import config
from .utils import setup_logging, model_exists

logger = setup_logging(__name__)


def load_model(model_key: str | None = None):
    """
    Load a trained model from disk.

    Args:
        model_key: Registry key e.g. 'RandomForest'. If None, loads the active model.

    Returns:
        Trained sklearn Pipeline

    Raises:
        FileNotFoundError: If model doesn't exist
    """
    from .utils import get_active_model_key

    key = model_key or get_active_model_key()

    if key and key in config.MODEL_PATHS:
        path = config.MODEL_PATHS[key]
        if path.exists():
            logger.info(f"Loading model '{key}' from {path}")
            return joblib.load(path)

    # Legacy fallback
    if not model_exists():
        raise FileNotFoundError(
            "No trained model found. Please train the model first."
        )
    logger.info(f"Loading legacy model from {config.MODEL_PATH}")
    return joblib.load(config.MODEL_PATH)


def predict_single(input_data: dict, model=None) -> tuple[int, float, str, str]:
    """
    Make a prediction for a single applicant.
    
    Args:
        input_data: Dictionary of feature name -> value
        model: Trained model. If None, loads from disk.
        
    Returns:
        Tuple of (prediction, probability, label)
    """
    if model is None:
        model = load_model()
    
    # Create DataFrame from input
    df = pd.DataFrame([input_data])
    
    # Ensure columns are in correct order
    df = df.reindex(columns=config.FEATURE_COLUMNS)
    
    # Make prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0, 1] if hasattr(model, "predict_proba") else float(prediction)
    
    label = "Approved" if prediction == 1 else "Rejected"
    
    confidence_level = "Standard"
    
    # Human-in-the-Loop Disagreement Detection
    if hasattr(model, "named_steps") and "classifier" in model.named_steps and "preprocessor" in model.named_steps:
        clf = model.named_steps["classifier"]
        preprocessor = model.named_steps["preprocessor"]
        from sklearn.ensemble import VotingClassifier
        
        if isinstance(clf, VotingClassifier):
            try:
                X_trans = preprocessor.transform(df)
                base_preds = [est.predict(X_trans)[0] for est in clf.estimators_]
                num_approve = sum(1 for p in base_preds if p == 1)
                
                if num_approve == len(base_preds) or num_approve == 0:
                    confidence_level = "High Confidence"
                else:
                    confidence_level = "Edge Case / Manual Review Required"
            except Exception as e:
                logger.warning(f"Could not compute confidence bounds: {e}")

    logger.info(f"Prediction: {label} (probability: {probability:.4f}, confidence: {confidence_level})")
    
    return int(prediction), float(probability), label, confidence_level


def predict_batch(df: pd.DataFrame, model=None) -> pd.DataFrame:
    """
    Make predictions for a batch of applicants.
    
    Args:
        df: DataFrame with applicant features
        model: Trained model. If None, loads from disk.
        
    Returns:
        DataFrame with original data plus prediction columns
    """
    if model is None:
        model = load_model()
    
    # Keep original data
    result_df = df.copy()
    
    # Ensure only feature columns are used for prediction
    feature_df = df.reindex(columns=config.FEATURE_COLUMNS)
    
    # Make predictions
    predictions = model.predict(feature_df)
    probabilities = model.predict_proba(feature_df)[:, 1] if hasattr(model, "predict_proba") else predictions
    
    # Add prediction columns
    result_df["Prediction"] = predictions
    result_df["Probability"] = probabilities
    result_df["Status"] = np.where(predictions == 1, "Approved", "Rejected")
    
    # Human-in-the-Loop Disagreement Detection
    confidence_levels = ["Standard"] * len(df)
    if hasattr(model, "named_steps") and "classifier" in model.named_steps and "preprocessor" in model.named_steps:
        clf = model.named_steps["classifier"]
        preprocessor = model.named_steps["preprocessor"]
        from sklearn.ensemble import VotingClassifier
        
        if isinstance(clf, VotingClassifier):
            try:
                X_trans = preprocessor.transform(feature_df)
                all_base_preds = np.array([est.predict(X_trans) for est in clf.estimators_]).T
                
                for idx, preds in enumerate(all_base_preds):
                    num_approve = np.sum(preds == 1)
                    if num_approve == len(preds) or num_approve == 0:
                        confidence_levels[idx] = "High Confidence"
                    else:
                        confidence_levels[idx] = "Edge Case / Manual Review Required"
            except Exception as e:
                logger.warning(f"Could not compute confidence bounds for batch: {e}")
                
    result_df["Confidence Level"] = confidence_levels
    
    logger.info(f"Batch prediction complete: {len(df)} samples")
    logger.info(f"  Approved: {sum(predictions)} ({sum(predictions)/len(df)*100:.1f}%)")
    logger.info(f"  Rejected: {len(predictions) - sum(predictions)} ({(len(predictions) - sum(predictions))/len(df)*100:.1f}%)")
    logger.info(f"  Edge Cases: {sum(1 for c in confidence_levels if 'Edge' in c)}")
    
    return result_df


def smoke_test():
    """
    Run a smoke test with hardcoded example data.
    
    Returns:
        True if test passes, raises exception otherwise
    """
    logger.info("=" * 50)
    logger.info("Running smoke test...")
    logger.info("=" * 50)
    
    # Hardcoded test example
    test_input = {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "1",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 5849,
        "CoapplicantIncome": 0,
        "LoanAmount": 128,
        "Loan_Amount_Term": 360,
        "Credit_History": 1.0,
        "Property_Area": "Urban",
    }
    
    logger.info("Test input:")
    for key, value in test_input.items():
        logger.info(f"  {key}: {value}")
    
    try:
        prediction, probability, label, confidence = predict_single(test_input)
        
        logger.info(f"\nResult: {label}")
        logger.info(f"Probability of approval: {probability:.4f}")
        logger.info(f"Confidence Level: {confidence}")
        logger.info("\n✓ Smoke test PASSED!")
        
        return True
        
    except Exception as e:
        logger.error(f"\n✗ Smoke test FAILED: {e}")
        raise


def main():
    """Main entry point for prediction module."""
    parser = argparse.ArgumentParser(description="Intelligent Scoring")
    parser.add_argument(
        "--smoke-test",
        action="store_true",
        help="Run smoke test with hardcoded example"
    )
    parser.add_argument(
        "--input-file",
        type=str,
        help="Path to CSV file for batch prediction"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        help="Path to save predictions CSV"
    )
    
    args = parser.parse_args()
    
    if args.smoke_test:
        smoke_test()
    elif args.input_file:
        df = pd.read_csv(args.input_file)
        result = predict_batch(df)
        
        if args.output_file:
            result.to_csv(args.output_file, index=False)
            logger.info(f"Predictions saved to {args.output_file}")
        else:
            print(result.to_string())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
