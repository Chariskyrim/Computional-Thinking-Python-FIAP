import os
os.system('cls')

salario_Bruto = float(input('Digite seu salario bruto: '))
if salario_Bruto > 1412:
    inss = 0.09 * salario_Bruto
else:
    inss = 0.075 * salario_Bruto
 
result = salario_Bruto - inss
print(f'O valor do INSS será {inss:.2f} e o salário líquido será de {result:.2f}')



