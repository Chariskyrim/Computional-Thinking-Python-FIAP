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


while True:
    print("\nMenu")
    print("1. Preencher Lista")
    print("2. Exibir o Conteúdo da LO")
    print("3. Contar quanto valores inteiros existem na LO")
    print("4. Contar quanto valores Floats existem na LO")
    print("5. Passar a LO por parâmetro e copiar na outra somente valores inteiros")
    print("6. Passar a LO por parâmetro e copiar na outra somente valores floats")
    print("7. Pegar uma String por parâmetro e retornar quantas vogais existem nela")
    print("8. Passar um parâmetro L ou R que elimina os espaços da esquerda ou direita")
    print("9. Retorna True caso o valor passado por parâmetro seja do tipo Float")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        lista = preencher_lista()