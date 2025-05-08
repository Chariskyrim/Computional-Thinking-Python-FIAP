# Enzo Luciano Barros de Oliveira
# RM 559557

import os
os.system('cls')

def calculadora(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Erro: divisão por zero'
    else:
        return 'Operador inválido'

print("\n--- Calculadora ---")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite o operador (+, -, *, /): ")
resultado = calculadora(n1, n2, op)
print("Resultado:", resultado)


def ordem_crescente(a, b, c):
    return a < b < c

print("\n--- Ordem crescente ---")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
resultado = ordem_crescente(a, b, c)
print("Estão em ordem crescente?", resultado)


def somar_pares(n):
    return sum(i for i in range(2, n + 1, 2))

print("\n--- Somar pares ---")
n = int(input("Digite um número: "))
resultado = somar_pares(n)
print("Soma dos pares até", n, "=", resultado)


def eh_mapa(lista):
    if not isinstance(lista, list) or len(lista) == 0:
        return False
    for item in lista:
        if item not in ('.', 'o'):
            return False
    return True

print("\n--- Eh mapa ---")
entrada = input("Digite os caracteres separados por espaço (ex: . o . o): ")
lista = entrada.split()
resultado = eh_mapa(lista)
print("É um mapa válido?", resultado)


import math

def perto_quad_perfeito(n):
    raiz = math.isqrt(n)
    return (raiz ** 2 == n) or ((raiz + 1) ** 2 == n) or ((raiz - 1) ** 2 == n)

print("\n--- Quase quadrado ---")
n = int(input("Digite um número: "))
resultado = perto_quad_perfeito(n)
print("É quadrado perfeito ou perto?", resultado)
