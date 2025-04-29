#Enzo Luciano Barros de Oliveira
#RM559557 - 1ESPR

import os
import json

os.system('cls' if os.name == 'nt' else 'clear')

if os.path.exists("registro.json"):
    with open("registro.json", "r") as file:
        pessoas = json.load(file)
else:
    pessoas = {
        'pessoa1': {
            'cpf': 44455566633,
            'nome': 'Edson',
            'cel': '11 998877662',
        },
        'pessoa2': {
            'cpf': 33344455522,
            'nome': 'Jorge',
            'cel': '11 987654321',
        },
        'pessoa3': {
            'cpf': 22244455577,
            'nome': 'Alan',
            'cel': '11 956748324',
        },
    }
    with open("registro.json", "w") as file:
        json.dump(pessoas, file, indent=4)

def salvar_dados():
    with open("registro.json", "w") as file:
        json.dump(pessoas, file, indent=4)

def cadastrar_novo_registro():
    try:
        cpf = int(input("Digite o CPF a ser cadastrado (somente números): "))
    except ValueError:
        print("CPF inválido! Deve conter apenas números.\n")
        return

    for dados in pessoas.values():
        if dados['cpf'] == cpf:
            print("CPF já cadastrado! Não é possível cadastrar novamente.\n")
            return

    nome = input("Digite o nome: ")
    cel = input("Digite o celular: ")

    nova_pessoa = f'pessoa{len(pessoas) + 1}'
    pessoas[nova_pessoa] = {
        'cpf': cpf,
        'nome': nome,
        'cel': cel,
    }
    salvar_dados()
    print("Pessoa cadastrada com sucesso!\n")

def listar_registros():
    if not pessoas:
        print("\nNenhum registro encontrado.\n")
        return
    
    print("\nRegistros atuais:")
    for chave, dados in pessoas.items():
        print(f"{chave}:")
        print(f"  CPF: {dados['cpf']}")
        print(f"  Nome: {dados['nome']}")
        print(f"  Celular: {dados['cel']}")
        print("-" * 20)
    print()

def editar_registro():
    try:
        cpf_busca = int(input("Digite o CPF da pessoa que deseja editar: "))
    except ValueError:
        print("CPF inválido! Deve conter apenas números.\n")
        return

    for chave, dados in pessoas.items():
        if dados['cpf'] == cpf_busca:
            print(f"Registro encontrado: {dados}")
            novo_nome = input("Digite o novo nome (deixe vazio para manter o atual): ")
            novo_cel = input("Digite o novo celular (deixe vazio para manter o atual): ")

            if novo_nome:
                dados['nome'] = novo_nome
            if novo_cel:
                dados['cel'] = novo_cel

            salvar_dados()
            print("Registro atualizado com sucesso!\n")
            return
    print("CPF não encontrado.\n")

def menu():
    while True:
        print("MENU\n")
        print("0. SAIR")
        print("1. Cadastrar novo Registro")
        print("2. Listar os registros")
        print("3. Editar um registro")
        
        escolha = input("\nEscolha: ").strip() 

        if escolha in ['0', '1', '2', '3']:
            if escolha == '0':
                print("Saindo...")
                break
            elif escolha == '1':
                cadastrar_novo_registro()
            elif escolha == '2':
                listar_registros()
            elif escolha == '3':
                editar_registro()
        else:
            print("Opção inválida.\n")


menu()
