import streamlit as st
import pickle
import numpy as np
import pandas as pd
from transformers import pipeline

# --------------------- Page Config ---------------------
st.set_page_config(page_title="Car Advisor AI", layout="wide")

# Background Image Styling
def set_background():
    bg_img = """
    <style>
    .stApp {
        background: url("https://wallpapercave.com/wp/wp10821254.png") no-repeat center center fixed;
        background-size: cover;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
        background: rgba(0, 0, 0, 0.6);
        padding: 10px;
        border-radius: 10px;
    }
    .subheader {
        color: white;
        font-size: 22px;
        background: rgba(0, 0, 0, 0.5);
        padding: 8px;
        border-radius: 8px;
    }
    </style>
    """
    st.markdown(bg_img, unsafe_allow_html=True)

set_background()

# --------------------- Load Models & Data ---------------------

@st.cache_data
def load_car_data():
    return pd.read_csv("cars_data.csv")  # Load car dataset

df = load_car_data()

with open("model.pkl", "rb") as file:
    model = pickle.load(file)  # Load trained ML model

# --------------------- Categorical Mappings ---------------------
city_map = {"Banglore": 0, "Chennai": 1, "Delhi": 2, "Hyderabad": 3, "Jaipur": 4, "Kolkata": 5}
fuel_type_map = {"Petrol": 0, "Diesel": 1, "Electric": 2, "Hybrid": 3}
ownership_map = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth or More": 3}
transmission_map = {"Manual": 0, "Automatic": 1}

# --------------------- Car Price Prediction UI ---------------------
st.markdown('<h1 class="title">🚗 Car Resale Value Predictor & AI Advisor</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">🔍 Predict Your Car’s Resale Value</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    city = st.selectbox("📍 City", options=city_map.keys())
    oem = st.text_input("🏭 OEM (Manufacturer)", placeholder="Enter manufacturer name")
    model_name = st.text_input("🚘 Model", placeholder="Enter car model")
    model_year = st.number_input("📅 Year of Manufacture", min_value=2000, max_value=2025, step=1)
    kms_driven = st.number_input("🚗 Kilometers Driven", min_value=0, step=500, value=10000)

with col2:
    fuel_type = st.selectbox("⛽ Fuel Type", options=fuel_type_map.keys())
    ownership = st.selectbox("👤 Ownership Type", options=ownership_map.keys())
    transmission = st.selectbox("🛞 Transmission Type", options=transmission_map.keys())
    max_power = st.number_input("⚡ Max Power (BHP)", min_value=50, step=1)
    mileage = st.number_input("🛣️ Mileage (km/l)", min_value=0.0, step=0.1)

seating_capacity = st.number_input("🪑 Seating Capacity", min_value=2, max_value=10, step=1)
engine_displacement = st.number_input("🔧 Engine Displacement (cc)", min_value=500, step=50)
body_type = st.text_input("🚙 Body Type (e.g., Sedan, SUV)", placeholder="Enter body type")
engine_type = st.text_input("🛠️ Engine Type", placeholder="Enter engine type")
acceleration = st.number_input("🏎️ Acceleration (0-100 km/h in seconds)", min_value=1.0, step=0.1)

# --------------------- Feature Preprocessing ---------------------
def preprocess_input(features):
    return np.array(features).reshape(1, -1)

if st.button("🔮 Predict Resale Value"):
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
        mileage,  
        seating_capacity,  
        engine_displacement,  
        len(body_type),  
        len(engine_type),  
        acceleration  
    ]

    input_data = preprocess_input(input_features)
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Resale Value: ₹{prediction[0]:,.2f}")


# --------------------- Car Recommendation ---------------------
st.markdown('<h2 class="subheader">🎯 Find Your Perfect Car</h2>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    budget = st.number_input("💰 Your Budget (₹)", min_value=100000, step=50000)

with col4:
    fuel_type_map = {"Petrol": 0, "Diesel": 1, "Electric": 2, "Hybrid": 3}
    transmission_map = {"Manual": 0, "Automatic": 1}
    fuel_pref = st.selectbox("⛽ Preferred Fuel", fuel_type_map.keys())
    transmission_pref = st.selectbox("🛞 Preferred Transmission", transmission_map.keys())

def recommend_car(budget, fuel, transmission):
    filtered_cars = df[
        (df["price"] <= budget) &
        (df["Fuel Type"].str.lower() == fuel.lower()) &
        (df["Transmission"].str.lower() == transmission.lower())
    ]
    if not filtered_cars.empty:
        recommended = filtered_cars.sample(1).to_dict(orient="records")[0]
        return f"**🚗 {recommended['model']}**\n\n💰 Price: ₹{recommended['price']:,.2f}\n⛽ Fuel: {recommended['Fuel Type']}\n🛞 Transmission: {recommended['Transmission']}\n🪑 Seats: {recommended['Seating_Capacity']} seats"
    else:
        return "No suitable car found! Try adjusting your budget or preferences."

# --------------------- AI Chatbot ---------------------
st.sidebar.title("💬 AI Car Advisor")

if "show_chat" not in st.session_state:
    st.session_state["show_chat"] = False

if st.sidebar.button("🤖 Open Chat"):
    st.session_state["show_chat"] = not st.session_state.get("show_chat", False)

if st.session_state.get("show_chat", False):
    with st.sidebar:
        st.subheader("💡 Ask Me Anything!")
        
        # Loading the GPT-2 model
        @st.cache_resource
        def load_ai_model():
            return pipeline("text-generation", model="gpt2", device=-1)  # Use -1 for CPU

        chatbot = load_ai_model()

        if "chat_messages" not in st.session_state:
            st.session_state["chat_messages"] = []

        for msg in st.session_state["chat_messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_input = st.chat_input("Ask me about cars or tell me your budget!")

        if user_input:
            st.session_state["chat_messages"].append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Check if the input contains the word "budget"
            if "budget" in user_input.lower():
                try:
                    # Extract the number from the user's input (e.g., "my budget is 500000")
                    budget = int([word for word in user_input.split() if word.isdigit()][0])
                    fuel_pref = 'Petrol'  # Default or user can also specify
                    transmission_pref = 'Automatic'  # Default or user can also specify
                    response = recommend_car(budget, fuel_pref, transmission_pref)
                except Exception as e:
                    response = "Sorry, I couldn't understand your budget."

            else:
                # Use GPT-2 for general conversation if no budget-related query
                response = chatbot(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]

            st.session_state["chat_messages"].append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

# --------------------- Car Recommendation Section ---------------------
if st.button("🚀 Find Best Car"):
    result = recommend_car(budget, fuel_pref, transmission_pref)
    st.success(result)