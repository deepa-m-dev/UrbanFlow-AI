import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle

from preprocess import Preprocessor

# ----------------------------
# LOAD DATASET
# ----------------------------
df = pd.read_csv("../dataset/traffic.csv")

# ----------------------------
# FEATURES
# ----------------------------
features = ["hour", "day_of_week", "vehicle_count", "weather", "accident", "road_type", "event"]

X = df[features]
y = df["congestion_level"]

# ----------------------------
# LINEAR REGRESSION
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)

print("Linear Regression Score:", lr.score(X_test, y_test))

# ----------------------------
# KMEANS CLUSTERING (USING SAME PREPROCESSOR STYLE)
# ----------------------------
pre = Preprocessor()

scaler = StandardScaler()

X_scaled = scaler.fit_transform(df[["vehicle_count", "hour", "congestion_level"]])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)

# ----------------------------
# SAVE MODELS (PRODUCTION SAFE)
# ----------------------------
pickle.dump(lr, open("../model/regression_model.pkl", "wb"))
pickle.dump(kmeans, open("../model/kmeans_model.pkl", "wb"))
pickle.dump(scaler, open("../model/scaler.pkl", "wb"))

# OPTIONAL: save processed dataset
df.to_csv("../dataset/traffic_clustered.csv", index=False)

print("🚦 UrbanFlow AI Models trained and saved successfully!")