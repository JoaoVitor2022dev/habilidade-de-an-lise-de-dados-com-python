import statsmodels.api as sm

cancer = sm.datasets.cancer.load_pandas().data

# cabeçalho de dados 
print(cancer.head())

# o tipo de extrutura de dados 
print(type(cancer))

# a quantidade de colunas e linhas
print(cancer.shape)

