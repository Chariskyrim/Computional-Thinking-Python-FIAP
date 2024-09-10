value = float(input('Digite o valor da sua compra: '))
if value > 500:
    discount = 0.12 * value
else:
    discount = 0.06 * value

result = value - discount
print(f'Valor com Desconto: {result}')