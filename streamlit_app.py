import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def set_bg(image_url):
    bg_style = f"""
    <style>
    .stApp {{
        background: url("{image_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

set_bg("https://wallpapers.com/images/high/car-pattern-1200-x-1200-wallpaper-yrqs5nd5ve1nutu0.webp")

#
#https://wallpapers.com/images/high/car-logo-2880-x-1800-wallpaper-z1bexjkukwg2vai1.webp

# Streamlit app
st.title("Used Car Value Predictor")

# Input features for prediction
st.header("Enter Car Specifications")

# Categorical feature mappings
city_map = {"Banglore": 0, "Chennai": 1, "Delhi": 2, "Hyderabad": 3, "Jaipur": 4, "kolkata": 5}
fuel_type_map = {"Petrol": 0, "Diesel": 1, "Electric": 2, "Hybrid": 3}
ownership_map = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth or More": 3}
transmission_map = {"Manual": 0, "Automatic": 1}

# Inputs
city = st.selectbox("City", options=city_map.keys())
oem = st.text_input("OEM (Manufacturer)", placeholder="Enter manufacturer name")
model_name = st.text_input("Model", placeholder="Enter car model")
model_year = st.number_input("Year of Manufacture", min_value=2000, max_value=2025, step=1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500, value=10000)
fuel_type = st.selectbox("Fuel Type", options=fuel_type_map.keys())
ownership = st.selectbox("Ownership Type", options=ownership_map.keys())
transmission = st.selectbox("Transmission Type", options=transmission_map.keys())
max_power = st.number_input("Max Power (in BHP)", min_value=50, step=1)
engine_type = st.text_input("Engine Type", placeholder="Enter engine type")
mileage = st.number_input("Mileage (in km/l)", min_value=0.0, step=0.1)
seating_capacity = st.number_input("Seating Capacity", min_value=2, max_value=10, step=1)
engine_displacement = st.number_input("Engine Displacement (in cc)", min_value=500, step=50)
body_type = st.text_input("Body Type", placeholder="Enter body type (e.g., Sedan, SUV)")
acceleration = st.number_input("Acceleration (0-100 km/h in seconds)", min_value=1.0, step=0.1)

# Preprocess the input
def preprocess_input(features):
    return np.array(features).reshape(1, -1)

# Collect all inputs
try:
    input_features = [
        city_map[city],            
        len(oem),                  
        len(model_name),           
        model_year, 
        kms_driven, 
        fuel_type_map[fuel_type],  
        ownership_map[ownership],  
        transmission_map[transmission],  
        max_power,
        len(engine_type),         
        mileage,
        seating_capacity,
        engine_displacement,
        len(body_type),            
        acceleration
    ]

    # Predict button
    if st.button("Predict Resale Value"):
        input_data = preprocess_input(input_features)
        prediction = model.predict(input_data)
        st.success(f"The predicted resale value of the car is: ₹{prediction[0]:,.2f}")

except Exception as e:
    st.error(f"Error: {e}")
