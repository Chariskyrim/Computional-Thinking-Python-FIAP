import os
os.system('cls')

#    0  1  2   3  4  <==== indices
v = [5, 9, 2 , 4, 8] # <==== valores

# exibindo o vetor inteiro
print(v)

# exibindo um elemento
print(v[4])

for i in range(0, 5, 1):
    v[i] = input(f"v[{i}] = ")

def preenche_vetor(vet: list) -> None:
    for i in range(0, 5, 1):
        vet[i] = input(f"v[{i}] = ")

def exibe_vetor(vet: list) -> None:
    for i in range(0, 5, 1):
        print(f"{vet[i]} ", end ='')
