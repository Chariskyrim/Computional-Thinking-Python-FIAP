# MANIPULAÇÃO DE ARQUIVOS
"""
MODOS DE ABERTURA
'w' | write - gravação
'r' | read - leitura
'a' | append - edição
'+' | leitura e gravação
"""
# Função: open() -> Abre um arquivo
# Sintaxe:
#  <objeto> = open("<nome_arquivo>", "<modo_de_abertura")

import os
os.system("cls")
"""
arq = open("arquivo1.txt", "w", encoding = "utf-8")
# write() é o método que grava uma informação no arquivo
arq.write("Ótimo! gravamos dados no arquivo\n")
arq.write("Nova linha")
arq.close() # close() fecha o arquivo

print("Arquivo gravado!")
"""

# Lendo o conteúdo de um arquivo
"""
arq = open("arquivo1.txt", "r", encoding = "utf-8")
print("Conteudo do arquivo:")
print(arq.read()) # lê o arquivo na íntegra
arq.close()
"""

# Editando um arquivo: modo de abertura 'a'
"""
arq = open("arquivo2.txt", "a", encoding = "utf-8")
arq.write("\nInseri uma nova linha!")
arq.close()

# Operador de contexto: with
# Todos os comandos endentados serão gerenciados pelo with.
# Não usamos mais o close()
with open("arquivo3.txt", "w+", encoding = "utf-8") as arq:
    arq.write("Gravando linha 1\n")
    arq.write("Gravando linha 2\n")
    arq.write("Gravando linha 3\n")
    arq.seek(5) # posiciona o cursor em algum ponto do arquivo
    print(arq.read())

with open("arquivo4.txt", "w+", encoding = "utf-8") as arq:
    arq.write("01234567890123\n")
    arq.write("Paralelepipedo\n")
    arq.seek(5) # posiciona o cursor em algum ponto do arquivo
    print(arq.read())

# readline() - retorna uma linha a partir do cursor
with open("arquivo5.txt", "w+", encoding = "utf-8") as arq:
    arq.write("Neste exemplo\n")
    arq.write("estamos treinando\n")
    arq.write("o método readlines()\n")
    arq.seek(20)
    print(arq.readline())

# readlines() - armazena todas as linhas do arquivo 
# em uma lista

os.system("cls")
with open("arquivo5.txt", "w+", encoding = "utf-8") as arq:
    arq.write("Neste exemplo\n")
    arq.write("estamos treinando\n")
    arq.write("o método readlines()\n")
    arq.seek(0)
    os.system("cls")
    print("Situação da lista:")
    lista_linhas = arq.readlines()
    print(lista_linhas)
    print(f"Linha 2: {lista_linhas[1]}")
    print(f"Tamanho da linha 3: {len(lista_linhas[2])}")
    arq.seek(0)
      
    for linha in arq.readlines():
        print(linha, end='')

    arq.seek(0)
    for num_linha, linha in enumerate(arq.readlines()):
        print(f"{num_linha}. {linha}", end='')

"""
os.system("cls")
# writelines(): gravando valias linhas em um arquivo
with open("arquivo7.txt", "w+", encoding = "utf-8") as arq:
    print("Gravando uma linha por vez")
    while True:
        linha = input("Linha: ")
        if linha != "":
            arq.write(linha + "\n")
        else:
            break
    print("Exibindo a gravacao")
    arq.seek(0)
    print(arq.read())

with open("arquivo7.txt", "w+", encoding = "utf-8") as arq:
    print("Gravando uma linha por vez")
    documento=[]
    while True:
        linha = input("Linha: ")
        if linha != "":
            documento.append(linha + "\n")
        else:
            break
    arq.writelines(documento) # grava a lista no arquivo
    print("Exibindo a gravacao")
    arq.seek(0)
    print(arq.read())