#Enzo Luciano Barros de Oliveira
#RM559557 1ESPR

import os
os.system('cls')

def unicos(elementos) -> None:
    novo_Elem = set(elementos)
    return len(novo_Elem)

def duplicados(elementos) -> None:
    return len(elementos) - unicos(elementos)

def primeiro_elem(elementos):
    if elementos:
        elemento = next(iter(elementos))
        elementos.remove(elemento)
        return elemento
    return None 

def ultimo_elem(elementos):
    if elementos:
        ultimo = list(elementos)[-1]
        elementos.remove(ultimo)
        return ultimo
    return None

def calcular_remocao(elementos, elemento):
    if elemento not in elementos or len(elementos) != 10:
        return None  

    conjunto_copia = elementos.copy()
    removidos = 0

    for _ in range(5):
        if conjunto_copia:
            primeiro_elemento = list(conjunto_copia)[0]
            conjunto_copia.remove(primeiro_elemento)  
            if primeiro_elemento == elemento:
                removidos += 1  

    return (removidos / 5) * 100


elementos_unicos = input("Digite os elementos para a função 'unicos' (separados por espaço): ").split()
print(f"Quantidade de elementos únicos: {unicos(elementos_unicos)}")

elementos_duplicados = input("Digite os elementos para a função 'duplicados' (separados por espaço): ").split()
print(f"Quantidade de elementos duplicados: {duplicados(elementos_duplicados)}")

elementos_primeiro = input("Digite os elementos para a função 'primeiro_elem' (separados por espaço): ").split()
print(f"Primeiro elemento removido: {primeiro_elem(elementos_primeiro)}")

elementos_ultimo = input("Digite os elementos para a função 'ultimo_elem' (separados por espaço): ").split()
print(f"Último elemento removido: {ultimo_elem(elementos_ultimo)}")

elementos_remocao = input("Digite 10 elementos para a função 'calcular_remocao' (separados por espaço): ").split()
elemento_remover = input("Digite o elemento que você deseja calcular a remoção: ")

if len(elementos_remocao) == 10:
    print(f"Percentual de remoção do elemento: {calcular_remocao(elementos_remocao, elemento_remover)}%")
else:
    print("Erro: O número de elementos deve ser 10.")
