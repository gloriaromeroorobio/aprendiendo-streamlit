import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargar los datos
@st.cache
def load_data():
    data = pd.read_csv('pelis.csv')
    return data

data = load_data()

# Sidebar: Filtros
st.sidebar.header('Filtros')
rank = st.sidebar.slider('Rank', int(data['Rank'].min()), int(data['Rank'].max()))
year = st.sidebar.slider('Year', int(data['Year'].min()), int(data['Year'].max()))
votes = st.sidebar.slider('Votes', int(data['Votes'].min()), int(data['Votes'].max()))
revenue = st.sidebar.slider('Revenue (Millions)', float(data['Revenue (Millions)'].min()), float(data['Revenue (Millions)'].max()))

# Filtrar datos
filtered_data = data[(data['Rank'] <= rank) & 
                     (data['Year'] <= year) & 
                     (data['Votes'] <= votes) & 
                     (data['Revenue (Millions)'] <= revenue)]

# Gráfico de barras de películas por año
fig, ax = plt.subplots()
filtered_data['Year'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title('Número de Películas por Año')
ax.set_xlabel('Año')
ax.set_ylabel('Número de Películas')

st.pyplot(fig)
