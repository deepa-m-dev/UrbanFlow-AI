import numpy as np
from sklearn.preprocessing import StandardScaler

class Preprocessor:

    def __init__(self):
        # You can reuse scaler later if needed
        self.scaler = StandardScaler()

    # ----------------------------
    # USED FOR LINEAR REGRESSION / API INPUT
    # ----------------------------
    def transform_features(self, data):
        """
        Converts JSON input into model-ready numpy array
        Ensures same order everywhere (VERY IMPORTANT)
        """

        return np.array([[
            data["hour"],
            data["day_of_week"],
            data["vehicle_count"],
            data["weather"],
            data["accident"],
            data["road_type"],
            data["event"]
        ]])

    # ----------------------------
    # USED FOR KMEANS CLUSTERING
    # ----------------------------
    def scale_for_clustering(self, df):
        """
        Standard scaling for clustering features
        """
        cols = ["vehicle_count", "hour", "congestion_level"]
        return self.scaler.fit_transform(df[cols])