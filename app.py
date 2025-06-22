import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Interactive Data Visualization with Plotly and Streamlit")
st.write("This app allows you to visualize data interactively using Plotly and Streamlit.")

car_data = pd.read_csv("/home/mad52xd/proyect_s7/vehicles_us.csv")
hist_button_o= st.button("Show Mileaage Histogram")
hist_button_p = st.button("Show Prices Histogram")

if hist_button_o:
    st.subheader("Histogram of Mileage")
    fig = px.histogram(car_data, x="odometer", nbins=50, title="Vehicle Price Distribution")
    st.plotly_chart(fig)

if hist_button_p:
    st.subheader("Histogram of Prices")
    fig = px.histogram(car_data, x="price", nbins=50, title="Vehicle Price Distribution")
    st.plotly_chart(fig)

