name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  pipeline:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install dvc[s3]  # Install DVC with the required remote (e.g., s3 or dagshub)

    # Set up DVC (for DagsHub storage)
    - name: Set up DVC
      run: |
        # Configure DVC remote to use DagsHub as storage
        dvc remote add origin s3://dvc
        dvc remote modify origin endpointurl https://dagshub.com/allmamun556/MLOPS_CI_CD_MONITORING.s3
        dvc remote modify origin --local access_key_id ${{ secrets.DVC_ACCESS_KEY_ID }}
        dvc remote modify origin --local secret_access_key ${{ secrets.DVC_SECRET_ACCESS_KEY }}

    # Pull data from DVC remote (DagsHub)
    - name: Pull data from DVC remote
      run: |
        dvc pull -r origin  # Pull data from the configured remote (DagsHub)    

    - name: Run Data Loader
      run: python src/data_loader.py

    - name: Run Preprocessing
      run: python src/preprocessing.py

    - name: Train Model
      run: python src/train.py

    - name: Evaluate Model
      run: python src/evalute_model.py

    # Save model output to DVC (if necessary)
    - name: Git Config
      run: |
        git config user.name allmamun556
        git config user.email allmamun556@gmail.com

    - name: Add model to DVC
      run: |
        dvc add data  # Add the trained model to DVC tracking
        git add data.dvc
        git commit -m "Add trained model"
    
    # Push model and data to DVC remote (DagsHub)
    - name: Push data and model to DVC remote
      run: |
        dvc push -r origin  # Push data and model to the configured remote (DagsHub)  
