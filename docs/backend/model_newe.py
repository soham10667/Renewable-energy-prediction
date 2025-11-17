import os
import pickle as pkl
import numpy as np


# Base directory of this file (backend/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# IMPORTANT: match the actual filenames exactly as shown in VS Code
MODEL_PATH = os.path.join(BASE_DIR, "Linear_Regression_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Load model and scaler once when the module is imported
with open(MODEL_PATH, "rb") as f:
    model = pkl.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pkl.load(f)


def predict_energy(features_dict: dict) -> float:
    """
    features_dict is filled by app.py from the frontend:

        {
            "temperature": ...,
            "wind_speed": ...,
            "humidity": ...,
            "solar_irradiance": ...
        }

    The remaining features are set to 0.0.
    """

    # Order of features must match the order used during training
    # Example: [Feature_1, Feature_2, ..., Feature_10]
    # Map frontend inputs into the first four features
    feature_vector = [
        float(features_dict["temperature"]),       # Feature_1
        float(features_dict["wind_speed"]),        # Feature_2
        float(features_dict["humidity"]),          # Feature_3
        float(features_dict["solar_irradiance"]),  # Feature_4
        0.0,  # Feature_5
        0.0,  # Feature_6
        0.0,  # Feature_7
        0.0,  # Feature_8
        0.0,  # Feature_9
        0.0,  # Feature_10
    ]

    X = np.array(feature_vector, dtype=float).reshape(1, -1)

    # If scaler is a StandardScaler/MinMaxScaler etc.
    X_scaled = scaler.transform(X)

    y_pred = model.predict(X_scaled)[0]
    return float(y_pred)
