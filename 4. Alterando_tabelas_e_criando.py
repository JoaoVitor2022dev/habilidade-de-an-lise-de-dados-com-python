import numpy as np
import pandas as pd


covid_sp = pd.read_csv(
    'C:/HD/ESTUDO GERAL 2025/ESTUDOS EM GERAL GRADE 3 SEMENTRES 2025/1. Python/4. Estudo de Python base/3. Projetos/1. Covid 19/covid_19/Database de dados/dados_covid_sp.csv',
    sep=';',           # Separador de colunas
    encoding='utf-8'   # Codificação de caracteres (pode ser utf-8, latin-1, iso-8859-1, etc.)
)

# Criar lista de índices
indices_lista = list(range(1, 880498))  

# Transformar lista em DataFrame
df_indices = pd.DataFrame(indices_lista, columns=['indice'])

# Juntar os DataFrames (dados + coluna de índices)
covid_sp = pd.concat([covid_sp, df_indices], axis=1)

#print(covid_sp.head(2))


# Reordenar colocando 'indice' como primeira coluna
covid_sp = covid_sp.reindex(columns=['indice'] + list(covid_sp.columns[:-1]))

#print(covid_sp.head(2))

# Remover coluna de posição 9
covid_sp_limpo = covid_sp.drop(covid_sp.columns[[9]], axis=1)

# Concatenar novamente com os índices
covid_sp_final = pd.concat([df_indices, covid_sp_limpo], axis=1)

print(covid_sp_final.head(10))
