import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

# Load trained model
model = pk.load(open('car-price.model', 'rb'))

st.header("Car Price Prediction App")

# User inputs
year = st.slider('Car Manufactured Year', 1990, 2024, key='year')
fuel = st.selectbox('Fuel Type', ['Diesel', 'Petrol'], key='fuel_type')
max_power = st.slider('Max Power (bhp)', 0, 200, key='max_power')

# Prediction
if st.button('Predict Price'):
    # Prepare input
    input_data_model = pd.DataFrame(
        [[year, fuel, max_power]],
        columns=['year', 'fuel', 'max_power']
    )

    # Encode categorical fuel type
    input_data_model['fuel'] = input_data_model['fuel'].replace({'Diesel': 0, 'Petrol': 1})

    # Predict log(price)
    car_price = model.predict(input_data_model.values)

    # Convert back from log scale
    car_price = np.exp(car_price)

    # Show result
    st.success(f"Estimated Car Price: {car_price[0]:,.2f}")