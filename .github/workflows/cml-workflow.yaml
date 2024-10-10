name: Run Experiments and Generate CML Report

on:
  push:
    branches:
      - master  # Trigger workflow on pushes to the master branch 

jobs:
  run-notebook:
    runs-on: ubuntu-latest

    steps:
      # Checkout the repository
      - name: Checkout Code
        uses: actions/checkout@v2

      # Set up Python environment
      - name: Set up Python 3.8
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      # Install dependencies
      - name: Install Dependencies
        run: |
          pip install -r requirements.txt
         # pip install jupyter dvc cml mlflow
      # Run the Jupyter Notebook
      - name: Run Jupyter Notebook
        run: |
          jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 modeling-wind-power-forecasting.ipynb
      # Track experiments with MLflow on DagsHub
      # - name: Log Metrics to MLflow (DagsHub)
      #   env:
      #     MLFLOW_TRACKING_URI: https://dagshub.com/allmamun556/MLOPS_CI_CD_MONITORING.mlflow
      #     MLFLOW_TRACKING_USERNAME: ${{ secrets.DAGSHUB_USERNAME }}
      #     MLFLOW_TRACKING_PASSWORD: ${{ secrets.DAGSHUB_API_TOKEN }}
      #   run: |
      #     python evaluate_model.py  # Assuming you log metrics from this script
      # Generate CML report
      # - name: Create CML Report
      #   run: |
      #     cml pr --metrics-fmt markdown
      # Push the CML report to GitHub
      # - name: Commit and Push CML Report
      #   run: |
      #     git config --global user.name "Your Name"
      #     git config --global user.email "you@example.com"
      #     git add . && git commit -m "Auto CML Report"
      #     git push
  