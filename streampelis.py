import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

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
fig, ax = plt.subplots()
filtered_data['Year'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title('Número de Películas por Año')
ax.set_xlabel('Año')
ax.set_ylabel('Número de Películas')

st.pyplot(fig)

"""num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))"""
