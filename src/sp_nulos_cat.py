# Importaciones de paquetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

# Observación general de nulos
def calcular_nulos(dataframe):
  porcentaje_nulos = (dataframe.isnull().sum()/dataframe.shape[0])*100
  return porcentaje_nulos


# Análisis general de las columnas categóricas
def analisis_general_cat(dataframe):
  col_cat = dataframe.select_dtypes(include='O').columns
  if len(col_cat) == 0:
    print('No hay columnas categóricas')
  else:
    for col in col_cat:
      print(f'Distribución de la columna {col.upper()}:')
      print(f'Esta columna tiene {len(dataframe[col].unique())} valores únicos')
      display(dataframe[col].value_counts(normalize=True))
      print('---------------------')
      display(dataframe[col].describe())
      
      print('---------------------')
      

# Graficar columnas categoricas
def subplot_col_cat(dataframe):
  
  # Seleccionar columnas categóricas
  col_cat = dataframe.select_dtypes(include=['object','category']).columns
  
  if len(col_cat) == 0:
    print("No hay columnas categóricas")
    return
  
  # Configurar el tamaño de la figura
  num_cols = len(col_cat)
  num_filas = (num_cols + 2) //3 # Calcular las filas necesarias para 3 columnas por fila
  fig, axes = plt.subplots(num_filas, 3, figsize=(15, num_filas * 5))
  axes = axes.flatten() # Convertir los ejes del array para facilitar la iteracion
  
  # Generar graficos para cada columna categorica
  for i, col in enumerate(col_cat):
    sns.countplot(data=dataframe, x=col, ax = axes[i], hue=col, palette="tab10", legend=False)
    axes[i].set_title(f'Distribucion de {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Frecuencia')
    axes[i].tick_params(axis='x', rotation=90) # Rotar etiquetas si es necesario
  
  # Eliminar ejes sobrantes si hay menos columnas que subplots
  for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])
  
  # Ajustar diseño
  plt.tight_layout()
  plt.show()
  
  
# Graficar columnas numéricas
def subplot_col_num(dataframe, col):
  num_graph = len(col)
  num_rows = (num_graph + 2) // 2

  fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5))

  for i, col in enumerate(col):
      sns.histplot(data=dataframe, x=col, ax=axes[i,0], bins=200)
      axes[i,0].set_title(f'Distribucion de {col}')
      axes[i,0].set_xlabel(col)
      axes[i,0].set_ylabel('Frecuencia')
      
      sns.boxplot(data=dataframe, x=col, ax=axes[i,1])
      axes[i,1].set_title(f'Boxplot de {col}')

  for j in range(i+1, len(axes)):
    fig.delaxes(axes[j])

  plt.tight_layout()
  plt.show()