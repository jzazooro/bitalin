import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Cargar los datos desde el archivo CSV subido
file_path = 'DATOS/1test8.csv'
data = pd.read_csv(file_path)

# Mostrar las primeras filas y la información del DataFrame para entender su estructura
data_info = data.info()
data_head = data.head()

data_info, data_head

# Visualización de los primeros 1000 puntos de datos para ECG y EDA
plt.figure(figsize=(15, 10))

# ECG de ambos dispositivos
plt.subplot(2, 1, 1)
plt.plot(data['ECG_bitalino'].iloc[:1000], label='ECG BITalino')
plt.plot(data['ECG_bionomadix'].iloc[:1000], label='ECG BioNomadix')
plt.title('Comparación de ECG BITalino vs BioNomadix')
plt.ylabel('Unidades de ECG')
plt.legend()

# EDA de ambos dispositivos
plt.subplot(2, 1, 2)
plt.plot(data['EDA_bitalino'].iloc[:1000], label='EDA BITalino')
plt.plot(data['EDA_bionomadix'].iloc[:1000], label='EDA BioNomadix')
plt.title('Comparación de EDA BITalino vs BioNomadix')
plt.ylabel('Unidades de EDA')
plt.xlabel('Muestras')
plt.legend()

plt.tight_layout()
plt.show()

from scipy.signal import find_peaks

# Configuración para la detección de picos R en la señal de ECG del BITalino
ecg_signal = data['ECG_bitalino']
# Establecer la altura mínima de un pico R considerando la escala de la señal
height = np.mean(ecg_signal) + 0.5 * np.std(ecg_signal)
distance = 50  # Distancia mínima entre picos, asumiendo una frecuencia cardíaca mínima razonable

# Detectar picos R
peaks, _ = find_peaks(ecg_signal, height=height, distance=distance)

# Calcular los intervalos RR (diferencia entre picos consecutivos) en número de muestras
rr_intervals = np.diff(peaks)
# Convertir de muestras a segundos (suponiendo una frecuencia de muestreo dada)
sampling_rate = 1000  # asumiendo una frecuencia de muestreo de 1000 Hz
rr_intervals_seconds = rr_intervals / sampling_rate

# Visualización de la señal de ECG con los picos R detectados
plt.figure(figsize=(10, 4))
plt.plot(ecg_signal[:2000], label='ECG BITalino')  # Visualizar solo los primeros 2000 puntos
plt.plot(peaks[peaks < 2000], ecg_signal[peaks[peaks < 2000]], "x", label='Picos R detectados')
plt.title('Señal de ECG con Picos R Detectados')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.show()

# Estadísticas básicas de los intervalos RR
rr_intervals_mean = np.mean(rr_intervals_seconds)
rr_intervals_std = np.std(rr_intervals_seconds)

rr_intervals_mean, rr_intervals_std

# Revisar los nombres de las columnas para confirmar el nombre correcto de la columna de ECG del BITalino
data.columns
# Revisar los nombres de las columnas correctamente, mostrando el encabezado del DataFrame nuevamente
data.head()
# Intentar cargar nuevamente el archivo CSV y mostrar los nombres de las columnas para asegurarse de que todo está correcto
data = pd.read_csv(file_path)

# Mostrar las primeras filas y la información del DataFrame para entender su estructura
data_info = data.info()
data_head = data.head()

data_info, data_head
