#Enzo Luciano Barros de Oliveira RM 559557

"""
1. Dado um numero por parâmetro, retornar o próximo. (FUNÇÃO)
x = prox_num(45) # x valerá 46

2. Dado um número por parâmetro, retornar o dobro. (FUNÇÃO)
x = dobro(25) # x valerá 50

3. Dados os valores de a, b e c por parâmetro, retornar o delta. (FUNÇÃO)
x = calc_delta(1, 2, 3) # x valerá -8

4. Dados 2 nomes por parâmetro, exibir em ordem alfabetica. (PROCEDIMENTO)
nome_ordem("Jonas", "Adriana") # Exibirá na tela Adriana e Jonas

5. Dado um numero por parâmetro, calcular e retornar o seu Fatorial (FUNÇÃO)
x = fatorial(4) # x valerá 24 => 4! = 4 . 3 . 4 . 1 = 24

6. Dada a base e o expoente por parâmetro, calcular a potencia.
x = potencia(2, 3) # x valerá 8

ORIENTAÇÕES:
READEQUEM TODOS OS EXERCÍCIOS AOS NOMES SUGERIDOS NO ENUNCIADO.
EM TODOS OS EXERCÍCIOS NÃO UTILIZAR FUNÇÕES PRÓPRIAS DO PYTHON, SIM DECISÕES, LAÇOS... CONCEITOS VISTOS EM AULA.
DESENVOLVA TUDO EM SOMENTE UM ARQUIVO .PY
ENVIE SOMENTE O PY SEM COMPRIMÍ-LO
ARQUIVOS ANEXADOS APÓS 22H55 SERÃO CONSIDERADOS EM ATRASO (perderá pontos)
"""

import os
os.system('cls')

# 1 Dado um numero por parâmetro, retornar o próximo:
def prox_num(num) -> None:
    num = num + 1
    return num

print(f"{prox_num(56)}")
num = prox_num(34)
print(f"{num}")

# 2 Dado um número por parâmetro, retornar o dobro:
def dobro_num(num) -> None:
    num = num * 2
    return num

print(f"{dobro_num(10)}")
num = dobro_num(15)
print(f"{num}")

# 3 Dados os valores de a, b e c por parâmetro, retornar o delta:
def delta_num(num1: int, num2: int, num3: int) -> int:
    num = num2 ** 2 - 4 * num1 * num3
    return num

print(f"{delta_num(1, 2, 3)}")
num = delta_num(2, 3, 4)
print(f"{num}")

# 4 Dados 2 nomes por parâmetro, exibir em ordem alfabetica:
def nome_ordem(nome1: str, nome2: str) -> str:
    if nome1 < nome2:
        print(nome1)
        return nome2
    else:
        print(nome2)
        return nome1
    
print(f"{nome_ordem("Jonas", "Adriana")}")

# 5 Dado um numero por parâmetro, calcular e retornar o seu Fatorial:
def fatorial(num) -> None:
        if num == 0 or num == 1:
            return 1
        else:
            return num * fatorial(num - 1)

print(f"{fatorial(4)}")

# 6 Dada a base e o expoente por parâmetro, calcular a potencia:
def potencia(base, expoente):
    return base ** expoente

print(f"{potencia(2, 3)}")