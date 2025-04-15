import os
os.system('cls')

import pandas as pd # pip install pandas openpyxl

dados = {
    'Data': ['10/10/2024', '16/04/2023'],
    'Valor': [456.76, 33.2],
    'Produto': ['Feijão', 'Arroz'],
    'Qtde': [50, 66],
}

df = pd.DataFrame(dados)

df.to_excel("planilha.xlsx", index = True, header = True, startcol = 4, startrow = 5)

print(f"Planilha criada com sucesso!")

