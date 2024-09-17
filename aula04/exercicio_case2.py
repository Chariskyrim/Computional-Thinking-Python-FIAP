import os
os.system('cls')


'''
Exercicios:
1. Dados os 4 dígitos da placa antiga de um automóvel em uma variavel inteira, informe o dia do rodízio.

Final 1 ou 2: Segunda-feira
Final 3 ou 4: Terça-feira
Final 5 ou 6: Quarta-feira
Final 7 ou 8: Quinta-feira
Final 9 ou 0: Sexta-feira
....

Entrada 1: 3644      Saída 1: Terça-feira
Entrada 2: 5370      Saída 2: Sexta-feira

'''

placa = int(input('Digite o número da sua placa: '))

match placa % 10:
    case 1 | 2:
        print('Segunda')
    case 3 | 4:
        print('Terça')
    case 5 | 6:
        print('Quarta')
    case 7 | 8:
        print('Quinta')
    case 9 | 0:
        print('Sexta')
