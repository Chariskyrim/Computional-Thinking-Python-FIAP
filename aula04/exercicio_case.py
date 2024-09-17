"""
Exercício: Dado um número que representa do dia da semana, apresentar o dia da semana correspondente;
    Entrada 1: 5        Saída 1: Quinta-feira.
    Entrada 2: 1        Saída 2: Domingo.
    Entrada 3: 10       Saída 3: Dia Inválido.

"""

escolha = input("Escolha: ")


if escolha.isnumeric():
    escolha = int



match escolha:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Dia Inválido!")