---
title: Your App Title
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
---

# CML Report Workflow

This `cml.yml` file is a GitHub Actions workflow designed to automate machine learning reporting with Continuous Machine Learning (CML). Triggered on push events, it sets up an environment with Python and DVC for dependency management and data versioning. It pulls data from a DVC remote (e.g., DagsHub), executes an ML training Jupyter notebook, generates a metrics report, and posts the results as a comment on the relevant pull request. The workflow uses secrets for secure integration with remote storage and MLflow tracking, ensuring seamless model development and reporting.



# CI/CD Pipeline

This `pipeline.yml` is a GitHub Actions workflow to automate CI/CD for machine learning projects. It triggers on pushes or pull requests to the `main` branch, setting up Python (3.8), installing dependencies, and configuring DVC for remote storage with DagsHub. The workflow automates data loading, preprocessing, model training, evaluation, and versioning by pushing the trained model and data to DVC remote storage, ensuring efficient and reproducible ML workflows.


# Sync to Hugging Face Hub

This `main.yml` is a GitHub Actions workflow designed to synchronize a repository with the Hugging Face Hub. Triggered by pushes to the `master` branch or manually via the Actions tab, it checks out the repository with Git LFS enabled and securely pushes changes to the Hugging Face Hub using a personal access token stored as a GitHub secret (`HF_TOKEN`). This workflow ensures seamless integration and updates to the Hugging Face platform.

# ML Model Monitoring with Streamlit

This `ml_monitoring.py` script demonstrates how to use the `Evidently AI` library with a Streamlit application to monitor the performance of a machine learning model. It provides tools to assess data stability and detect data drift using turbine data.

## Key Features
- **Data Preparation**: Loads and preprocesses turbine data, splitting it into reference and current datasets for comparison.
- **Data Stability Test**: Generates an interactive report on data stability using Evidently's `DataStabilityTestPreset`.
- **Data Drift Report**: Creates a detailed report to identify potential data drift using Evidently's `DataDriftPreset`.
- **Streamlit Integration**: Provides an intuitive web interface with buttons to view generated reports directly in the browser.

## How to Use
1. Install the necessary dependencies: `pip install streamlit evidently pandas`.
2. Place your turbine data in the `data/Turbine_Data.csv` file path.
3. Run the script with `streamlit run ml_monitoring.py`.
4. Use the app to view either the data stability or data drift report.

This script is ideal for real-time monitoring of ML models, ensuring data quality and detecting drift for robust deployments.

# Wind Power Prediction App

This `app.py` script is a Streamlit-based web application for predicting wind power output using a pre-trained Random Forest model. The app provides an intuitive interface for users to input relevant features and view predictions in real-time.

## Key Features
- **Interactive User Input**: A sidebar allows users to input key features such as bearing shaft temperature, blade pitch angle, wind speed, and more through sliders.
- **Machine Learning Model**: Utilizes a pre-trained Random Forest Regressor (`random_forest_model.pkl`) to predict wind power output.
- **Real-Time Predictions**: Displays the predicted wind power output (in kW) based on user-provided inputs.

## How to Use
1. Install dependencies: `pip install streamlit pandas scikit-learn`.
2. Place the pre-trained model file (`random_forest_model.pkl`) in the same directory as the script.
3. Run the app using `streamlit run app.py`.
4. Use the sidebar sliders to input feature values, and view the prediction in the main panel.

This application is ideal for demonstrating wind power prediction models in a user-friendly and interactive way.
# Machine Learning Training Notebook

This notebook provides a comprehensive workflow for training, evaluating, and tracking machine learning models on turbine data. It includes data preprocessing, feature engineering, model training, evaluation, and integrated experiment tracking with MLflow.

## Key Features
- **Data Preprocessing**: Handles missing values, performs feature engineering, and ensures data quality through outlier detection and stationarity checks.
- **Feature Engineering**: Includes transformations like differencing and scaling for time series and sequential data.
- **Model Training**: Implements multiple models, including:
  - Traditional models: Linear Regression, Random Forest, Decision Tree, Polynomial Regression, and ARIMA.
  - Advanced models: RNN, LSTM, CNN, and Gradient Boosting.
- **Evaluation Metrics**: Evaluates models using metrics like MAE, MSE, RMSE, and R², with detailed logs for model performance.
- **Experiment Tracking with MLflow**: Logs model parameters, metrics, and performance results to MLflow, enabling organized experiment tracking and reproducibility.
- **Visualization**: Correlation matrices, histograms, and box plots provide insights into data distributions and relationships.

## How to Use
1. Install required libraries: `pip install -r requirements.txt` and ensure MLflow is configured (`pip install mlflow`).
2. Place the turbine dataset (`data/Turbine_Data.csv`) in the expected directory.
3. Run the notebook to preprocess data, train models, and evaluate their performance.
4. MLflow will automatically log parameters and metrics for each model, which can be visualized using the MLflow tracking UI.
5. Review metrics, visualizations, and MLflow logs to compare model effectiveness.

This notebook serves as a robust foundation for experimenting with and deploying machine learning models, with the added benefit of experiment tracking using MLflow.




