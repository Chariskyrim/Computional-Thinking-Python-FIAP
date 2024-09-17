print(f"""
0 - sair
1 - cadastrar
2 - consultar
3 - editar
4 - excluir
      """)
escolha = int(input('Escolha: '))

match escolha:
    case 0:
        print('Saindo...')
    case 1:
        print('Cadastrando...')
    case 2:
        print('Consultando...')
    case 3:
        print('Editando...')
    case 4:
        print('Excluindo')
    case _:
        print('Opção Inválida...')


'''
print(f"""
0 - sair
1 - cadastrar
2 - consultar
3 - editar
4 - excluir
      """)
escolha = int(input('Escolha: '))
if escolha == 0:
    print('Saindo...')
elif escolha == 1:
    print('Cadastrando...')
elif escolha == 2:
    print('Consultando...')
elif escolha == 3:
    print('Editando...')
elif escolha == 4:
    print('Excluindo...')
else:
    print('Opção Inválida')
 
'''