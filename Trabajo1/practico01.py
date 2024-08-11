import matplotlib.pyplot as plt # importamos la libreria de pandas y matplotlib
import pandas as pd
import numpy as np

datos = pd.read_csv('datos_personas.csv') # leemos el archivo csv

x = datos['Altura (cm)'] / 100 # asignamos la variable datos altura a x
y = datos['Peso (kg)'] # asignamos la variable datos peso a y

np.random.seed(42)
estaturas = np.random.uniform(1.4, 2.0, 100)
pesos = []

for estatura in estaturas:
    peso_min = 18.5 * (estatura ** 2)
    peso_max = 24.9 * (estatura ** 2)
    peso = np.random.uniform(peso_min, peso_max)
    pesos.append(peso)

data_generated = pd.DataFrame({
    'Estatura (m)': estaturas,
    'Peso (kg)': pesos
})

x_gen = data_generated['Estatura (m)']
y_gen = data_generated['Peso (kg)']
m_gen = np.sum((x_gen - np.mean(x_gen)) * (y_gen - np.mean(y_gen))) / np.sum((x_gen - np.mean(x_gen)) ** 2)
b_gen = np.mean(y_gen) - m_gen * np.mean(x_gen)
y_line_gen = m_gen * x_gen + b_gen

m_csv = np.sum((x_csv - np.mean(x_csv)) * (y_csv - np.mean(y_csv))) / np.sum((x_csv - np.mean(x_csv)) ** 2)
b_csv = np.mean(y_csv) - m_csv * np.mean(x_csv)
y_line_csv = m_csv * x_csv + b_csv

plt.figure(figsize=(10, 6))

plt.scatter(x_gen, y_gen, color='blue', label='Datos Generados')
plt.plot(x_gen, y_line_gen, color='red', label='Línea ajustada (Generados)')

plt.scatter(x_csv, y_csv, color='green', label='Datos CSV')
plt.plot(x_csv, y_line_csv, color='orange', label='Línea ajustada (CSV)')

plt.title('Estatura vs Peso (Datos Generados y Datos CSV)')
plt.xlabel('Estatura/Altura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()
