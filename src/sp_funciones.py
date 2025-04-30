# Importaciones de paquetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# Hacer un analisis exploratorio de los datos 
def eda_preliminar(df):
  display(df.sample(5))
  print("-----------------")
  print('INFO')
  display(df.info())
  print("-----------------")
  print('NULOS')
  display(round(df.isnull().sum()/df.shape[0]*100,2))
  print("-----------------")
  print('DUPLICADOS')
  print(df.duplicated().sum())
  print("-----------------")
  print('VALUE COUNTS')
  for col in df.select_dtypes(include='O').columns:
    print(df[col].value_counts())
    print("---------------------")
    

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
  
  
# Análisis de las columnas categóricas con churn_label
def analisis_categoricas(dataframe, col_cat):
  col_excluidas = ["churn_label", "customer_id", "state", "contact_date", "last_transaction_date"] # Excluir estas columnas por el momento
  col_cat = [col for col in dataframe.select_dtypes(include='O').columns if col not in col_excluidas]
    
  if len(col_cat) == 0:
      print("No hay columnas categóricas")
  else:
    # Configurar el tamaño de la figura
    num_cols = len(col_cat)
    num_filas = (num_cols + 2) //3 # Calcular las filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(num_filas, 3, figsize=(15, num_filas * 5))
    axes = axes.flatten() # Convertir los ejes del array para facilitar la iteracion
      
      # Generar graficos para cada columna categorica
    for i, col in enumerate(col_cat):
      sns.countplot(data=dataframe, x=col, ax = axes[i], hue='churn_label', palette="tab10", legend=False)
      axes[i].set_title(f'Distribucion de {col} por churn_label')
      axes[i].set_xlabel(col)
      axes[i].set_ylabel('Frecuencia')
      axes[i].tick_params(axis='x', rotation=90) # Rotar etiquetas si es necesario
      
    # Eliminar ejes sobrantes si hay menos columnas que subplots
    for j in range(i + 1, len(axes)):
      fig.delaxes(axes[j])
    
    # Ajustar diseño
    plt.tight_layout()
    plt.show()
    

# Análisis columnas temporales
def plot_churn_tendencia(dataframe, unidad_tiempo="month"):
    """
    Función para visualizar la evolución del churn en función del tiempo.
    
    Parámetros:
    - df: DataFrame con los datos.
    - time_unit: Nivel de agrupación temporal ('month', 'year', 'quarter').
    """
    # Filtrar solo los clientes que han hecho churn
    df_churn = dataframe[dataframe["churn_label"] == "yes"]
    
    # Definir la columna de tiempo a usar
    col_tiempo = unidad_tiempo
    
    if col_tiempo not in dataframe.columns:
        print(f"Error: La columna '{col_tiempo}' no existe en el dataset.")
        return

    # Contar la cantidad de churns por la unidad de tiempo seleccionada
    churn_trend = df_churn.groupby(col_tiempo).size()

    # Graficar la evolución del churn
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=churn_trend.index, y=churn_trend.values, marker="o", color="red")
    plt.title(f"Evolución del Churn por {unidad_tiempo.capitalize()}")
    plt.xlabel(unidad_tiempo.capitalize())
    plt.ylabel("Cantidad de Churns")
    plt.grid(True)

    # Ajustar el eje X si es por mes o trimestre
    if unidad_tiempo == "month":
        plt.xticks(range(1, 13))  # Asegurar que todos los meses aparezcan
    elif unidad_tiempo == "quarter":
        plt.xticks(range(1, 5))  # Asegurar que todos los trimestres aparezcan

    plt.show()
    

def analisis_numericas(dataframe, col_num):
    """
    Función para analizar variables numéricas en relación con 'churn_label'.
    Muestra histogramas para visualizar la distribución.
    
    Parámetros:
    - dataframe: DataFrame con los datos.
    - col_num: Lista de columnas numéricas a analizar.
    """
    
    if len(col_num) == 0:
        print("No hay columnas numéricas.")
    else:
        # Configurar el tamaño de la figura
        num_cols = 3  # 3 gráficos por fila
        num_filas = (len(col_num) + 2) // num_cols  # Calcular filas necesarias
        fig, axes = plt.subplots(num_filas, num_cols, figsize=(15, num_filas * 5))
        axes = axes.flatten()  # Convertir los ejes del array en una lista para iterar
        
        # Generar histogramas para cada variable numérica
        for i, col in enumerate(col_num):
            sns.histplot(data=dataframe, x=col, hue="churn_label", kde=True, bins=30, ax=axes[i], palette="tab10", alpha=0.6)
            axes[i].set_title(f"Distribución de {col} por Churn Label")
            axes[i].set_xlabel(col)
            axes[i].set_ylabel("Frecuencia")
        
        # Eliminar ejes sobrantes si hay menos columnas que subplots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])
        
        # Ajustar diseño
        plt.tight_layout()
        plt.show()