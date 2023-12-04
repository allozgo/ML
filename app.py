import streamlit as st
import pandas as pd
import numpy as np
import pickle
from heart_attack.ipynb import cargar_modelo, hacer_prediccion 

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
datos = st.sidebar.button("Predicciones")

cholesterol = st.slider('Colesterol:', min_value=0.0, max_value=1000.0)
BMI = st.slider('Índice de masa corporal', min_value=0.0, max_value=100.0)
exercise = st.slider('Horas de ejecicio semanales', min_value=0.0, max_value=100.0)
systolic = st.slider('Valor de tu presión arterial sistólica', min_value=0.0, max_value=200.0)
stress = st.slider('tu nivel de estrés de 0 a 10', min_value=0.0, max_value=10.0)
obesidad = st.slider('Obesidad: (0: No, 1: Sí)', min_value=0.0, max_value=1.0)
sleep = st.slider('Horas de sueño diarias', min_value=0.0, max_value=1.0)
obesidad = st.slider('Obesidad: (0: No, 1: Sí)', min_value=0.0, max_value=1.0)
triglycerides = st.slider('Trigliceridos', min_value=0.0, max_value=1000.0)
diabetes = st.slider('Diabetes: (0: No, 1: Sí)', min_value=0.0, max_value=1.0)
obesidad = st.slider('Obesidad: (0: No, 1: Sí)', min_value=0.0, max_value=1.0)
obesidad = st.slider('Obesidad: (0: No, 1: Sí)', min_value=0.0, max_value=1.0)
obesidad = st.slider('Obesidad: (0: No, 1: Sí)', min_value=0.0, max_value=1.0)


def dict_vals(dict):
    x = list(dict.values())
    x = np.array([x])
    return x

def hacer_prediccion(predict_type, dictionary):
    lifestyle_changes = []
    if predict_type > 0:
        if 'Cholesterol' in new_person and new_person['Smoking'] == 1:
            lifestyle_changes.append('tienes que dejar de fumar')
        if 'BMI' in new_person and new_person['BMI'] < 18.5:
            lifestyle_changes.append('tienes que ganar peso')
        elif 'BMI' in new_person and new_person['BMI'] > 25:
            lifestyle_changes.append('tienes que perder peso')
        if 'Exercise Hours Per Week' in new_person and new_person['Exercise Hours Per Week'] < 1.25:
            lifestyle_changes.append('tienes que hacer más ejercicio')
        if 'systolic' in new_person and new_person['Diet'] > 120:
            lifestyle_changes.append('tienes que controlar tu presión arterial')
        if 'Stresss Level' in new_person and new_person['Stresss Level'] > 5:
            lifestyle_changes.append('tienes que aprender a relajarte')
        if 'Obesity' in new_person and new_person['Obesity'] == 1:
            lifestyle_changes.append('tienes que comer mejor')  
        if 'Sleep Hours Per Day' in new_person and new_person['Sleep Hours Per Day'] < 7:
            lifestyle_changes.append('tienes que dormir más')  
        if 'Triglycerides' in new_person and new_person['Triglycerides'] > 150:
            lifestyle_changes.append('tienes que controlar tus trigliceridos')  
        if 'Diabetes' in new_person and new_person['Diabetes'] == 1:
            lifestyle_changes.append('tienes que controlar tu diabetes')  
        st.write("Heart attack risk:", predict_type)
        for i in lifestyle_changes:
            st.write(f"Por favor, {i},")
        st.write("Esto puede reducir tu riesgo de ataque al corazón.")
        
    if predict_type > 0.75:
        st.write("Deberías consultar con tu médico.")
        st.write("Riesgo de ataque al corazón:", predict_type)

nuevo_paciente = {'Cholesterol': cholesterol, 'systolic': systolic,
       'Diabetes': diabetes, 'Obesity': obesidad, 'Exercise Hours Per Week': exercise,
        'BMI': BMI, 'Triglycerides': triglycerides, "Stresss Level": stress, 'Sleep Hours Per Day' : sleep}
x = dict_vals(nuevo_paciente)

if datos:
    st.header("Home page")
    st.text("A continuación mostramos data:")

    model.predict(x)
    predict_type = model.predict_proba(x)[:, 1]
    result = determine_lifestyle_changes(predict_type, nuevo_paciente)
    result




else:
    st.header("Welcome page")
    st.text("Bienvenidos a nuestra APP de predicción de infartos")
    image_url = "https://www.inlet.es/wp-content/uploads/2019/10/sello-Fundacion-Espanola-Corazon-inlet.jpg"
    st.image(image_url)
