import os
os.system('cls')

# PANDAS
import pandas as pd # pip install pandas

# Biblioteca que permite manipular e analisar dados
# ----------- Listas
lista = ["Edson", "Maria", "José", "Ester",]

lista_pd = pd.Series(lista)
print(lista_pd)

print()

lista_df = pd.DataFrame(lista)
print(lista_df)

# matriz
os.system('cls')
matriz = [[23, "Edson"], [43, "Ester"], [29, "Maria"]]
matriz_pd = pd.Series(matriz)
print(matriz_pd)
print()
matriz_df = pd.DataFrame(matriz)
print(matriz_df)

# Estrutura de dados
os.system('cls')
venda = {
    'Data': ['10/10/2024', '16/04/2023'],
    'Valor': [456.76, 33.2],
    'Produto': ['Feijão', 'Arroz'],
    'Qtde': [50, 66],
}
venda_pd = pd.Series(venda)
print(venda_pd)
print()
venda_df = pd.DataFrame(venda)
print(venda_df)