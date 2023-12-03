import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Predicción ataques al corazón",
    page_icon=":heart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("MY ST APP")
st.sidebar.text("Menú")

home = st.sidebar.button("Home")
data = st.sidebar.button("Data")
viz = st.sidebar.button("Viz")
df = pd.read_csv("https://raw.githubusercontent.com/JLGOrtega/datasets/master/BostonHousing.csv")

if data:
    st.header("Home page")
    st.text("A continuación mostramos data:")

    st.dataframe(df)

elif viz:
    st.text("Viz")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.scatter_chart(data = df, x = "rm", y = "age", size = "medv", color = "rad")
    with col2:
        st.line_chart(data = df, x = "rm", y = "age")
    with col3:
        st.map(data = df, latitude = "rm", longitude = "age")

else:
    st.header("Welcome page")
    st.text("Bienvenidos a nuestra Streamlit APP")
    image_url = "https://www.65ymas.com/uploads/s1/84/56/43/puente-romano-cangas-de-onis_1_621x621.jpeg"
    st.image(image_url)
