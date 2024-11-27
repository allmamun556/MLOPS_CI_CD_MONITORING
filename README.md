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

# MLOPS_CI_CD_MONITORING
# Second
# Data Link
# https://www.kaggle.com/code/pedrorichena/modeling-wind-power-forecasting

# Continuous Machine Learning Workflow (`cml.yml`)

This repository includes a GitHub Actions workflow file (`cml.yml`) to automate ML workflows using Continuous Machine Learning (CML). 

## Workflow Overview
The `cml.yml` file performs the following tasks:
- **Environment Setup**:
  - Runs on `ubuntu-latest`.
  - Checks out the repository and sets up Python (`3.x`) with necessary dependencies.
  - Installs and configures DVC for remote storage (e.g., DagsHub with S3 support).
- **Data Management**:
  - Pulls data from the DVC remote and validates the dataset structure (e.g., columns in the CSV file).
- **Model Training and Reporting**:
  - Executes a Jupyter notebook for ML training and logs model metrics.
  - Generates a CML report with key metrics and posts it as a comment on the relevant pull request.

## Secrets
The workflow uses the following GitHub Secrets:
- `DVC_ACCESS_KEY_ID` and `DVC_SECRET_ACCESS_KEY` for accessing DVC remote storage.
- `MLFLOW_TRACKING_USERNAME` and `MLFLOW_TRACKING_PASSWORD` for MLflow tracking.
- `GITHUB_TOKEN` for authentication during report generation.

## How to Use
1. Place the `cml.yml` file in `.github/workflows/` within your repository.
2. Ensure the required secrets are added to your repository settings.
3. Push changes to trigger the workflow and automate your ML tasks.

