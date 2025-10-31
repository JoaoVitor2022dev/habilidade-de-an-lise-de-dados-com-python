import numpy as np
import pandas as pd
from collections import Counter

cancap_ouze = pd.read_csv(
    'C:/HD/ESTUDO GERAL 2025/ESTUDOS EM GERAL GRADE 3 SEMENTRES 2025/1. Python/4. Estudo de Python base/3. Projetos/5. Tratamento/ouze/data/CANCAP_OUZE.csv',
    sep=';',
    encoding='utf-8',
    skiprows=4  # ⬅️ Pula as 4 primeiras linhas
)

print(cancap_ouze.isnull().sum())

# cabeçalho de dados 
# print(cancap_ouze2.head(10))

print(cancap_ouze['Telefone - Todos os telefones.2'].isnull().sum())

# EXCLUIR TODOS OS VALORES MISSING
cancap_ouze2 = cancap_ouze.dropna()

print(cancap_ouze2.isnull().sum())


# SUBSTITUIR OS VALORES MISSING PELA MEDIANA
cancap_ouze2['obitos_novos'].fillna(cancap_ouze2['obitos_novos'].median(), inplace=True)

# SUBSTITUIR OS VALORES MISSING PELA MÉDIA
cancap_ouze2['obitos_novos'].fillna(cancap_ouze2['obitos_novos'].mean(), inplace=True)

# SUBSTITUIR OS VALORES MISSING POR QUALQUER OUTRO VALOR
cancap_ouze2['obitos_novos'].fillna(cancap_ouze2['obitos_novos'].mean(), inplace=True)

['obitos_novos'].fillna(10, inplace=True)