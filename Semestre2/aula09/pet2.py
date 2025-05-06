import os
os.system('cls')

import oracledb

try:
    conn = oracledb.connect(user="pf1530", password = "fiap2025", dsn = 'oracle.fiap.com.br:1521/ORCL ')
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False
else:
    # Flag para executar a aplicação
    conexao = True
