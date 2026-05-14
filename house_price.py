import pickle
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
house_price_model = pickle.load(open('house_price_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

st.title('House Price Prediction')

num_bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=10, value=3)
num_bathrooms = st.number_input('Number of Bathrooms', min_value=0.0, max_value=10.0, value=2.0, step=0.5)
square_footage = st.number_input('Square Footage', min_value=100, max_value=10000, value=1500)
lot_size = st.number_input('Lot Size (in acres)', min_value=0.0, max_value=10.0, value=0.5, step=0.1)
year_built = st.number_input('Year Built', min_value=1800, max_value=2024, value=2000)
garage_size = st.number_input('Garage Size (number of cars)', min_value=0, max_value=5, value=2)
neighborhood_quality = st.number_input('Neighborhood Quality (1-10)', min_value=1, max_value=10, value=7)

prediction = ''

if st.button('Predict House Price'):
    input_data = [[num_bedrooms, num_bathrooms, square_footage, lot_size, year_built, garage_size, neighborhood_quality]]
    input_data_scaled = scaler.transform(input_data)
    predicted_price = house_price_model.predict(input_data_scaled)
    prediction = f'Predicted House Price: ${predicted_price[0]:,.2f}'

if prediction:
    st.success(prediction)
