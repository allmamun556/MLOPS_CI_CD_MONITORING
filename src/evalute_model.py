import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def evaluate_model(data_path: str, model_path: str):
    """
    Evaluate the trained model on the turbine data.

    Args:
        data_path (str): Path to the preprocessed data.
        model_path (str): Path to the trained model.
    """
    # Load data and model
    df = pd.read_csv(data_path)
    features = df.drop(columns=["ActivePower", "Time"])
    target = df["ActivePower"]
    model = joblib.load(model_path)
    
    # Generate predictions
    predictions = model.predict(features)
    mse = mean_squared_error(target, predictions)
    mae = mean_absolute_error(target, predictions)
    r2 = r2_score(target, predictions)
    
    print(f"Evaluation Metrics - MSE: {mse}, MAE: {mae}, R2: {r2}")

if __name__ == "__main__":
    evaluate_model("data/preprocessed_data.csv", "data/model.pkl")