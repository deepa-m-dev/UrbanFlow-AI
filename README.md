# 🚦 UrbanFlow AI

## Smart Traffic Intelligence System using Machine Learning

UrbanFlow AI is a full-stack machine learning project that predicts traffic congestion and analyzes urban traffic patterns using **Linear Regression** and **K-Means Clustering**. It provides real-time predictions through a Flask API and a modern web dashboard.

---

# 📌 Features

* 🚦 Predicts traffic congestion level in real-time
* 🧠 K-Means clustering for traffic pattern grouping (Low / Medium / High)
* 📊 ML-powered traffic analytics dashboard
* 🌐 Flask REST API backend
* 💻 Interactive frontend UI
* ⚡ Real-time prediction system via API
* 📦 Modular ML pipeline design

---

# 🧠 Machine Learning Approach

## 1. Linear Regression

Used to predict **traffic congestion level (%)** based on:

* Hour of day
* Day of week
* Vehicle count
* Weather conditions
* Accidents
* Road type
* Events

---

## 2. K-Means Clustering

Used to group traffic into:

* 🟢 Low Traffic
* 🟡 Medium Traffic
* 🔴 High Traffic

Based on:

* Vehicle count
* Hour
* Congestion level

---

# 🏗️ System Architecture

```text
Frontend (HTML/CSS/JS)
        ↓
Flask API (Backend)
        ↓
Preprocessing Layer
        ↓
Machine Learning Models
   ├── Linear Regression
   └── K-Means Clustering
        ↓
JSON Response → Frontend Dashboard
```

---

# 🛠️ Tech Stack

### 👨‍💻 Backend

* Python
* Flask
* Flask-CORS

### 🤖 Machine Learning

* Scikit-learn
* Pandas
* NumPy

### 🌐 Frontend

* HTML
* CSS
* JavaScript
* Chart.js

---

# 📂 Project Structure

```
urbanflow-ai/
│
├── backend/
│   ├── app.py
│   ├── train_models.py
│   ├── preprocess.py
│
├── dataset/
│   ├── traffic.csv
│   ├── traffic_clustered.csv
│
├── model/
│   ├── regression_model.pkl
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│
├── frontend/
│   ├── index.html
│
└── README.md
```

---

# 🚀 How to Run Locally

## 1. Clone the repository

```bash
git clone https://github.com/your-username/urbanflow-ai.git
cd urbanflow-ai
```

---

## 2. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 3. Train models

```bash
python backend/train_models.py
```

---

## 4. Run backend server

```bash
python backend/app.py
```

---

## 5. Run frontend

Open:

```
frontend/index.html
```

---

# 📡 API Endpoint

## Predict Traffic

**URL:**

```
POST /predict
```

**Request Body:**

```json
{
  "hour": 18,
  "day_of_week": 5,
  "vehicle_count": 1200,
  "weather": 1,
  "accident": 0,
  "road_type": 1,
  "event": 0
}
```

**Response:**

```json
{
  "predicted_congestion": 67.45,
  "traffic_cluster": "High Traffic 🔴"
}
```

---

# 📊 Output Example

* Congestion Prediction (%)
* Traffic Category (Low / Medium / High)
* Real-time insights for traffic conditions

---

# 💡 Future Improvements

* 🌍 Integration with Google Maps API
* 📡 Real-time traffic data streaming
* 🧠 Advanced ML models (Random Forest / XGBoost)
* 📱 Mobile app version
* 🚗 Route optimization system

---

# 🏆 Project Highlights

✔ Full-stack ML project
✔ Real-world problem solving
✔ API-based architecture
✔ Clean modular ML pipeline
✔ Dashboard-based visualization
✔ Deployment-ready system

---

# 👨‍💻 Author
