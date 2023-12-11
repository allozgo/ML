import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import sklearn

with open('modelo_entrenado.pkl', 'rb') as archivo_modelo:
    modelo = pickle.load(archivo_modelo)

if 'nuevo_paciente' not in st.session_state:
    st.session_state.nuevo_paciente = None

x = []

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
    st.header("Introducir Datos")
    
    # Formulario para introducir datos
    with st.form(key='my_form'):
        # Widget para introducir colesterol
        cholesterol = st.number_input('Colesterol:', key='cholesterol', value=0.0)

        # Widget para introducir BMI
        BMI = st.number_input('Índice de masa corporal', min_value=0.0, max_value=100.0, key='BMI', value=0.0)

        # Widget para introducir horas de ejercicio semanales
        exercise = st.number_input('Horas de ejercicio semanales', min_value=0.0, max_value=100.0, key='exercise', value=0.0)

        # Widget para introducir valor de presión arterial sistólica
        systolic = st.number_input('Valor de tu presión arterial sistólica', min_value=0.0, max_value=200.0, key='systolic', value=0.0)

        # Widget para introducir nivel de estrés
        stress = st.number_input('Tu nivel de estrés de 0 a 10', min_value=0.0, max_value=10.0, key='stress', value=0.0)

        # Widget para introducir obesidad (0: No, 1: Sí)
        obesidad = st.selectbox('Obesidad: (0: No, 1: Sí)', [0, 1], key='obesidad')

        # Widget para introducir horas de sueño diarias
        sleep = st.number_input('Horas de sueño diarias', min_value=0.0, max_value=24.0, key='sleep', value=0.0)

        # Widget para introducir triglicéridos
        triglycerides = st.number_input('Triglicéridos', min_value=0.0, max_value=1000.0, key='triglycerides', value=0.0)

        # Widget para introducir diabetes (0: No, 1: Sí)
        diabetes = st.selectbox('Diabetes: (0: No, 1: Sí)', [0, 1], key='diabetes')

        # Botón para procesar datos
        submit_button = st.form_submit_button(label='Procesar Datos')
    
    if submit_button:

        nuevo_paciente = {
            'Cholesterol': cholesterol,
            'BMI': BMI,
            'Exercise Hours Per Week': exercise,
            'systolic': systolic,
            'Stresss Level': stress,
            'Obesity': obesidad,
            'Sleep Hours Per Day': sleep,
            'Triglycerides': triglycerides,
            'Diabetes': diabetes
        }
        x = dict_vals(nuevo_paciente)
        st.success("Datos procesados con éxito!")

 

if prediction:
    st.header("Predicciones")
    st.text("A continuación mostramos la prediccón:")

    if st.session_state.nuevo_paciente:
        #x = dict_vals(st.session_state.nuevo_paciente)
        prediccion = modelo.predict_proba(x)[:, 1][0]
        lifestyle_changes, mensaje_prediccion = hacer_prediccion(prediccion, st.session_state.nuevo_paciente)

        st.write(f"Riesgo de ataque al corazón: {prediccion}")
        for cambio in lifestyle_changes:
            st.write(cambio)

        if prediccion > 0.75:
            st.warning("Deberías consultar con tu médico.")

if home:
    st.header("Welcome page")
    st.text("Bienvenidos a nuestra APP de predicción de infartos")
    image_url = "https://www.inlet.es/wp-content/uploads/2019/10/sello-Fundacion-Espanola-Corazon-inlet.jpg"
    st.image(image_url)
