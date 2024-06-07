import pandas as pd
import streamlit as st
import numpy as np
import pickle as pk
import math
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
st.write("""
<div style='text-align:center'>
    <h1 style='color:#FB04F7;'>Singapore Resale Flat Prices Prediction</h1>
</div>
""", unsafe_allow_html=True)

st.write("""
    <div style='text-align:center'>
        <h3 style='color:#FB1004;'>Selling Price Predictor</h3>
    </div>
    """, unsafe_allow_html=True)
town_options = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
        'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
        'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
        'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
        'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
        'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
        'PUNGGOL']
flat_type_options = ['1 ROOM', '3 ROOM', '4 ROOM', '2 ROOM', '5 ROOM', 'EXECUTIVE','MULTI GENERATION']
country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
flat_model_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
# Define the widgets for user input
st.write( f'<h5 style="color:rgb(120, 251, 4);">NOTE: Min & Max given for reference, you can enter any value</h5>', unsafe_allow_html=True )
col1,col2,col3=st.columns([5,2,5])
with col1:
    town = st.selectbox("Town", town_options,key=1)
    flat_type = st.selectbox("flat_type", flat_type_options,key=2)
    flat_model = st.selectbox("flat_model", flat_model_options,key=3)
    floor_area_sqm = st.text_input("Enter floor Area_sqm  (Min:28.0 & Max:307.0)")
    lease_commence_date = st.text_input("Enter Lease Commence Year  (Min:1966 & Max:2022)")
with col3:
        remaining_lease = st.text_input("Enter Remaining Lease (Min:41 & Max:98)")
        start = st.text_input("Enter Storey Range Start(Min:1 & Max:49)")
        end = st.text_input("Enter Storey Range End (Min:3, Max:51)")
        year = st.text_input("Price of which Year (Min:1990, Max:2024)")
        month_of_year = st.text_input("Price of which Month (Min:1, Max:12)")
submit_button = st.button(label="PREDICT SELLING PRICE")
st.markdown("""
                        <style>
                        div.stButton > button:first-child {
                            background-color: #FBF704;
                            color: red;
                            width: 100%;
                        }
                        </style>
        """, unsafe_allow_html=True)
def fun():
        new_sample= np.array([[town,flat_type,floor_area_sqm,flat_model,lease_commence_date,remaining_lease,start,end,year,month_of_year]])
        new=pd.DataFrame(new_sample,columns=['town', 'flat_type','floor_area_sqm','flat_model', 'lease_commence_date', 'remaining_lease','start', 'end', 'year', 'month_of_year'])
        with open(r"XGBRegressor_model (1).pkl", 'rb') as file:
            loaded_model = pk.load(file)
        new_pred = loaded_model.predict(new)
        reversed_value = math.exp(new_pred)
        return(reversed_value)
if submit_button:
        a=fun()
        st.write("Flat Resale Price:",a)