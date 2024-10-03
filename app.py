import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # Leer los datos.

st.header("Venta de autos en USA") # Crear un encabezado.

#Crear un botón para crear el histograma.
hist_boton = st.button('Construir histograma')

if hist_boton:

    st.write('Creación de un histograma de los valores del odometro de los autos.')

    fig = px.histogram(car_data, x = 'odometer')

    st.plotly_chart(fig)

# Crear un gráfico de dispersión.
dispersion_boton = st.checkbox("Crear gráfico de dispersión")

if dispersion_boton:
        
    st.write("Creación de gráfico de dispersión precio del auto vs horometro")

    fig = px.scatter(car_data, x = "odometer", y = "price")

    st.plotly_chart(fig)