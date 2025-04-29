import os 
os.system('cls')

# ARQUIVOS JSON
# Criando um dicionário

contato = {
    'nome':'Edson de Oliveira',
    'idade':50,
    'cel':'11947262525',
}

import json
# Gravando o dicionário em um arquivo json
with open("teste.json", "w") as arq:
    json.dump(contato, arq)

# lendo o arquivo json
with open("teste.json", "r") as arq:
    dados_lidos = json.load(arq)
    print("Dados colhidos do arquivo json:")
    print(dados_lidos)
    for k, v in dados_lidos.items():
        print(f"{k:10} -> {v}")

os.system('cls')
# modificando os dados de um arquivo json
with open("teste.json", "r") as arq:
    dados_modificados = json.load(arq) #dados jogados para uma lista diferente

print("Exibindo os dados antes da modificação:")
print(dados_modificados)
# modificando os dados no dicionario
dados_modificados["idade"] = int(input("Idade: "))
dados_modificados["cel"] = input("Celular: ")

# Gravando o dicionario modificado no arquivo json
with open("teste.json", "w") as arq:
    json.dump(dados_modificados, arq)

print("Exibindo os dados antes da modificação:")
print(dados_modificados)

for k, v in dados_modificados.items():
    print(f"{k:10} -> {v}")