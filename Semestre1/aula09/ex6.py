import os
os.system('cls')

v = [45, -89, 32, -12, 33]

def imprimir(vet) -> None:
    prim = vet[0]
    ultimo = vet[-1]
    print(f"{prim} {ultimo}")

imprimir(v)