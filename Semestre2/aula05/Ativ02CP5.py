# Enzo Luciano Barros de Oliveira
# RM 559557 - 1ESPR

import os 
os.system('cls')

def exibir_menu():
    print("""
    MENU
    0 - SAIR
    1 - Cadastrar Funcionário
    2 - Consultar Funcionário
    3 - Listar Funcionários
    """)

funcionarios = []

while True:
    exibir_menu()
    escolha = input("Escolha: ")
    
    if escolha == '0':
        print("Saindo...")
        break
    elif escolha == '1':
        cpf = input("CPF: ")
        existe = False
        for f in funcionarios:
            if f["cpf"] == cpf:
                existe = True
                break
        if existe:
            print("Funcionário já cadastrado!\n")
        else:
            nome = input("Nome: ")
            salario = input("Salário: ")
            funcionarios.append({"cpf": cpf, "nome": nome, "salario": salario})
            print("Funcionário cadastrado!\n")
    elif escolha == '2':
        cpf = input("CPF para consulta: ")
        encontrado = False
        for f in funcionarios:
            if f["cpf"] == cpf:
                print(f"CPF: {f['cpf']}, Nome: {f['nome']}, Salário: {f['salario']}\n")
                encontrado = True
                break
        if not encontrado:
            print("Funcionário não encontrado.\n")
    elif escolha == '3':
        if not funcionarios:
            print("Nenhum funcionário cadastrado.\n")
        else:
            for f in funcionarios:
                print(f"CPF: {f['cpf']}, Nome: {f['nome']}, Salário: {f['salario']}")
            print()
    else:
        print("Opção inválida!\n")