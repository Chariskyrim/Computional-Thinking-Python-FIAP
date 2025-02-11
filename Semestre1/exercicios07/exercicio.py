import os
os.system('cls')

hora = int(input("Digite o horário atual: "))

if hora >= 5 and hora <= 12 :
    print("Bom Dia")
elif hora >= 12 and hora <= 18 :
    print("Boa Tarde")
else:
    print("Boa Noite")