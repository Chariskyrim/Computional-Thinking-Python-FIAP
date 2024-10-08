import os
os.system('cls')

# Dado um numero pelo usuario, exibir o seu positivo
num = int(input('Digite um numero: '))
if num < 0:
    # transformar em positivo
    num *= -1
print(num)