import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')



def app():
    #st.set_page_config(page_title='Car',page_icon=':bar_chart:')
    st.title(' :bar_chart: Indian Auto MPG Data Visualization')
    #st.markdown('<style>div.block-container{padding-top:2.4rem;}</style>',unsafe_allow_html=True)

    f1 = st.file_uploader(":file_folder: Upload a File", type=(['csv','txt', 'xlsx','xls']))
    if f1 is not None:
        filename = f1.name
        #st.write('filename')
        df = pd.read_csv(filename, encoding="ISO 8859-1")
    else:
        df = pd.read_csv("indian-auto-mpg.csv", #encoding="ISO 8859-1")


    st.sidebar.header("Choose Your Filter")

    # create for manufacturer
    manufacturer = st.sidebar.multiselect("Select Your Manufacturer", df['Manufacturer'].unique())
    if not manufacturer:
        df2 = df.copy()
    else:
        df2 = df[df['Manufacturer'].isin(manufacturer)]

    # create for name
    name = st.sidebar.multiselect('Select Name', df2['Name'].unique())
    if not name:
        df3 = df2.copy()
    else:
        df3 = df2[df2['Name'].isin(name)]

    #create for location
    location = st.sidebar.multiselect("Select Location", df3["Location"].unique())

    # Filter data based on manufacturer, name and location
    if not manufacturer and not name and not location:
        filtered_df = df
    elif not name and not location:
        filtered_df = df[df['Manufacturer'].isin(manufacturer)]
    elif not manufacturer and not location:
        filtered_df = df[df['Name'].isin(name)]
    elif name and location:
        filtered_df = df3[df['Name'].isin(name) & df3['Location'].isin(location)]
    elif manufacturer and location:
        filtered_df = df3[df['Manufacturer'].isin(manufacturer) & df3['Location'].isin(location)]
    elif manufacturer and name:
        filtered_df = df3[df['Manufacturer'].isin(manufacturer) & df3['Name'].isin(name)]
    elif location:
        filtered_df = df3[df3['Location'].isin(location)]
    else:
        filtered_df = df3[df3['Manufacturer'].isin(manufacturer) & df3['Name'].isin(name) & df3['Location'].isin(location)]

    col1, col2 = st.columns(2)

    avg_mileage = filtered_df.groupby('Manufacturer')['Mileage_KmL'].mean().sort_values(ascending=False)

    st.subheader("Average Mileage by Manufacturer")
    fig = px.bar(avg_mileage, x = avg_mileage.index, y = avg_mileage.values, template = "seaborn")
    fig.update_layout(xaxis_title='Manufacturer', yaxis_title='Average Mileage (Km/L)')
    st.plotly_chart(fig,use_container_width=True, height = 200)

    with col1:
        st.subheader("Distribution of Cars by Fuel Type")
        fig1 = px.histogram(filtered_df, y='Fuel_Type', title='Distribution of Cars by Fuel Type', labels={'Fuel_Type': 'Fuel Type'}, template = "seaborn", orientation='h')
        fig1.update_layout(xaxis_title='Count', yaxis_title='Fuel Type')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Distribution of Cars by Transmission")
        fig1 = px.histogram(filtered_df, x='Transmission', title='Distribution of Cars by Transmission', labels={'Transmission': 'Transmission'}, template = "seaborn")
        fig1.update_layout(xaxis_title='Transmission', yaxis_title='Count')
        st.plotly_chart(fig1, use_container_width=True)
        

    st.subheader("Hierarchical view")
    fig2 = px.treemap(filtered_df, path = ['Manufacturer','Location', 'Owner_Type'])
    fig2.update_layout(width = 800, height = 650)
    st.plotly_chart(fig2, use_container_width=True)


