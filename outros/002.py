value = float(input('Digite o valor da compra: '))
user_choice = input('Você tem cupom de desconto, digite S para sim, todo o resto vai ser considerado não: ')
has_coupon = False
if user_choice == 'S':
    has_coupon = True


if has_coupon and value >= 20:
    discount = 20
else:
    discount = 0


result = value - discount

print(f'O valor da venda é {result:.2f}')
