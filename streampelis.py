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

# Grouping data by 'Year' and summing 'Revenue (Millions)' for each year
yearly_revenue = filtered_data.groupby('Year')['Revenue (Millions)'].sum()


fig, ax = plt.subplots(figsize=(12, 6))
yearly_revenue.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Total Revenue of Movies by Year (in Millions)')
ax.set_xlabel('Year')
ax.set_ylabel('Total Revenue (Millions)')
plt.xticks(rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)
