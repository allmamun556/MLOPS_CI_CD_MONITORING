# .github/workflows/cml.yaml
name: CML Report
permissions:
  id-token: write
  contents: write
on: [push]

jobs:
  run:
    runs-on: ubuntu-latest
    #container: docker://ghcr.io/iterative/cml:0-dvc2-base1
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - uses: iterative/setup-cml@v1
      #- uses: iterative/setup-dvc@v1

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
        
      - name: Check Data Columns
        run: |
          python -c "import pandas as pd; data = pd.read_csv('data/Turbine_Data.csv'); print(data.columns)" 

      - name: 'Create CML report'
        env:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          MLFLOW_TRACKING_USERNAME: ${{ secrets.MLFLOW_TRACKING_USERNAME }}
          MLFLOW_TRACKING_PASSWORD: ${{ secrets.MLFLOW_TRACKING_PASSWORD }}
        
          #PYTHONUNBUFFERED: 1 
          
        run: |
          jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 ml_training_notebook.ipynb

          echo "## Model Metrics" > report.md
          cat metrics.txt >> report.md

          cml-send-comment report.md
          
          # echo "## Model Metrics" > report.md
          # cat metrics.txt >> report.md

          # cml-send-comment report.md

