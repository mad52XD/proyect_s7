import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Interactive Data Visualization with Plotly and Streamlit")
st.write("This app allows you to visualize data interactively using Plotly and Streamlit.")

car_data = pd.read_csv("/home/mad52xd/proyect_s7/vehicles_us.csv")
hist_button= st.button("Show Histogram")
scatter_button = st.button("Show Scatter Plot")
'''
if hist_button:
    st.write("Histogram of Vehicles Odometer Readings")
    fig = px.histogram(car_data, x="odomter")
    st.plotly_chart(fig, use_container_width=True)

elif scatter_button:
    st.write("Scatter Plot of Vehicles Odometer Readings vs Price")
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    fig.show()
'''
