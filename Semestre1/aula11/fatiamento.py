import os
os.system("cls")
#          0   1   2   3   4   5   6   7   8   9
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#         -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
print(numeros)
print(numeros[3:7])
print(numeros[-4:-1])
print(numeros[0], numeros[-1])
#            [inicio:fim:incremento]
print(numeros[1:9:2])
print(numeros[8:1:-2])
print(numeros[-3:])
print(numeros[::-1])
l1 = numeros[1:9:2]
print(numeros, l1)