import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")
st.write("Predict house prices using Linear Regression")

st.subheader("Enter House Details")

MedInc = st.number_input("Median Income", min_value=0.0, value=3.0)
HouseAge = st.number_input("House Age", min_value=0.0, value=20.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0, value=5.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0)
Population = st.number_input("Population", min_value=0.0, value=500.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0, value=3.0)
Latitude = st.number_input("Latitude", value=35.0)
Longitude = st.number_input("Longitude", value=-120.0)

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "MedInc": [MedInc],
        "HouseAge": [HouseAge],
        "AveRooms": [AveRooms],
        "AveBedrms": [AveBedrms],
        "Population": [Population],
        "AveOccup": [AveOccup],
        "Latitude": [Latitude],
        "Longitude": [Longitude]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ${prediction[0] * 100000:,.2f}")
