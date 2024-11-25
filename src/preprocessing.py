
import pandas as pd

def preprocess_data(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Preprocess the turbine data, handling missing values and scaling features.

    Args:
        input_path (str): Path to the cleaned data CSV file.
        output_path (str): Path to save the preprocessed data.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    df = pd.read_csv(input_path)
    df.drop(columns=['ControlBoxTemperature', 'WTG'], inplace=True)
    df = df[df.drop(columns='Time').notna().sum(axis=1) > 0]
    df.drop(columns='GeneratorWinding2Temperature', inplace=True)
    df.drop(columns='GearboxBearingTemperature', inplace=True)
    df.drop(columns='RotorRPM', inplace=True)
    df.drop(columns=['Blade2PitchAngle', 'Blade3PitchAngle'], inplace=True)

    correlation_matrix = df.drop(columns=['Time']).corr()
    correlation_limit = 0.3 
    low_correlation_vars = correlation_matrix[correlation_matrix['ActivePower'].abs() < correlation_limit].index.tolist()
    if 'ActivePower' in low_correlation_vars:
        low_correlation_vars.remove('ActivePower')  

    df.drop(columns=low_correlation_vars, inplace=True)

    df['ActivePower'].fillna(df['ActivePower'].interpolate(method='linear'), inplace=True)


    df['BearingShaftTemperature'].fillna(df['BearingShaftTemperature'].median(), inplace=True)

    df['Blade1PitchAngle'].fillna(df['Blade1PitchAngle'].median(), inplace=True)


    df['GearboxOilTemperature'].fillna(df['GearboxOilTemperature'].median(), inplace=True)

    df['GeneratorRPM'].fillna(df['GeneratorRPM'].median(), inplace=True)

    df['GeneratorWinding1Temperature'].fillna(df['GeneratorWinding1Temperature'].median(), inplace=True)


    df['HubTemperature'].fillna(df['HubTemperature'].median(), inplace=True)


    df['ReactivePower'].fillna(df['ReactivePower'].median(), inplace=True)

    df['WindSpeed'].fillna(df['WindSpeed'].median(), inplace=True)


    df.to_csv(output_path, index=False)
    print(f"Data preprocessed and saved to {output_path}.")
    return df

if __name__ == "__main__":
    preprocess_data("data/cleaned_data.csv", "data/preprocessed_data.csv")