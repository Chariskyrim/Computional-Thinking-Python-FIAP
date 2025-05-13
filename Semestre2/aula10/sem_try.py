import os
import oracledb
import pandas as pd

try:
    conn = oracledb.connect(user="pf1530", password="fiap2025", dsn='oracle.fiap.com.br:1521/ORCL')
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True

margem = ' ' * 4

print("----- CADASTRAR JOGO -----")
cpf = input(margem + "CPF (11 dígitos): ")
nome = input(margem + "Nome: ")
nome_jogo = input(margem + "Nome do Jogo: ")
tipo = input(margem + "Tipo do Jogo: ")
data_lancamento = int(input(margem + "Ano de Lançamento: "))

cadastro = f"""
INSERT INTO ATV_CP06_ENZO_LUCIANO (cpf, nome, nome_jogo, tipo, data_lancamento)
VALUES ('{cpf}', '{nome}', '{nome_jogo}', '{tipo}', {data_lancamento})
"""

inst_cadastro.execute(cadastro)
conn.commit()