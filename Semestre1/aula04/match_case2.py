# Verificar se o dia informado faz parte do final de semana ou dia útil

dia = 'Domingo'
"""
match dia:
    case 'Sábado':
        print('Final de semana')
    case 'Domingo':
        print('Final de semana')
    case _:
        print('Dia útil')
"""

if dia == 'Sábado'or dia == 'Domingo':
    print('Final de semana')
else:
    print('Dia útil')