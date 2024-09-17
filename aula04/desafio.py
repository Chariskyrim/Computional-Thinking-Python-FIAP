#Enzo Luciano Barros de Oliveira RM559557

import os
os.system('cls')

venda = float(input("Digite o valor da venda: "))
cupom = input("Você tem cupom de desconto? Digite Sim ou Não: ")


if cupom == 's':
    valor_cupom = 50
    print(f'Venda: R${venda}')
elif cupom == 'n':
    valor_cupom = 0
    print(f'Venda: R${venda}')



if venda > 1000:
    desconto = venda * (10 / 100)
else:
    desconto = venda * (5 / 100)


venda = venda - desconto - valor_cupom


print(f'Desconto: R${desconto}')
print(f'Cupom: R${valor_cupom}')
print(f'Venda Final: R${venda}')

