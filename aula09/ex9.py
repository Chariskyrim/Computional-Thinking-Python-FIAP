import os
os.system("cls")
 
v = [45, -89, 32, -12, 33]
 
n = len(v)
for i in range(n):
    for j in range(0, n-i-1):
        if v[j] > v[j+1]:
            # Trocar os elementos
            v[j], v[j+1] = v[j+1], v[j]
 
# Exibindo o vetor ordenado
print("Vetor ordenado:", v)