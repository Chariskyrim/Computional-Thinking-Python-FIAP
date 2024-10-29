import os
os.system('cls')

def preencher_lista():
    """Preenche uma lista até que o usuário digite '.'"""
    lista = []
    while True:
        elemento = input("Digite um elemento (ou '.' para terminar): ")
        if elemento == '.':
            break
        lista.append(elemento)
    return lista

def indices(lista):
    """Exibe os índices e elementos da lista"""
    for i in range(len(lista)):
        print(f"{i}-{lista[i]}", end=" | ")
    print()

def lista_formatada(lista):
    """Exibe a lista formatada com elementos separados por '|'"""
    for i in range(len(lista)):
        if i > 0:
            print(" | ", end="")
        print(lista[i], end="")
    print()

def valor_existe(lista, valor):
    """Verifica se um valor existe na lista"""
    return valor in lista

def inverter(lista):
    """Inverte a lista usando um loop"""
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
