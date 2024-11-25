import pandas as pd

def load_and_clean_data(file_path: str, output_path: str) -> pd.DataFrame:
    """
    Load and clean the turbine data, renaming columns and handling initial setup.
    
    Args:
        file_path (str): Path to the raw CSV file.
        output_path (str): Path to save the cleaned data.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df = pd.read_csv(file_path)
    df.rename(columns={'Unnamed: 0': 'Time'}, inplace=True)
   
    df.to_csv(output_path, index=False)
    print(f"Data cleaned and saved to {output_path}.")
    return df

if __name__ == "__main__":
    load_and_clean_data("data/Turbine_Data.csv", "data/cleaned_data.csv")