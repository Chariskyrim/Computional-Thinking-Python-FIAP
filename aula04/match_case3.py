import os
os.system('cls')




x = 6
match x:
    case bool():
        print('Variável booleana')
    case str():
        print('Variável string')
    case float():
        print('Variável float')
    case int():
        print('Variável inteira')
    case _:
        print('variavel de tipo não primitivo')