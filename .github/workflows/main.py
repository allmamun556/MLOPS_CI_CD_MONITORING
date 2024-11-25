name: Deploy to the Hugging Faces Hub

on:
  push:
    branches: [main]

  # to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  sync-to-hub:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          lfs: true
 

      # Remove large files to prevent push errors
      - name: Install dependencies
        run: |
          pip install pandas  # Install pandas if not in requirements.txt

      - name: Run unit tests
        run: |
          python -m unittest discover tests  # Runs all tests in the "test" directory    

      - name: Remove large files
        run: |
          git rm --cached Turbine_Data.csv || true
          echo "Turbine_Data.csv" >> .gitignore
          git add .gitignore
          git commit -m "Exclude large files from push" || true

      - name: Push to Hugging Face Hub

        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: git push --force https://mamunds:$HF_TOKEN@huggingface.co/spaces/mamunds/mlops main