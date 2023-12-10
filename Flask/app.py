import pandas as pd
import numpy as np
import pickle
import os
import sklearn
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

modelo = None
nuevo_paciente = None

def dict_vals(dict):
    x = list(dict.values())
    x = np.array([x])
    return x

def hacer_prediccion(prediccion, nuevo_paciente):
    lifestyle_changes = []
    if prediccion > 0:
        # Lógica para evaluar las recomendaciones basadas en la predicción
        if 'Cholesterol' in nuevo_paciente and nuevo_paciente['Cholesterol'] > 240:
            lifestyle_changes.append('tienes que mejorar tu dieta y hacer ejercicio')
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

    mensaje_prediccion = f"Riesgo de ataque al corazón: {prediccion}"

    return lifestyle_changes, mensaje_prediccion

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/datos', methods=['GET', 'POST'])
def datos():
    global nuevo_paciente

    if request.method == 'POST':
        # Recuperar datos del formulario
        cholesterol = float(request.form['cholesterol'])
        BMI = float(request.form['BMI'])
        exercise = float(request.form['exercise'])
        systolic = float(request.form['systolic'])
        stress = float(request.form['stress'])
        obesidad = int(request.form['obesidad'])
        sleep = float(request.form['sleep'])
        triglycerides = float(request.form['triglycerides'])
        diabetes = int(request.form['diabetes'])

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

        return render_template('predicciones.html', mensaje="Datos procesados con éxito!")

    return render_template('datos.html', mensaje=None)

@app.route('/predicciones', methods=['GET', 'POST'])
def predicciones():
    global nuevo_paciente, modelo

    # Lógica para hacer la predicción utilizando el modelo y el nuevo_paciente
    if nuevo_paciente:
        x = dict_vals(nuevo_paciente)
        prediccion = modelo.predict_proba(x)[:, 1][0]
        resultado, mensaje_prediccion = hacer_prediccion(prediccion, nuevo_paciente)
        return render_template('predicciones.html', mensaje=mensaje_prediccion, prediccion=prediccion)

    return render_template('predicciones.html', mensaje="No hay datos para realizar predicciones.")

if __name__ == '__main__':
    # Inicializa el modelo y otros elementos necesarios
    with open('modelo_entrenado.pkl', 'rb') as archivo_modelo:
        modelo = pickle.load(archivo_modelo)

    # Ejecuta la aplicación Flask
    app.run(debug=True)