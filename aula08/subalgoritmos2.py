import os
os.system

# Retorno bool (True  ou False) - Se os dois parametros são negativos
def num_neg(n1: float, n2: float) -> bool:
    return n1 < 0 or n2 < 0
    
    """
    if n1 < 0 or n2 < 0:
        return True
    else:
        return False
    """

# -------- chamada da função
if num_neg(3, -6): # == True:
    print("Um (ou os dois) dos numeros são negativos ")
else:
    print("Os numeros não são negativos ")

# parametros default - Saudacao
os.system("cls")

def saudacao(usuario: str = "Enzo", hora: int = 19) -> None:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg}, {usuario}!")

# --------- chamada da função
saudacao(hora = 12)

# parametros *args - media
os.system("cls")
def media_numeros(*args ) -> float:
    soma = 0
    for numero in args:
        soma += numero
    return soma / len(args)


# --------------- chamada da funcao
print(media_numeros(5,4,6,3,4,5,6,0))

# Subalgoritmos agrupados - media fiap
os.system('cls')
def menor_3n (n1: float, n2: float, n3: float) -> float:
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

def media_cp (n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3 - menor_3n(n1, n2, n3)) / 2

#chamada da funcao
print(media_cp(6, 2, 8))

os.system('cls')

def media_cpb(n1: float, n2: float, n3: float) -> float:
    
    def menor_3nb(n1: float, n2: float, n3: float) -> float:
        menor = n1
        if n2 < menor:
            menor = n2
        if n3 < menor:
            menor = n3
        return menor
    
    return (n1 + n2 + n3 - menor_3nb(n1, n2, n3)) / 2


print(media_cpb(4, 5, 6))
"""
youtube: @edsonoliveiraprof
insta: @beabaprogramacao
"""