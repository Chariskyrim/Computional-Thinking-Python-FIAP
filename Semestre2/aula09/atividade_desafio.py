# instalacao do pip https://medium.com/@nara.guimaraes/instalando-o-pip-nolinux-windows-e-macos-um-guia-passo-a-passo-cc7b6d752b31#:~:text=Instalação%20do%20Pip%20no%20macOS,Python%203%20e%20o%20Pip.

"""
SCRIPT BD

create database petshop
use petshop

create table petshop(
    id int PRIMARY KEY IDENTITY,
    tipo_pet VARCHAR(30),
    nome_pet VARCHAR(30),
    idade INT
);
"""


import os
import oracledb
import pandas as pd



try:
    conn = oracledb.connect(user = "pf1530", password = "fiap2025", dsn='oracle.fiap.com.br:1521/ORCL')
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao =  False
else:
    # Flag para executar a Aplicação
    conexao =  True

margem = ' ' * 4  

# Enquanto o flag conexao estiver apontado com True
while conexao:

    os.system('cls')

    # Apresenta o menu
    print("------- CRUD - PETSHOP -------")
    print("""
    1 - Cadastrar Pet
    2 - Listar Pets
    3 - Alterar Pet
    4 - Excluir Pet
    5 - EXCLUIR TODOS OS PETS
    6 - SAIR
    """)

    # Captura a escolha do usuário
    escolha = input(margem + "Escolha -> ")

    # Verifica se o número digitado é um valor numérico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        escolha = 6
        print("Digite um número.Reinicie a Aplicação!")

    os.system('cls')  # Limpa a tela via SO

    # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:
        # CADASTRAR UM PET
        case 1:
            try:
                print("----- CADASTRAR PET -----")
                # Recebe os valores para cadastro
                tipo = input(margem + "Digite o tipo....: ")
                nome = input(margem + "Digite o nome....: ")
                idade = int(input(margem + "Digite a idade...: "))

                # Monta a instrução SQL de cadastro em uma string
                cadastro = f""" INSERT INTO petshop (tipo_pet, nome_pet, idade)VALUES ('{tipo}', '{nome}', {idade}) """

                # Executa e grava o Registro na Tabela
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                # Erro de número não digitar um numero na idade
                print("Digite um número na idade!")
            except:
                # Caso ocorra algum erro de conexão ou no BD
                print("Erro na transação do BD")
            else:
                # Caso haja sucesso na gravação
                print("##### Dados GRAVADOS #####")

        # LISTAR TODOS OS PETS
        case 2:
            print("----- LISTAR PETs -----")
            lista_dados = []  # Lista para captura de dados do Banco

            # Monta a instrução SQL de seleção de todos os registros da tabela
            inst_consulta.execute('SELECT * FROM petshop')
            # Captura todos os registros da tabela e armazena no objeto data
            data = inst_consulta.fetchall()

            # Insere os valores da tabela na Lista
            for dt in data:
                lista_dados.append(dt)

            # ordena a lista
            lista_dados = sorted(lista_dados)

            # Gera um DataFrame com os dados da lista utilizando o Pandas
            dados_df = pd.DataFrame.from_records(
                lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade'], index='Id')

            # Verifica se não há registro através do dataframe
            if dados_df.empty:
                print(f"Não há um Pets cadastrados!")
            else:
                print(dados_df)  # Exibe os dados selecionados da tabela

            print("##### LISTADOS! #####")

    # Pausa o fluxo da aplicação para a leitura das informações
    input(margem + "Pressione ENTER")
else:
    print("Obrigado por utilizar a nossa aplicação! :)")