import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Loading the saved model
model = pickle.load(open("best_model.sav", 'rb'))

# Function to preprocess input data and make a prediction
def car_price_prediction(input_data):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data], columns=['Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Engine_CC', 'Power', 'Seats', 'Mileage_KmL'])

    # Use the loaded model to make a prediction
    prediction = model.predict(input_df)

    return prediction[0]

def app():
    #st.set_page_config(page_title='Car Price Prediction', page_icon=':oncoming_automobile:')
    st.title(':red_car: Find the Best Price for Your Car')
    #st.markdown('<style>div.block-container{padding-top:2.4rem;}</style>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("image.png")

    with col2:
        Year = st.slider('Enter the Year', 1990, 2024, 2015)
        Kilometers_Driven = st.number_input('Enter the KMS Driven')

        col1, col2, col3 = st.columns(3)

        with col1:
            Fuel_Type = st.selectbox('Select the Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG'])
            Engine_CC = st.number_input('Enter Engine CC')

        with col2:
            Transmission = st.selectbox('Select Transmission', ['Manual', 'Automatic'])
            Power = st.number_input('Enter the Power')

        with col3:
            Owner_Type = st.selectbox('Select Owner Type', ['First', 'Second', 'Third', 'Fourth'])
            Seats = st.number_input('Enter the Seats')

        Mileage_KmL = st.slider('Enter Mileage of Car', 10, 30)

        if st.button('Predict'):
            input_data = [Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Engine_CC, Power, Seats, Mileage_KmL]
            result = car_price_prediction(input_data)
            st.success(f'The predicted price of the car is: ₹{result:.2f} Lakh')

if __name__ == '__app__':
    app()
