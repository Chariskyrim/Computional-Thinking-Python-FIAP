# %% [markdown]
# ## Dicionários 
# 
# Criando um dicionário vazio

# %%
dados = dict()
print(dados)

# %% [markdown]
# Criando um dicionario com valores
# 
# Sintaxe:
# 
# nome_dicionario = {<br>
#     "key1": "value1",<br>
#     "key2": "value2"<br>
# }

# %%
dados = {
    "nome":"Edson de Oliveira",
    "idade": 50
}
print(dados)

# %% [markdown]
# Acrescentando uma key

# %%
dados["email"] = "prof.edson.oliveira@hotmail.com"
print(dados)

# %% [markdown]
# Exibindo os items

# %%
print(f"""
nome.....: {dados["nome"]}
Idade....: {dados["idade"]}
E-mail...: {dados["email"]}
""")

# %% [markdown]
# Exercício:
# 
# 1.Fazer um procedimento que leia o dicionario acima
# 
# 2.Fazer um procedimento que exiba o dicionario acima

# %%
def preenche_dicionario(d: dict) -> None:
    d["nome"] = input("Nome: ")
    d["idade"] = input("Idade")
    d["email"] = input("email: ")

def exibe_dicionario(d: dict) -> None:
    print(f"""
nome.....: {d["nome"]}
Idade....: {d["idade"]}
E-mail...: {d("email")}
""")

#preenche_dicionario(dados)
#exibe_dicionario(dados)    


# %% [markdown]
# Métodos que tratam dicionários
# 
# .values() mostra os conteúdos
# 
# .key() mostra as chaves
# 
# .items() mostra os dois

# %%
print(dados.values())
print(dados.keys())
print(dados.items())

# %%
dados["cel"] = "(11) 934443938"

print("usando o items():")
for k, v in dados.items():
    print(f"O/A  {k} é {v}")

print("\nusando o keys():")
for k in dados.keys():
    print(k)
print("\nusando o values():")
for v in dados.values():
    print(v)

# %% [markdown]
# Sincronizando dicionarios: update()

# %%
dicionario1 = {
    "Nome":"Enzo",
    "Idade":"20"
    }

dicionario2 = {
    "email":"jorge@gmail.com",
    "telefone":"(11) 987654321"
    }

print("Dicionario1: ",dicionario1)
print("Dicionario2: ",dicionario2)
dicionario1.update(dicionario2)
print("Dicionario1: ",dicionario1)
print("Dicionario2: ",dicionario2)

# %% [markdown]
# O pop() remove um elemento do dicionario pela chave

# %%
valor_removido = dicionario1.pop("telefone")
print(valor_removido)
print(dicionario1)

# %% [markdown]
# o metodo get() é usado para obter o valor de uma chave específica. Ele retorna o valor correspondente

# %%
valor = dicionario1.get("Nome")
print(valor)
print(dicionario1)


