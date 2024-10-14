import os
os.system

# Retorno bool (True  ou False) - Se os dois parametros são negativos
def num_neg(n1: float, n2: float) -> bool:
    if n1 < 0 or n2 < 0:
        return True
    else:
        return False
    

# -------- chamada da função
print(num_neg(3, 6))    
    