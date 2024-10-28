# %% [markdown]
# ### Olá felpsipi

# %% [markdown]
# ### Aprendendo sobre listas <br>
# #### Aprendemos a utilizar os **principais** métodos que manipulam uma lista

# %% [markdown]
# Método list() - Inicia uma lista como vazia

# %%
lista = list()
print(lista)

# %% [markdown]
# Criando uma lista com valores 

# %%
lista = ["1ESPR", 1, "Edson", True, 56.7]
print(lista)

# %% [markdown]
# Método `append(elemento)` - insere um elemento no final da lista

# %%
lista.append("novo")
print(lista)

# %% [markdown]
# Método `insert(posição, elemento)` - Insere um elemento em qualquer posição válida da lista.

# %%
lista.insert(2, "FIAP")
print(lista)

# %% [markdown]
# Método `pop(posicao)` - Remove o elemento especificado via posicao

# %%
lista.pop()
print(lista)

# %% [markdown]
# Método `remove(elemento)` - Remove um elemento pelo conteúdo

# %%
lista.remove(True)
print(lista)

# %%
lista.insert(2, True)
print(lista)

# %% [markdown]
# Método index(elemento) - Retorna o indice do elemento citado

# %%
lista = [22, 57.7, "Lógica"]
indice = lista.index(57.7)
print(f"Índice = {indice}")

# %% [markdown]
# Método `count(elemento)` - Conta a ocorrencia de um mesmo elemento

# %%
lista = [22, 57.7, "Lógica", 22]
quantidade = lista.count(22)
print(f"Quantidade = {quantidade}")

# %% [markdown]
# Função len(lista) - Conta a quantidade de elementos

# %%
lista = [22, 57.7, "Lógica", 22]
quantidade = len(lista)
print(f"Quantidade = {quantidade}")

# %% [markdown]
# Função `sum(lista)` - soma os elementos da lista

# %%
lista = [22, 57.7, 22]
soma = sum(lista)
print(f"Soma = {soma}")

# %% [markdown]
# Concatenação + - Junta duas listas

# %%
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
print(f"Lista3 = {lista3}")


# %% [markdown]
# Método extended(lista) - Adiciona uma lista no final da outra

# %%
lista1 = [1, 2, 3]
print(f"Lista1 = {lista1}")
lista2 = [4, 5, 6]
print(f"Lista2 = {lista2}")
lista2.extend (lista1)
print(f"Lista2 = {lista2}")

# %%
l1 = [1, 2, 3]
l2 = l1
print(l1)
print(l2)
l1.append(10)
print(l1)
print(l2)

# %%
l1 = [1, 2, 3]
print(l1)
l2 = l1.copy()
l1.append(10)
print(l1)
print(l2)

# %%
lista = [19, 3, 25, 33, -5]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

# %%
lista = [19, 4, 25, 33, -5]
lista.reverse()
print(lista)

# %%
lista = [19, 4, 25, 33, -5]
print(lista)
lista.clear()
print(lista)

# %%
lista = [19, 4, 25, 33, -5]
print(lista)
del lista
#print(lista)


