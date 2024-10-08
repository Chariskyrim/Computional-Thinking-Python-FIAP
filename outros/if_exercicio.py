import os
os.system('cls')

num = float
(input('Digite um numero: '))

if num > 100:
    num = num - num*0.10 
print(f'Resultado com desconto: {num}')
