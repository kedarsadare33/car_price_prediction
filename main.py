import streamlit as st
from streamlit_option_menu import option_menu

import car_dashboard, car_price_prediction

st.set_page_config(page_title= 'Car Price Prediction and Visualization', layout='wide')
st.markdown('<style>div.block-container{padding-top:2.4rem;}</style>', unsafe_allow_html=True)

class MultiApp:

    def __init__(self):
        self.app = []
    def add_app(self, title, function):
        self.app.append({
            "title" : title,
            "function" : function
        })
    
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title = 'Main Menu',
                options = ['Car Dashboard', 'Car Price Prediction'],
                icons = [],
                menu_icon = 'cast',
                default_index = 1,
            
            )

        if app == "Car Dashboard":
            car_dashboard.app()
        if app == "Car Price Prediction":
            car_price_prediction.app()
    run()