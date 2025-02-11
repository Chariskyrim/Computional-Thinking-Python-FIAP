#Enzo Luciano Barros de Oliveira
#RM 559557

import os
os.system('cls')

def vogal_maiuscula(string):
    resultado = ""
    for char in string:
        if char in "aeiou":
            resultado += char.upper()
        else:
            resultado += char
    return resultado

def retorna_indices(nome, caractere):
    indices = []
    for i in range(len(nome)):
        if nome[i] == caractere:
            indices.append(i)
    return indices

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def eh_numero(string):
    if not string:
        return False
    if string[0] in ('+', '-'):
        string = string[1:]
    for char in string:
        if char not in '0123456789':
            return False
    return True

def cpf_completo(cpf):
    if len(cpf) != 9 or not cpf.isdigit():
        return "CPF inválido"
    
    pesos_primeiro = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_primeiro = sum(int(cpf[i]) * pesos_primeiro[i] for i in range(9))
    resto_primeiro = soma_primeiro % 11
    digito_primeiro = 11 - resto_primeiro if resto_primeiro < 10 else 0

    pesos_segundo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_segundo = sum(int(cpf[i]) * pesos_segundo[i] for i in range(10))
    resto_segundo = soma_segundo % 11
    digito_segundo = 11 - resto_segundo if resto_segundo < 10 else 0

    return f"{cpf}{digito_primeiro}{digito_segundo}"

def cpf_valido(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    pesos_primeiro = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_primeiro = sum(int(cpf[i]) * pesos_primeiro[i] for i in range(9))
    resto_primeiro = soma_primeiro % 11
    digito_primeiro = 11 - resto_primeiro if resto_primeiro < 10 else 0

    pesos_segundo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_segundo = sum(int(cpf[i]) * pesos_segundo[i] for i in range(10))
    resto_segundo = soma_segundo % 11
    digito_segundo = 11 - resto_segundo if resto_segundo < 10 else 0

    return cpf[-2:] == f"{digito_primeiro}{digito_segundo}"

def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Modificar as vogais de uma string para maiúsculas")
        print("2. Encontrar índices de um caractere em uma string")
        print("3. Verificar se uma string é um número")
        print("4. Verificar se uma string representa um número float")
        print("5. Calcular CPF completo (com base nos 9 primeiros dígitos)")
        print("6. Validar CPF completo")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            string = input("Digite a string: ")
            print("Resultado:", vogal_maiuscula(string))
        
        elif opcao == "2":
            nome = input("Digite o nome ou a string: ")
            caractere = input("Digite o caractere a ser buscado: ")
            print("Índices encontrados:", retorna_indices(nome, caractere))
        
        elif opcao == "3":
            string = input("Digite a string: ")
            print("É número?", eh_numero(string))
        
        elif opcao == "4":
            string = input("Digite a string: ")
            print("É um número float?", isfloat(string))
        
        elif opcao == "5":
            cpf = input("Digite os 9 primeiros dígitos do CPF: ")
            print("CPF completo:", cpf_completo(cpf))
        
        elif opcao == "6":
            cpf = input("Digite o CPF completo (somente números): ")
            print("O CPF é válido?", cpf_valido(cpf))
        
        elif opcao == "7":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

menu()
