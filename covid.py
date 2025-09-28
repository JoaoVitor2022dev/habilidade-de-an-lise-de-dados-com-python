import numpy as np
import pandas as pd

covid_sp = pd.read_csv(
    'C:/HD/ESTUDO GERAL 2025/ESTUDOS EM GERAL GRADE 3 SEMENTRES 2025/1. Python/4. Estudo de Python base/3. Projetos/1. Covid 19/covid_19/Database de dados/dados_covid_sp.csv',
    sep=';',           # Separador de colunas
    encoding='utf-8'   # Codificação de caracteres (pode ser utf-8, latin-1, iso-8859-1, etc.)
)

covid_sp_excel = pd.read_excel(
    'C:/HD/ESTUDO GERAL 2025/ESTUDOS EM GERAL GRADE 3 SEMENTRES 2025/1. Python/4. Estudo de Python base/3. Projetos/1. Covid 19/covid_19/Database de dados/covid_19_excel.xlsx'
)

# Exemplo: dataset Iris (famoso em Machine Learning)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Definindo os nomes das colunas manualmente
colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Criando o DataFrame
iris = pd.read_csv(url, names=colnames)

# shape → retorna (linhas, colunas)
print("Dimensão do dataset Iris (linhas, colunas):", iris.shape)

# len(iris.Class) → retorna o número de registros da coluna "Class"
print("Quantidade de registros na coluna 'Class':", len(iris.Class))

# head() → mostra os primeiros registros
print("\nExemplo dos 5 primeiros registros:")
print(iris.head())

# info() → mostra informações gerais das colunas
print("\nInformações do dataset:")
print(iris.info())

# describe() → estatísticas descritivas das colunas numéricas
print("\nEstatísticas descritivas:")
print(iris.describe())
