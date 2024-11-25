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
        with:
          lfs: true  # This ensures that Git LFS files are downloaded

      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - uses: iterative/setup-cml@v1
      #- uses: iterative/setup-dvc@v1

       # Install dependencies
      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Check Data Columns
        run: |
          python -c "import pandas as pd; data = pd.read_csv('data/Turbine_Data.csv'); print(data.columns)"    
          
      - name: 'Create CML report'
        env:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
        
          #PYTHONUNBUFFERED: 1 
          
        run: |
          jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 notebooks/ml_training_notebook.ipynb

          echo "## Model Metrics" > report.md
          cat notebooks/metrics.txt >> report.md

          cml-send-comment report.md
          
          # echo "## Model Metrics" > report.md
          # cat notebooks/metrics.txt >> report.md

          # cml-send-comment report.md

