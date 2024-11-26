import streamlit as st
import pandas as pd
import pickle
import requests
import os

# DAGsHub model URL
MODEL_URL = "https://dagshub.com/allmamun556/MLOPS_CI_CD_MONITORING/raw/main/data/model.pkl"

# Function to download the model if not already downloaded
def download_model(url, save_path="model.pkl"):
    if not os.path.exists(save_path):
        with st.spinner("Downloading model..."):
            response = requests.get(url)
            response.raise_for_status()  # Raise an error if the download fails
            with open(save_path, "wb") as f:
                f.write(response.content)
            st.success("Model downloaded successfully!")
    else:
        st.info("Model already exists locally.")

# Download the model
download_model(MODEL_URL)

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit App
st.title("Wind Power Prediction New")

# Sidebar for user input
st.sidebar.header("Input Features")
def user_input_features():
    bearing_shaft_temperature = st.sidebar.slider('Bearing Shaft Temperature (°C)', -10.0, 100.0, 50.0)
    blade1_pitch_angle = st.sidebar.slider('Blade 1 Pitch Angle (degrees)', 0.0, 90.0, 45.0)
    gearbox_oil_temperature = st.sidebar.slider('Gearbox Oil Temperature (°C)', -10.0, 120.0, 60.0)
    generator_rpm = st.sidebar.slider('Generator RPM', 0, 3000, 1500)
    generator_winding1_temperature = st.sidebar.slider('Generator Winding 1 Temperature (°C)', -10.0, 150.0, 75.0)
    hub_temperature = st.sidebar.slider('Hub Temperature (°C)', -10.0, 120.0, 60.0)
    reactive_power = st.sidebar.slider('Reactive Power (kVAR)', -500.0, 500.0, 0.0)
    wind_speed = st.sidebar.slider('Wind Speed (m/s)', 0.0, 25.0, 10.0)
    active_power_diff = st.sidebar.slider('Active Power Difference (kW)', -1000.0, 1000.0, 0.0)

    # Store the input data in a dictionary
    data = {
        'BearingShaftTemperature': bearing_shaft_temperature,
        'Blade1PitchAngle': blade1_pitch_angle,
        'GearboxOilTemperature': gearbox_oil_temperature,
        'GeneratorRPM': generator_rpm,
        'GeneratorWinding1Temperature': generator_winding1_temperature,
        'HubTemperature': hub_temperature,
        'ReactivePower': reactive_power,
        'WindSpeed': wind_speed,
        'active_power_diff': active_power_diff
    }
    
    # Convert dictionary to a pandas DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Get the user input
input_df = user_input_features()

# Main panel to show user input
st.subheader('User Input:')
st.write(input_df)

# Make prediction using the model
prediction = model.predict(input_df)

# Display the result
st.subheader('Predicted Wind Power Output (kW):')
st.write(prediction[0])
