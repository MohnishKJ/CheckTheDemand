#imports
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load trained model safely using absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "tourism_demand_model.pkl")

model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["arrival_date_month"],
        data["stays_in_weekend_nights"],
        data["stays_in_week_nights"],
        data["travel_type"],
        data["children"],
        data["budget_category"],
        data["destination_type"]
    ]])

    prediction = model.predict(features)[0]

    result = "High Demand" if int(prediction) == 0 else "Low Demand"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
