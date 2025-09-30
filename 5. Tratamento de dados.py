import numpy as np
import pandas as pd

covid_sp = pd.read_csv(
'C:/HD/ESTUDO GERAL 2025/ESTUDOS EM GERAL GRADE 3 SEMENTRES 2025/1. Python/4. Estudo de Python base/3. Projetos/1. Covid 19/covid_19/Database de dados/dados_covid_sp.csv', sep=';', encoding='utf-8')

#Renomeando as colunas, lembrando que essa mudança é apenas para a variavei civd_sp  
covid_sp2 = covid_sp.rename(columns={'nome_munic':'municipio'})

print(covid_sp2.head(3))

# Renomeando as colunas definidamente com o inplace=true
covid_sp.rename(columns={'datahora':'data'}, inplace=True)
covid_sp.rename(columns={'nome_munic':'municipio'}, inplace=True)

# Renomeando mais de uma coluna de uma vez
covid_sp.rename(columns={'map_leg': 'rotulo_mapa','map_leg_s':'codigo_mapa'},inplace=True) 

#Validando se a coluna foi renomeada corretamente 
print(covid_sp.head(3))

# 2 -  Excluir variaveis ( coluna )

# excluir pelo nome da coluna 
covid_sp_alterado_removendo_hora_test = covid_sp.drop(columns=['data'])

print(covid_sp_alterado_removendo_hora_test.head(3))

# Verficando os numero de colunas e de registros  

print(covid_sp_alterado_removendo_hora_test.shape)

# Removendo uma coluna com o numero de posição da coluna 

covid_sp_alterado_removendo_hora_test2 = covid_sp_alterado_removendo_hora_test.drop(covid_sp_alterado_removendo_hora_test.columns[[1]], axis=1)

print(covid_sp_alterado_removendo_hora_test2.shape)

# Remover várias colunas de uma de uma vez 

covid_sp_alterado_removendo_hora_test2.drop(columns=['casos','pop'],inplace=True)

print(covid_sp_alterado_removendo_hora_test2.shape)

covid_sp_alterado_removendo_hora_test2.drop(covid_sp_alterado_removendo_hora_test2.columns[[13,14,18,19]],axis=1, inplace=True)

# Explicação curta: inplace=True altera diretamente a tabela real (DataFrame),
# enquanto inplace=False cria uma cópia que pode ser salva em uma variável.









