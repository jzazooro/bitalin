import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV subido
file_path = 'DATOS/1test6.csv'
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