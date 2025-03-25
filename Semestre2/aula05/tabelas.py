# Trabalhando com tabelas de memórias
dados = {
    "nome": "Edson",
    "idade": 50,
}
import os
os.system('cls')

pessoa = dict()
cadastro = list()

# Cadastrar registros até que seja digitado . (ponto) em nome
while True:
    pessoa['nome'] = input("Nome: ")
    if pessoa['nome'] == '.': break
    pessoa['idade'] = int(input("Idade: "))
    cadastro.append(pessoa.copy())

# Exibir os dados cadastrados
for i in range (0, len(cadastro), 1):
    print(f"Nome = {cadastro[i]['nome']}")
    print(f"Idade = {cadastro[i]['idade']}\n")