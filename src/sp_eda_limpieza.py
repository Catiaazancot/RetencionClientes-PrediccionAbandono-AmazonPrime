import pandas as pd

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