#Enzo Luciano Barros de Oliveira RM 559557
import os
os.system('cls')

def numero_inter(n1, n2, n3):
    if (n1 >= n2 and n1 <= n3) or (n1 <= n2 and n1 >= n3):
        return n1
    elif (n2 >= n1 and n2 <= n3) or (n2 <= n1 and n2 >= n3):
        return n2
    else:
        return n3

def ordem_crescente(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        if n2 <= n3:
            print(f'Ordem crescente: {n1}, {n2}, {n3}')
        else:
            print(f'Ordem crescente: {n1}, {n3}, {n2}')
    elif n2 <= n1 and n2 <= n3:
        if n1 <= n3:
            print(f'Ordem crescente: {n2}, {n1}, {n3}')
        else:
            print(f'Ordem crescente: {n2}, {n3}, {n1}')
    else:
        if n1 <= n2:
            print(f'Ordem crescente: {n3}, {n1}, {n2}')
        else:
            print(f'Ordem crescente: {n3}, {n2}, {n1}')

def tabuada(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')

def nota_valida(nota):
    return 0 <= nota <= 10

def principal():
    contadores = [0, 0, 0, 0]
    
    while True:
        print("0 - SAIR")
        print("1 - Número intermediário")
        print("2 - Ordem crescente")
        print("3 - Tabuada")
        print("4 - Nota válida")
        escolha = input("Escolha: ")

        if escolha == '0':
            break
        elif escolha == '1':
            contadores[0] += 1
            n1 = float(input("Digite o 1.o número: "))
            n2 = float(input("Digite o 2.o número: "))
            n3 = float(input("Digite o 3.o número: "))
            meio = numero_inter(n1, n2, n3)
            print(f"Número intermediário: {meio}")
        elif escolha == '2':
            contadores[1] += 1
            n1 = float(input("Digite o 1.o número: "))
            n2 = float(input("Digite o 2.o número: "))
            n3 = float(input("Digite o 3.o número: "))
            ordem_crescente(n1, n2, n3)
        elif escolha == '3':
            contadores[2] += 1
            n = int(input("Digite a tabuada: "))
            tabuada(n)
        elif escolha == '4':
            contadores[3] += 1
            nota = float(input("Digite uma nota: "))
            if nota_valida(nota):
                print(f"A nota {nota} é válida")
            else:
                print(f"A nota {nota} é inválida")
        else:
            print("Opção inválida!")

    total_execucoes = sum(contadores)
    if total_execucoes > 0:
        for i in range(4):
            contador = contadores[i]
            porcentagem = (contador / total_execucoes) * 100
            print(f"Rotina {i + 1} - {contador} vezes - {porcentagem}%")
    else:
        print("Nenhuma rotina foi executada.")

principal()
