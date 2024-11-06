import streamlit as st
import pandas as pd
from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import tempfile

# Load the data and prepare the reference and current datasets
@st.cache_data
def load_and_prepare_data():
    # Load your data
    turbine_data = pd.read_csv("data/Turbine_Data.csv")
    # Rename the column 'Unnamed: 0' to 'Time'
    turbine_data.rename(columns={'Unnamed: 0': 'Time'}, inplace=True)
    turbine_data.drop(columns=['ControlBoxTemperature', 'WTG'], inplace=True)
    turbine_data = turbine_data[turbine_data.drop(columns='Time').notna().sum(axis=1) > 0]
    turbine_data.drop(columns=['Blade1PitchAngle','Blade2PitchAngle', 'Blade3PitchAngle'], inplace=True)

    # Splitting the data into reference and current halves
    mid_point = len(turbine_data) // 2
    reference_data = turbine_data.iloc[:mid_point]
    current_data = turbine_data.iloc[mid_point:]

    # Sample the data to reduce computation time
    sample_size = 1000
    reference_data = reference_data.sample(n=min(sample_size, len(reference_data)), random_state=42)
    current_data = current_data.sample(n=min(sample_size, len(current_data)), random_state=42)

    return reference_data, current_data

# Generate and save data stability test to HTML
def save_data_stability_test(reference_data, current_data):
    data_stability_test = TestSuite(tests=[DataStabilityTestPreset()])
    data_stability_test.run(current_data=current_data, reference_data=reference_data, column_mapping=None)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmpfile:
        data_stability_test.save_html(tmpfile.name)
        return tmpfile.name

# Generate and save data drift report to HTML
def save_data_drift_report(reference_data, current_data):
    data_drift_report = Report(metrics=[DataDriftPreset()])
    data_drift_report.run(current_data=current_data, reference_data=reference_data, column_mapping=None)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmpfile:
        data_drift_report.save_html(tmpfile.name)
        return tmpfile.name

# Streamlit application layout
st.title("Turbine Data Quality and Drift Monitoring")

# Load and prepare the data
reference_data, current_data = load_and_prepare_data()

# Create two buttons for the user to choose the report they want to view
if st.button("Show Data Stability Report"):
    st.subheader("Data Stability Report")
    stability_report_path = save_data_stability_test(reference_data, current_data)
    with open(stability_report_path, "r") as f:
        st.components.v1.html(f.read(), height=1000, width=1920, scrolling=True)

if st.button("Show Data Drift Report"):
    st.subheader("Data Drift Report")
    drift_report_path = save_data_drift_report(reference_data, current_data)
    with open(drift_report_path, "r") as f:
        st.components.v1.html(f.read(), height=1000, width=1920, scrolling=True)
