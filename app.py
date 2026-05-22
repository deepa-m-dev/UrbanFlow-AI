from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
from preprocess import Preprocessor

app = Flask(__name__)
CORS(app)

# ----------------------------
# LOAD MODELS
# ----------------------------
lr_model = pickle.load(open("../model/regression_model.pkl", "rb"))
kmeans_model = pickle.load(open("../model/kmeans_model.pkl", "rb"))
scaler = pickle.load(open("../model/scaler.pkl", "rb"))

pre = Preprocessor()

# ----------------------------
# HOME ROUTE
# ----------------------------
@app.route("/")
def home():
    return "🚦 UrbanFlow AI Backend Running!"

# ----------------------------
# PREDICTION ROUTE
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    # ----------------------------
    # USE PREPROCESSOR (CLEAN PIPELINE)
    # ----------------------------
    features = pre.transform_features(data)

    # LINEAR REGRESSION PREDICTION
    congestion = lr_model.predict(features)[0]

    # ----------------------------
    # KMEANS CLUSTERING (SAFE + CONSISTENT)
    # ----------------------------
    cluster_input = np.array([[data["vehicle_count"], data["hour"], congestion]])
    cluster_scaled = scaler.transform(cluster_input)
    cluster = kmeans_model.predict(cluster_scaled)[0]

    cluster_label = {
        0: "Low Traffic 🟢",
        1: "Medium Traffic 🟡",
        2: "High Traffic 🔴"
    }

    return jsonify({
        "predicted_congestion": round(float(congestion), 2),
        "traffic_cluster": cluster_label.get(cluster, "Unknown")
    })

# ----------------------------
# RUN SERVER
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)