"""PARA OS PRESENTES NA SALA DE AULA PODE SER FEITO EM DUPLA
SOMENTE UM INTEGRANTE ENVIA NO TEAMS
CONTANTO QUE DEIXE OS NOMES COMENTADOS NAS PRIMEIRAS LINHAS

Atividade 3 - CP$

Crie um dicionário relacionado a livros (acrescente 5 campos ao 
seu gosto) e crie o seguinte menu:

0 - Sair
1 - Preencher o dicionário
2 - Listar o dicionario
3 - Acrescentar um campo
4 - Excluir um campo
5 - Retornar o conteúdo de um campo

Deixe o menu funcional. Será melhor avaliado os que fizerem 
subalgoritmos nos itens do menu"""

import os
os.system('cls')

def preenche_dicionario(d: dict) -> None:
    d["nome"] = input("Nome do Livro: ")
    d["autor"] = input("Nome do Autor: ")
    d["genero"] = input("Gênero do livro: ")
    d["data"] = input("Data de Publicação: ")
    d["ISBN"] = input("ISBN: ")

def lista_dicionario(d: dict) -> None:
    if d:
        for k, v in d.items():
            print(f" {k} : {v} ")
    else:
        print("O dicionário está vazio")
    
def adiciona_campo(d: dict) -> None:
    k = input("Nome do novo campo: ")
    v = input(f"Valor para {k}:")
    d[k] = v

def excluir_campo(d: dict) -> None:
    k = input("Nome do campo a ser removido: ")
    if k in d:
        del d[k]
        print(f"Campo {k} removido com sucesso!")
    else:
        print("Campo não encontrado!")

def retorno_campo(d: dict) -> None:
    k = input('Nome do campo a ser retornado: ')
    if k in d:
        print(f"{d.get(k)}")
    else:
        print("Campo não encontrado!")

def menu():
    dicionario_livro = {}
    while True:
        print("\nMenu")
        print("0 - Sair")
        print("1 - Preencher o dicionário: ")
        print("2 - Listar o dicionario: ")
        print("3 - Acrescentar um campo: ")
        print("4 - Excluir um campo: ")
        print("5 - Retornar o conteúdo de um campo: ")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            preenche_dicionario(dicionario_livro)
        elif opcao == "2":
            lista_dicionario(dicionario_livro)
        elif opcao == "3":
            adiciona_campo(dicionario_livro)
        elif opcao == "4":
            excluir_campo(dicionario_livro)
        elif opcao == "5":
            retorno_campo(dicionario_livro)
        else:
            print("Opção inválida! Tente novamente")
    
menu()