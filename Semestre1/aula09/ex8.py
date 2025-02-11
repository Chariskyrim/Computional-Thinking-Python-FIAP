import os
os.system("cls")
 
v = [45, -89, 32, -12, 33]
 
num = int(input("Digite o número que você deseja comparar: "))
s = False
 
for i in v:
    if num == i:
        s = True
 
if s == True:
    print(f"O número: {num} está incluído no vetor")
else:
    print(f"O número: {num} não está incluído no vetor")