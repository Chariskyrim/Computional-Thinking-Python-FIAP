import os
import json
os.system('cls')

# Criando um dicionário aninhado
pessoas = {
    'pessoas1':{
        'nome': 'Edson',
        'idade': 50,
        'email': 'edson@gmail.com',
    },
    'pessoas2':{
        'nome': 'Ester',
        'idade': 40,
        'email': 'ester@gmail.com',
    },
    'pessoas3':{
        'nome': 'Laura',
        'idade': 80,
        'email': 'laura@gmail.com',
    },
}

# criando o objeto json
pessoas_json = json.dumps(pessoas, indent = 4)
print('\nExibindo o dicionário: ')
print(pessoas)
print('\nExibindo o objeto json: ')
print(pessoas_json)

# Gravando no arquivo json
with open("arquivo.json", "w") as file:
    file.write(pessoas_json)

# Lendo o arquivo json
with open("arquivo.json", "r") as file:
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

print(pessoas)
print(pessoas_json)

# Apresentação para o usuário
os.system('cls')
for k, v in pessoas.items():
    print(f"Registro...: {k}")
    for k1, v1 in v.items():
        print(f"\t{k1}: {v1}")