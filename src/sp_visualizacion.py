# Importaciones de paquetes
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

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