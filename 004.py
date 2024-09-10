salario_bruto = float(input('Digite seu salario: '))
porcentagem_inss = 0
if salario_bruto < 0:
    print('Não existe salario negativo')
else:

    if salario_bruto <= 1302.01:
        porcentagem_inss = 0.075
    elif salario_bruto <= 2571.29:
        porcentagem_inss = 0.09
    elif salario_bruto <= 3856.94:
        porcentagem_inss = 0.12
    elif salario_bruto <= 7507.49:
        porcentagem_inss = 0.14

    inss = salario_bruto * porcentagem_inss 
    if salario_bruto > 7507.49:
        inss = 0.14 * 7507.49

    salario_liquido = salario_bruto - inss
    print(f'Salário Bruto: {salario_bruto:.2f}')
    print(f'INSS: {inss:.2f}')
    print(f'Salario Liquido: {salario_liquido:.2f}')

