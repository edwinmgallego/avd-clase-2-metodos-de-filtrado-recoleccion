import pandas as pd

# Leer un archivo CSV
#csv_data = pd.read_csv('datos.csv')
#csv_data = pd.read_csv('dataset/dataset_turismo.csv')
#print(csv_data.head())

# Leer un archivo Excel

excel_data = pd.read_excel('dataset/ListadeestudiantesCurso .xlsx', sheet_name='Lista de estudiantes')
print(excel_data.head())

