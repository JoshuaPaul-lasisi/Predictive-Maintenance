import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load pre-trained model (replace 'clf.pkl' with your trained model file)
import joblib
clf = joblib.load("../models/random_forest_model.pkl")

# Load dataset
data = pd.read_csv("../data/processed/condition_monitoring_data.csv")

st.title("Real-Time Condition Monitoring Dashboard")

# Input features for prediction
st.sidebar.header("Enter Sensor Data")
motor_power = st.sidebar.number_input("Motor Power", value=2411.6)
volume_flow = st.sidebar.number_input("Volume Flow", value=8.99)
pressure1 = st.sidebar.number_input("Pressure 1", value=151.47)
vibration = st.sidebar.number_input("Vibration", value=0.604)

# Create input data for prediction
input_data = pd.DataFrame([[motor_power, volume_flow, pressure1, vibration]],
                          columns=['Motor Power', 'Volume Flow 1', 'Pressure 1', 'Vibration'])

# Make prediction
prediction = clf.predict(input_data)
st.subheader("Prediction")
st.write(f"Cooler Condition: {prediction[0]}%")
