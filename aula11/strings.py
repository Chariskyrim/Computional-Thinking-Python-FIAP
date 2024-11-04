import os
os.system("cls")

frase = "Agora veremos como o fatiamento funciona com strings"
print(frase)
print(frase[2])
print(frase[7:15])
print(frase[::-1])
print(frase[::3])
print(frase[32:5:-3])
print(frase[2:20:2])
# metodos find - encontra o indice da primeira ocorrencia
print(frase.find("veremos"))
print(frase.find("como"))
print(frase.find("como", 30, 40))
nome = ["Edson", "de", "Oliveira"]
# .join - transforma uma lista de strings em uma string
print("".join(nome))
print(" ".join(nome))
print("abacate".join(nome))
# split - transforma uma string em uma lista de strings
nome = "Edson de Oliveira"
print(nome.split())
print(len(nome.split()))
print(nome.split('e'))
print(nome.split('de'))
# Replace - substitui trechos de uma string por outro trecho
nome = "Edson de Oliveira"
nome_new1 = nome.replace('e','E')
print(nome_new1)

nome_new2 = nome.replace('de','DE')
print(nome_new2)
nome_new3 = nome.replace(' ', '_')
print(nome_new3)
nome_new4 = nome.replace(' ', '_',1)
print(nome_new4)
# strip - eimina os espaços das extremidades
texto = "   elimina os espaços das extremidades   "
texto2 = texto.strip()
print(f"'{texto}'|'{texto2}'")
# operador in - encontra algo numa lista
lista = [1, 2, 3, 4, 5, 6]
print(3 in lista)
print(8 in lista)
nome = "Edson de Oliveira"
print('u' in nome)
print('x' not in nome)