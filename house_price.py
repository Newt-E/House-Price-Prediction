import pickle
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
house_price_model = pickle.load(open(os.path.join(BASE_DIR, 'house_price_model.sav'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'scaler.sav'), 'rb'))

st.title('House Price Prediction')

num_bedrooms = st.text_input('Number of Bedrooms')
num_bathrooms = st.text_input('Number of Bathrooms')
square_footage = st.text_input('Square Footage')
lot_size = st.text_input('Lot Size (in acres)')
year_built = st.text_input('Year Built')
garage_size = st.text_input('Garage Size (number of cars)')
neighborhood_quality = st.text_input('Neighborhood Quality (1-10)')

prediction = ''

if st.button('Predict House Price'):
    input_data = ([[num_bedrooms, num_bathrooms, square_footage, lot_size, year_built, garage_size, neighborhood_quality]])
    input_data_scaled = scaler.transform(input_data)
    predicted_price = house_price_model.predict(input_data_scaled)
    prediction = f'Predicted House Price: ${predicted_price[0]:,.2f}'

if prediction:
    st.success(prediction)