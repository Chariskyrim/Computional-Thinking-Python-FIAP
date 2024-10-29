"""
Enzo Luciano Barros de Oliveira RM559557 1ESPR

1. Fazer um procedimento que preencha uma lista até que seja digitado ponto(.).
    45 4.6 Edson a False .
2. Fazer um procedimento que exiba os índices acompanhados dos elementos da lista no seguinte formato.
    0-45 | 1-4.6 | 2-Edson | 3-a | 4-False
3. Dada uma lista e um valor pelo via parâmetro, Fazer uma função que retorne True caso este valor exista ou False caso ele não exista. Ao final exibir “O valor foi encontrado” ou “O valor não foi encontrado”.
    Valor: 33 Não encontrado
4. Faça um procedimento que passe dois vetores por parâmetro e copie no segundo o valor do primeiro invertido. Ao final exibir as duas listas.  
    False | Edson | 4.6   | 45
    45    | 4.6   | Edson | False


Criar um menu onde o usuário possa interagir com estas funções até que ele não queira mais
"""

import os
os.system('cls')

def preencher_lista():
    lista = []
    while True:
        elemento = input("Digite um elemento (ou '.' para terminar): ")
        if elemento == '.':
            break
        lista.append(elemento)
    return lista

def indices(lista):
    for i in range(len(lista)):
        print(f"{i}-{lista[i]}", end=" | ")
    print()

def lista_formatada(lista):
    for i in range(len(lista)):
        if i > 0:
            print(" | ", end="")
        print(lista[i], end="")
    print()

def valor_existe(lista, valor):
    return valor in lista

def inverter(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

lista = []

while True:
    print("\nMenu:")
    print("1. Preencher lista")
    print("2. Exibir lista com índices")
    print("3. Verificar se valor existe na lista")
    print("4. Inverter lista e exibir")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        lista = preencher_lista()
    elif opcao == '2':
        indices(lista)
    elif opcao == '3':
        valor = input("Digite o valor a ser pesquisado: ")
        print("O valor foi encontrado" if valor_existe(lista, valor) else "O valor não foi encontrado")
    elif opcao == '4':
        lista_invertida = inverter(lista)
        lista_formatada(lista_invertida)
        lista_formatada(lista)
    elif opcao == '0':
        print("Encerrando programa.")
        break
    else:
        print("Opção inválida, tente novamente.")
