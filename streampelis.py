import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
import streamlit as st
import pandas as pd
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
# Grouping data by 'Year' and summing 'Revenue (Millions)' for each year
yearly_revenue = data.groupby('Year')['Revenue (Millions)'].sum()

# Plotting the bar chart
plt.figure(figsize=(12, 6))
yearly_revenue.plot(kind='bar', color='skyblue')
plt.title('Total Revenue of Movies by Year (in Millions)')
plt.xlabel('Year')
plt.ylabel('Total Revenue (Millions)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
