import os
os.system('cls')

def saudacao1() -> None:
    print ("Boa noite, usuario")

def saudacao3(usuario: str, hora: int) -> None:
    if hora >= 5 and hora <= 12 :
        print(f"Bom Dia, {usuario}")
    elif hora >= 12 and hora <= 18 :
        print(f"Boa Tarde, {usuario}")
    else:
        print(f"Boa Noite, {usuario}")

def maior3n(n1: float, n2: float, n3: float) -> float:
    maior = n1 
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior
    #JAMAIS USE PRINT OU INPUT DENTRO DE UMA FUNÇÂO



print(f"Maior = {maior3n(56, 76, 97)}")
num_maior = maior3n(34, 6.7, 45.9)
print(f"Maior = {num_maior}")