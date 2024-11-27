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



