import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import pickle
import plotly.graph_objects as go

# Load the trained Random Forest model (replace 'random_forest_model.pkl' with the actual model file path)
model = pickle.load(open('random_forest_model.pkl', 'rb'))

# Create a Dash application
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Wind Power Prediction App"),
    
    # Sliders for input features
    html.Div([
        html.Label("Bearing Shaft Temperature (°C)"),
        dcc.Slider(id='bearing-shaft-temperature', min=-10, max=100, step=1, value=50),
        
        html.Label("Blade 1 Pitch Angle (degrees)"),
        dcc.Slider(id='blade1-pitch-angle', min=0, max=90, step=1, value=45),
        
        html.Label("Gearbox Oil Temperature (°C)"),
        dcc.Slider(id='gearbox-oil-temperature', min=-10, max=120, step=1, value=60),
        
        html.Label("Generator RPM"),
        dcc.Slider(id='generator-rpm', min=0, max=3000, step=10, value=1500),
        
        html.Label("Generator Winding 1 Temperature (°C)"),
        dcc.Slider(id='generator-winding1-temperature', min=-10, max=150, step=1, value=75),
        
        html.Label("Hub Temperature (°C)"),
        dcc.Slider(id='hub-temperature', min=-10, max=120, step=1, value=60),
        
        html.Label("Reactive Power (kVAR)"),
        dcc.Slider(id='reactive-power', min=-500, max=500, step=1, value=0),
        
        html.Label("Wind Speed (m/s)"),
        dcc.Slider(id='wind-speed', min=0, max=25, step=0.1, value=10),
        
        html.Label("Active Power Difference (kW)"),
        dcc.Slider(id='active-power-diff', min=-1000, max=1000, step=1, value=0),
    ], style={'columnCount': 9}),
    
    # Display user input data
    html.H2("User Input:"),
    html.Div(id='user-input'),

    # Display predicted output
    html.H2("Predicted Wind Power Output (kW):"),
    html.Div(id='prediction-output'),
    
    # Graph to display the user inputs in tabular form
    dcc.Graph(id='input-graph')
])

# Define callback to update the prediction and input display
@app.callback(
    [Output('user-input', 'children'),
     Output('prediction-output', 'children'),
     Output('input-graph', 'figure')],
    [Input('bearing-shaft-temperature', 'value'),
     Input('blade1-pitch-angle', 'value'),
     Input('gearbox-oil-temperature', 'value'),
     Input('generator-rpm', 'value'),
     Input('generator-winding1-temperature', 'value'),
     Input('hub-temperature', 'value'),
     Input('reactive-power', 'value'),
     Input('wind-speed', 'value'),
     Input('active-power-diff', 'value')]
)
def update_output(bearing_shaft_temperature, blade1_pitch_angle, gearbox_oil_temperature, 
                  generator_rpm, generator_winding1_temperature, hub_temperature,
                  reactive_power, wind_speed, active_power_diff):
    
    # Store the input data in a dictionary
    data = {
        'BearingShaftTemperature': [bearing_shaft_temperature],
        'Blade1PitchAngle': [blade1_pitch_angle],
        'GearboxOilTemperature': [gearbox_oil_temperature],
        'GeneratorRPM': [generator_rpm],
        'GeneratorWinding1Temperature': [generator_winding1_temperature],
        'HubTemperature': [hub_temperature],
        'ReactivePower': [reactive_power],
        'WindSpeed': [wind_speed],
        'active_power_diff': [active_power_diff]
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame(data)

    # Make prediction using the loaded model
    prediction = model.predict(input_df)[0]

    # Generate a table-like display of user input
    input_table = html.Table([
        html.Tr([html.Th(col) for col in input_df.columns]),
        html.Tr([html.Td(input_df[col][0]) for col in input_df.columns])
    ])

    # Create a bar chart of input values for visualization
    fig = go.Figure(data=[
        go.Bar(name='Input Features', x=input_df.columns, y=input_df.iloc[0])
    ])
    
    # Update layout of the figure
    fig.update_layout(title="Input Features", yaxis_title="Value", xaxis_title="Feature")
    
    return input_table, f"{prediction:.2f} kW", fig


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
