# Enzo Luciano Barros de Oliveira
# RM 559557

import os
os.system('cls')

import pandas as pd

from datetime import datetime


dados = {
    'Data': ['10/10/2024', '16/04/2023', '22/05/2022'],
    'Valor': [456.76, 33.2, 376.9],
    'Produto': ['Feijão', 'Arroz', 'Batata'],
    'Qtde': [50, 66, 89],
}

def menu():
    print("""
    0 - SAIR
    1 - Exportar: PYTHON -> EXCEL
    2 - Importar: EXCEL -> PYTHON
    """)


def export_python(dados):
    df = pd.DataFrame(dados)
    nome_arquivo = input(f'Pressione [ENTER] para gerar um arquivo com a data-hora_atual.xlsx ou digite o nome do arquivo: ')
    if nome_arquivo == "":
        data = str(datetime.now())
        data_atual = data.replace("-","").replace(":","").replace(".","").replace(" ","")
        df.to_excel(f"{data_atual}.xlsx")
    else:
        df.to_excel(f"{nome_arquivo}.xlsx")
    print(f"Planilha criada com sucesso!")


def import_python() -> None:
    arquivo = input("Digite o nome do arquivo: ")
    caminho_arquivo = f"./{arquivo}.xlsx"
    df = pd.read_excel(caminho_arquivo)
    print(f"Dados importados com sucesso!\n")
    print(df)

def main():
    while True:
        menu()
        opcao = input("Digite a opção: ")

        if opcao == "0":
            print('Saindo...')
            break
        elif opcao == "1":
            export_python(dados)
        elif opcao == "2":
            import_python()
        else:
            print('Opção Inválida! Tente Novamente')

if __name__ == "__main__":
    main()