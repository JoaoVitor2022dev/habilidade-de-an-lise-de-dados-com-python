# --------------------------------------------
# Análise dos tipos de atributos em Python
# Autor: João Mocambite
# --------------------------------------------

import pandas as pd

# ============================================================
# 1️⃣ OBJECT → Strings (textos)
# ============================================================

# Tudo que é texto, nome, código ou palavra é do tipo object.
# Exemplo simples:

nome = "João Mocambite"
cidade = "Florianópolis"
produto = "Tênis Nike"

print("Exemplo de object:")
print(nome, cidade, produto)
print("Tipo:", type(nome))
print("-" * 40)

# Exemplo prático com pandas:

dados = pd.DataFrame({
    'Nome': ['João', 'Maria', 'Carlos'],  # tipo object
    'Idade': [25, 30, 22]                 # tipo int64
})


print("Tipos de dados no DataFrame:")
print(dados.dtypes)

print("-" * 40)

# ============================================================
# 2️⃣ INT64 → Números inteiros
# ============================================================

# Representam valores sem casas decimais

idade = 25

quantidade = 100

saldo = -15

print("Exemplo de int64:")
print(idade, quantidade, saldo)
print("Tipo:", type(idade))
print("-" * 40)

# ============================================================
# 3️⃣ FLOAT64 → Números reais (com casas decimais)
# ============================================================

# Representam valores com ponto flutuante (decimais)

preco = 49.90

altura = 1.75

nota = 8.5

print("Exemplo de float64:")
print(preco, altura, nota)
print("Tipo:", type(preco))
print("-" * 40)

# ============================================================
# 4️⃣ COMPLEX → Números complexos
# ============================================================

# Usados em matemática e engenharia (pouco comum em análise de dados)
z = 2 + 3j

print("Exemplo de complex:")
print(z)
print("Parte real:", z.real)
print("Parte imaginária:", z.imag)
print("Tipo:", type(z))
print("-" * 40)

# ============================================================
# 🔎 RESUMO GERAL
# ============================================================

print("Resumo dos tipos de dados:")
print("""
| Tipo      | Exemplo      | Significado                     |
|------------|--------------|----------------------------------|
| object     | "João"       | Texto, nomes, palavras           |
| int64      | 25           | Números inteiros                 |
| float64    | 49.90        | Números com decimais             |
| complex    | 2 + 3j       | Números complexos (raro)         |
""")

# ============================================================
# Fim do arquivo
# ============================================================
