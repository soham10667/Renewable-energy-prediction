from flask import Flask, request, jsonify
from flask_cors import CORS

# IMPORTANT: import from model_newe, and import the correct function name
from model_newe import predict_energy

app = Flask(__name__)
CORS(app)  # allow frontend (e.g. Live Server on port 5500) to call the API


@app.route("/api/health", methods=["GET"])
def health():
    """Simple health-check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.route("/api/predict", methods=["POST"])
def predict():
    """
    Accepts JSON with:

        "temperature": ...,
        "wind_speed": ...,
        "humidity": ...,
        "solar_irradiance": ...

    and returns: { "prediction": <float> }
    """
    data = request.get_json() or {}

    required = ["temperature", "wind_speed", "humidity", "solar_irradiance"]

    # Check for missing fields
    for key in required:
        if key not in data:
            return jsonify({"error": f"Missing field: {key}"}), 400

    try:
        # Convert all inputs to float
        features = {k: float(data[k]) for k in required}

        # Call your model helper in model_newe.py
        y_pred = predict_energy(features)

        return jsonify({"prediction": y_pred}), 200

    except Exception as e:
        # Catch all model / conversion errors
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run on http://127.0.0.1:5000
    app.run(debug=True, port=5000)
