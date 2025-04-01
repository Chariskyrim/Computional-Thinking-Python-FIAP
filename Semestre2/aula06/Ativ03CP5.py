# Enzo Luciano Barros de Oliveira
# RM559557 1ESPR

import os 
os.system('cls')

def menu():
    print("""
    Atividade 3 - CP5
    0 - SAIR
    1 - Nome do arquivo
    2 - Preencher o arquivo diretamente
    3 - Preencher o arquivo linha a linha
    4 - Exibir o arquivo integralmente
    5 - Exibir uma linha dada pelo usuário
    6 - Contar quantas linhas há no arquivo
    7 - Contar quantos caracteres há no arquivo
    """)
    return input("Escolha: ")

def definir_nome_arquivo():
    return input("Digite o nome do arquivo: ")

def preencher_arquivo_diretamente(arquivo):
    if arquivo:
        conteudo = input("Digite o conteúdo do arquivo: ")
        with open(arquivo, "w") as f:
            f.write(conteudo)
    else:
        print("Defina o nome do arquivo primeiro (opção 1)")

def preencher_arquivo_linha_a_linha(arquivo):
    if arquivo:
        with open(arquivo, "w") as f:
            while True:
                linha = input("Digite uma linha (ou 'sair' para terminar): ")
                if linha.lower() == "sair":
                    break
                f.write(linha + "\n")
    else:
        print("Defina o nome do arquivo primeiro (opção 1)")

def exibir_arquivo(arquivo):
    if arquivo:
        f = open(arquivo, "r")
        conteudo = f.read()
        f.close()
        print(conteudo)
    else:
        print("Arquivo não encontrado.")

def exibir_linha_especifica(arquivo):
    if arquivo:
        f = open(arquivo, "r")
        linhas = f.readlines()
        f.close()
        num_linha = int(input("Digite o número da linha desejada: "))
        if 0 <= num_linha < len(linhas):
            print(linhas[num_linha].strip())
        else:
            print("Linha fora do intervalo.")
    else:
        print("Arquivo não encontrado.")

def contar_linhas(arquivo):
    if arquivo:
        f = open(arquivo, "r")
        total_linhas = len(f.readlines())
        f.close()
        print(f"Total de linhas: {total_linhas}")
    else:
        print("Arquivo não encontrado.")

def contar_caracteres(arquivo):
    if arquivo:
        f = open(arquivo, "r")
        conteudo = f.read()
        f.close()
        total_caracteres = len(conteudo.replace("\n", ""))
        print(f"Total de caracteres: {total_caracteres}")
    else:
        print("Arquivo não encontrado.")

def main():
    arquivo = ""
    while True:
        opcao = menu()
        
        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            arquivo = definir_nome_arquivo()
        elif opcao == "2":
            preencher_arquivo_diretamente(arquivo)
        elif opcao == "3":
            preencher_arquivo_linha_a_linha(arquivo)
        elif opcao == "4":
            exibir_arquivo(arquivo)
        elif opcao == "5":
            exibir_linha_especifica(arquivo)
        elif opcao == "6":
            contar_linhas(arquivo)
        elif opcao == "7":
            contar_caracteres(arquivo)
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
