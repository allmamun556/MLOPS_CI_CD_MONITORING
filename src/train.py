import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_model(data_path):
    # Load the preprocessed data
    data = pd.read_csv(data_path)
    
    # Define features and target
    features = data.drop(columns=['ActivePower', 'Time'])
    target = data['ActivePower']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model MSE: {mse}")
    
    # Save the trained model
    joblib.dump(model, 'data/model.pkl')

if __name__ == "__main__":
    train_model('data/preprocessed_data.csv')