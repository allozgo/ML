import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import sklearn

with open('modelo_entrenado.pkl', 'rb') as archivo_modelo:
    modelo = pickle.load(archivo_modelo)

st.set_page_config(
    page_title="Predicción ataques al corazón",
    page_icon=":heart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("PREDICCIÓN ATAQUES AL CORAZÓN")
st.sidebar.text("Menú")

home = st.sidebar.button("Home")
datos = st.sidebar.button("Introducir datos")
prediction = st.sidebar.button("Hacer predicciones")

nuevo_paciente = None

def dict_vals(dict):
    x = list(dict.values())
    x = np.array([x])
    return x

def hacer_prediccion(prediccion, nuevo_paciente):
    lifestyle_changes = []
    if prediccion > 0:
        if 'Cholesterol' in nuevo_paciente and nuevo_paciente['Cholesterol'] > 240:
            lifestyle_changes.append('tienes que mejorar tu dieta y hacer ejercicior')
        if 'BMI' in nuevo_paciente and nuevo_paciente['BMI'] < 18.5:
            lifestyle_changes.append('tienes que ganar peso')
        elif 'BMI' in nuevo_paciente and nuevo_paciente['BMI'] > 25:
            lifestyle_changes.append('tienes que perder peso')
        if 'Exercise Hours Per Week' in nuevo_paciente and nuevo_paciente['Exercise Hours Per Week'] < 1.25:
            lifestyle_changes.append('tienes que hacer más ejercicio')
        if 'systolic' in nuevo_paciente and nuevo_paciente['systolic'] > 120:
            lifestyle_changes.append('tienes que controlar tu presión arterial')
        if 'Stresss Level' in nuevo_paciente and nuevo_paciente['Stresss Level'] > 5:
            lifestyle_changes.append('tienes que aprender a relajarte')
        if 'Obesity' in nuevo_paciente and nuevo_paciente['Obesity'] == 1:
            lifestyle_changes.append('tienes que comer mejor')  
        if 'Sleep Hours Per Day' in nuevo_paciente and nuevo_paciente['Sleep Hours Per Day'] < 7:
            lifestyle_changes.append('tienes que dormir más')  
        if 'Triglycerides' in nuevo_paciente and nuevo_paciente['Triglycerides'] > 150:
            lifestyle_changes.append('tienes que controlar tus trigliceridos')  
        if 'Diabetes' in nuevo_paciente and nuevo_paciente['Diabetes'] == 1:
            lifestyle_changes.append('tienes que controlar tu diabetes')  
        st.write("Heart attack risk:", prediccion)
        for i in lifestyle_changes:
            st.write(f"Por favor, {i},")
        st.write("Esto puede reducir tu riesgo de ataque al corazón.")
        
    if prediccion > 0.75:
        st.warning("Deberías consultar con tu médico.")
        st.warning("Riesgo de ataque al corazón:", prediccion)



if datos:
    st.header("Datos")
    st.text("A continuación introduce tus datos:")

    cholesterol = st.number_input('Colesterol:')
    BMI = st.number_input('Índice de masa corporal', min_value=0.0, max_value=100.0)
    exercise = st.number_input('Horas de ejecicio semanales', min_value=0.0, max_value=100.0)
    systolic = st.number_input('Valor de tu presión arterial sistólica', min_value=0.0, max_value=200.0)
    stress = st.number_input('tu nivel de estrés de 0 a 10', min_value=0.0, max_value=10.0)
    obesidad = st.selectbox('Obesidad: (0: No, 1: Sí)', [0,1])
    sleep = st.number_input('Horas de sueño diarias', min_value=0.0, max_value=1.0)
    obesidad = st.selectbox('Obesidad: (0: No, 1: Sí)', [0,1])
    triglycerides = st.number_input('Trigliceridos', min_value=0.0, max_value=1000.0)
    diabetes = st.selectbox('Diabetes: (0: No, 1: Sí)', [0,1])

    if st.button("Procesar Datos"):
        nuevo_paciente = {'Cholesterol': cholesterol, 'BMI': BMI, ...}
        x = dict_vals(nuevo_paciente)
        st.success("Datos procesados con éxito!")

if prediction:
    st.header("Predicciones")
    st.text("A continuación mostramos la prediccón:")

    model.predict(x)
    prediccion = modelo.predict_proba(x)[:, 1]
    resultado = hacer_prediccion(prediccion, nuevo_paciente)
    resultado

else:
    st.header("Welcome page")
    st.text("Bienvenidos a nuestra APP de predicción de infartos")
    image_url = "https://www.inlet.es/wp-content/uploads/2019/10/sello-Fundacion-Espanola-Corazon-inlet.jpg"
    st.image(image_url)
