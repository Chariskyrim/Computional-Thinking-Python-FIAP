# RM 559557
# Enzo Luciano Barros de Oliveira

# Instalação do pip (link de referência):
# https://medium.com/@nara.guimaraes/instalando-o-pip-nolinux-windows-e-macos-um-guia-passo-a-passo-cc7b6d752b31

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

while conexao:
    os.system('cls')
    print("------- CRUD - JOGOS -------")
    print("""
    1 - Cadastrar Jogo
    2 - Listar Jogos
    3 - Alterar Jogo
    4 - Excluir Jogo
    5 - Excluir Todos os Jogos
    6 - SAIR
    """)

    escolha = input(margem + "Escolha -> ")

    if escolha.isdigit():
        escolha = int(escolha)
    else:
        escolha = 6
        print("Digite um número. Reinicie a Aplicação!")
        os.system('cls')
        continue

    match escolha:
        case 1:
            try:
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
            except ValueError:
                print("Digite um número no ano de lançamento!")
            except Exception as e:
                print("Erro na transação do BD:", e)
            else:
                print("##### Dados GRAVADOS #####")

        case 2:
            print("----- LISTAR JOGOS -----")
            inst_consulta.execute('SELECT * FROM ATV_CP06_ENZO_LUCIANO')
            data = inst_consulta.fetchall()

            if not data:
                print(f"Não há Jogos cadastrados!")
            else:
                dados_df = pd.DataFrame(data, columns=['CPF', 'Nome', 'Nome do Jogo', 'Tipo do Jogo', 'Ano de Lançamento'])
                print(dados_df)
                print("##### LISTADOS! #####")

        case 3:
            try:
                print("----- ALTERAR DADOS DO JOGO -----")
                cpf = input(margem + "Digite o CPF do cadastro a alterar: ")

                consulta = f"SELECT * FROM ATV_CP06_ENZO_LUCIANO WHERE cpf = '{cpf}'"
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()

                if not data:
                    print(f"Não há jogo cadastrado com o CPF = {cpf}")
                    input("Pressione ENTER")
                else:
                    novo_nome = input(margem + "Novo Nome: ")
                    novo_nome_jogo = input(margem + "Novo Nome do Jogo: ")
                    novo_tipo_jogo = input(margem + "Novo Tipo de Jogo: ")
                    novo_data_lancamento = int(input(margem + "Novo Ano de Lançamento: "))

                    alteracao = f"""
                    UPDATE ATV_CP06_ENZO_LUCIANO
                    SET nome='{novo_nome}', nome_jogo='{novo_nome_jogo}', tipo='{novo_tipo_jogo}', data_lancamento={novo_data_lancamento}
                    WHERE cpf='{cpf}'
                    """

                    inst_alteracao.execute(alteracao)
                    conn.commit()
            except ValueError:
                print("Digite um número no ano de lançamento!")
            except Exception as e:
                print("Erro na transação do BD:", e)
            else:
                print("##### Dados ATUALIZADOS! #####")

        case 4:
            print("----- EXCLUIR JOGO -----")
            cpf = input(margem + "Digite o CPF do cadastro a excluir: ")

            consulta = f"SELECT * FROM ATV_CP06_ENZO_LUCIANO WHERE cpf = '{cpf}'"
            inst_consulta.execute(consulta)
            data = inst_consulta.fetchall()

            if not data:
                print(f"Não há jogo cadastrado com o CPF = {cpf}")
            else:
                exclusao = f"DELETE FROM ATV_CP06_ENZO_LUCIANO WHERE cpf='{cpf}'"
                inst_exclusao.execute(exclusao)
                conn.commit()
                print("##### Jogo APAGADO! #####")

        case 5:
            print("!!!!! EXCLUIR TODOS OS DADOS DA TABELA !!!!!")
            confirma = input(margem + "CONFIRMA A EXCLUSÃO DE TODOS OS JOGOS? [S]im ou [N]ão: ")

            if confirma.upper() == "S":
                exclusao = "DELETE FROM ATV_CP06_ENZO_LUCIANO"
                inst_exclusao.execute(exclusao)
                conn.commit()
                print("##### Todos os registros foram excluídos! #####")
            else:
                print(margem + "Operação cancelada pelo usuário!")

        case 6:
            conexao = False

        case _:
            input(margem + "Digite um número entre 1 e 6.")

    input(margem + "Pressione ENTER")

else:
    print("Obrigado por utilizar a nossa aplicação! :)")
