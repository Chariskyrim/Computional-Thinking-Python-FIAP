import os
os.system('cls')
"""
Características dos SETS
1. Armazena dados não duplicados
2. Suporta operações aritméticas de conjuntos (união, intersecção..)
3. Não é possível modificar os dados existentes
4. Suporta elementos de quaisquer tipos 
5. São imutáveis porque não tem índices
6. São escritos entre chaves
"""
# Criando Sets vazios
conjunto = {}
conjunto = set()
print(conjunto)

# Criando Set a partir de uma lista
numeros = [1, 2, 2, 3, 3, 3, 3] # lista
conjunto = set(numeros)
print("lista = ", numeros)
print("sets =", conjunto)

# Inserindo elementos em um set
numeros = [1, 2, 2, 3, 3, 3, 3] # lista
conjunto = set()
for num in numeros:
    conjunto.add(num) # add adiciona um valor no set(conjunto)
conjunto.add(5)
print("lista = ", numeros)
print("sets =", conjunto)

# Removendo elementos de um set (remove)
os.system('cls')
nums = set([1, 2, 2, 2, 3, 3, 3])
print(nums)
nums.remove(2) # esse avisa se tem ou não um valor
print(nums)
nums.remove(3)
print(nums)

# Removendo elementos de um set com discard
os.system('cls')
nums = set([1, 2, 2, 2, 3, 3, 3])
print(nums)
nums.discard(2) # esse não avisa 
nums.discard(8)
print(nums)

# Removendo todos elementos de uma vez
os.system('cls')
nums = set([1, 2, 2, 2, 3, 3, 3])
print(nums)
nums.clear()
print(nums)

# =============== OPERAÇÕES MATEMATICAS COM SETS
# União de conjuntos (union)
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.union(b) # ele traz em ordem crescente
print("a = ",a)
print("a = ",b)
print("a = ",c)

# União de conjuntos utilizando | (union)
os.system('cls')
a = {0, 1, 10, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a | b
print("a =", a)
print("a = ",b)
print("a = ",c)

# intersecção - método intersection (utilizando o &)
os.system('cls')
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.intersection(b) #outra opção = a & b
print("a =", a)
print("a = ",b)
print("a = ",c)

# Inicialização de um set de string
os.system('cls')
planetas = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planetas)


#Associação in em sets
print('Ceres' in planetas)
print('Lua' in planetas)
print('eris' in planetas)

# Efetuando casting
astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
print(astros)
astros_sets = set(astros)
print(astros_sets)

# Comparando sets 
# Utilizando o == e !=
os.system('cls')
planetas1 = {'Terra', 'Venus', 'Mercurio', 'Marte'}
planetas2 = {'Terra', 'Venus', 'Mercurio', 'Marte', 'Saturno'}
print(planetas1 == planetas2)
print(planetas1 != planetas2)

# Verifica se o conjunto à esquerda é um subconjunto da direita
os.system('cls')
planetas1 = {'Terra', 'Venus', 'Mercurio', 'Marte'}
planetas2 = {'Terra', 'Venus', 'Mercurio', 'Marte', 'Saturno'}
print(planetas1 < planetas2)

# diference ou - : A diferença entre dois conjuntos é um conjunto contendo os elementos do
# conjunto à esquerda que não estão no conjunto à direita do operador
os.system('cls')
planetas1 = {'Venus', 'Mercurio', 'Terra', 'Netuno', 'Marte'} 
planetas2 = {'Terra', 'Jupiter', 'Urano', 'Saturno', 'Marte'}
print(planetas1 - planetas2)
print(planetas1.difference(planetas2))

#Diferença simética - apenas os itens não repetidos
os.system('cls')
planetas1 = {'Venus', 'Mercurio', 'Terra', 'Netuno', 'Marte'} 
planetas2 = {'Terra', 'Jupiter', 'Urano', 'Saturno', 'Marte'}
print(planetas1 ^ planetas2)
print(planetas1.symmetric_difference(planetas2))

# Conjuntos disjuntos - não possuem nenhum elemento em comum
os.system('cls')
planetas1 = {'Venus', 'Mercurio', 'Terra', 'Netuno', 'Marte'}
planetas2 = {'Terra', 'Jupiter', 'Urano', 'Saturno', 'Marte'}
planetas3 = {'Jupiter', 'Urano', 'Saturno'}
print(planetas1.isdisjoint(planetas2))
print(planetas1.isdisjoint(planetas3))

planetas1 |= planetas2 #juntou
print(planetas1)

#União com o |= ou update()
#Realiza uma operação de união, mas ordenando aleatoriamente
os.system('cls')
planetas1 = {'Venus', 'Mercurio', 'Terra', 'Netuno', 'Marte', 'Marte'}
planetas2 = {'Terra', 'Jupiter', 'Urano', 'Saturno', 'Marte'}
planetas1 |= planetas2
planetas1.update(planetas2) #faz a mesma coisa que o |=
print(planetas1)

# Copiando conjuntos
os.system('cls')
p1 = {'Venus', 'Mercurio', 'Terra', 'Netuno', 'Marte'}
p2 = p1.copy()
print(p1)
print(p2)

# Pop() remove um elemento aleatorio
os.system('cls')
p1 = {'Venus', 'Mercurio', 'Terra', 'Netuno', 'Marte'}
print(p1)
x = p1.pop()
print(p1)
print(x)