import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción de Costo  ''')
st.image("dinero.jpg", caption="Predicción del costo.")

st.header('Datos')

def user_input_features():
  # Entrada
  presupuesto = st.number_input('Presupuesto:', min_value=0.0, max_value=5000.0, value=1000.0, step=100.0)
  tiempo = st.number_input('Tiempo invertido (minutos):', min_value=0.0, max_value=500.0, value=1.0, step=1.0)
  tipo = st.number_input('Tipo (Salud:0, Alimento:1, Ahorro: 2, Inversión:2, Ocio:4, Entretenimiento:4, "Transporte":6):', min_value=1, max_value=6, value=1, step=1)
  momento = st.number_input('Momento (Dia: 1, Tarde:2, Noche:3):', min_value=1, max_value=3, value=1, step=1)
  no_personas = st.number_input('Número de personas:', min_value=1, max_value=100, value=1, step=1)

  user_input_data = {"Presupuesto" : presupuesto,
                     "Tiempo" : tiempo,
                     "Tipo" : tipo,
                     "Momento" : momento,
                     "No. de personas" : no_Personas}

  features = pd.DataFrame(user_input_data, index=[0])
  return features

df = user_input_features()

G = pd.read_csv('DatosGastos.csv')

X = G.drop(columns=['Costo'])
y = G['Costo']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1614175)

LR = LinearRegression()
LR.fit(X_train, y_train)

b1 = LR.coef_
b0 = LR.intercept_

prediccion = (b0+ b1[0]*df["Presupuesto"] + b1[1]*df["Tiempo"] + b1[2]*df["Tipo"]+ b1[3]*["Momento"]+ b1[4]*["No. de personas"])

st.subheader('Cálculo del costo aproximado')
st.write('El costo aproximado es: ', prediccion.values[0], "$")
