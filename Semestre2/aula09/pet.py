import os
os.system('cls')
import oracledb

"""
try:
    comandos a serem executados
except:
    caso haja falha
finally:
    executa independentemente de ter excessoes ou nao
"""

# problema: dividir dois numeros dados pelo usuario

# n1 = float(input("Numero1: "))
# n2 = float(input("Numero2: "))
# resp = n1 / n2

try:
    n1 = float(input("Numero1: "))
    n2 = float(input("Numero2: "))
    resp = n1 / n2
except ValueError:
    print("Digite dados numéricos!")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except:
    print("Chame a NASA")
else:
    print(resp)
finally:
    print("Obrigado por utilizar o nosso sistema!")
