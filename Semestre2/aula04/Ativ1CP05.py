# Enzo Luciano Barros de Oliveira
# RM 559557 - 1ESPR

import os
os.system('cls')

prova = {
    'Pergunta 1': {
        'enunciado': 'Quanto é 2+2? ',
        'alternativas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'enunciado': 'Quanto é 3x2? ',
        'alternativas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'enunciado': 'Qual o cubo de 2? ',
        'alternativas': {
            'a': '4',
            'b': '8',
            'c': '16',
        },
        'resposta_certa': 'b',
    },
}
 
resultados = []
 

def executar_prova():
    nome = input("Nome do Aluno: ")
    respostas_certas = 0
 
    for pergunta, dados_pergunta in prova.items():
        print(f'{pergunta}: {dados_pergunta["enunciado"]}')
 
        for letra, alternativa in dados_pergunta['alternativas'].items():
            print(f'\t{letra}) {alternativa}')
 
        resposta_usuario = input("Sua resposta: ").lower()
 
        if resposta_usuario == dados_pergunta['resposta_certa']:
            print("Resposta CORRETA! :]")
            respostas_certas += 1
        else:
            print("Resposta INCORRETA! :,[")
 
        print()
 
    quantidade_perguntas = len(prova)
    nota = (respostas_certas / quantidade_perguntas) * 10
    print(f"Você tirou nota: {nota:.1f}\n")
    
    resultados.append((nome, nota))
    print("Dados gravados na Tabela com sucesso!\n")
 
def cadastrar_questao():
    print("CADASTRANDO UMA QUESTÃO:")
    enunciado = input("Enunciado: ")
 
    alternativas = {}
    for letra in ['a', 'b', 'c']:
        alternativas[letra] = input(f"Alternativa {letra}): ")
 
    resposta_certa = input("Alternativa correta: ").lower()
    if resposta_certa not in alternativas:
        print("Alternativa correta inválida. Questão não cadastrada.\n")
        return
 
    nova_pergunta = f'Pergunta {len(prova) + 1}'
    prova[nova_pergunta] = {
        'enunciado': enunciado,
        'alternativas': alternativas,
        'resposta_certa': resposta_certa,
    }
    print("Questão cadastrada com sucesso!\n")
 
def listar_provas():
    if not resultados:
        print("Nenhuma prova foi executada ainda.\n")
        return
 
    soma_notas = 0
    print("LISTAGEM DAS PROVAS EXECUTADAS")
 
    for i, (nome, nota) in enumerate(resultados, start=1):
        print(f"Prova {i} | {nome} | {nota:.1f}")
        soma_notas += nota
 
    media = soma_notas / len(resultados)
    print(f"\nMédia dos alunos: {media:.1f}\n")
 
def menu():
    while True:
        print("MENU\n")
        print("0 - SAIR")
        print("1 - Executar a Prova")
        print("2 - Cadastrar questão")
        print("3 - Listar provas executadas | média dos alunos\n")
        
        escolha = input("Escolha: ")
        
        if escolha == '0':
            print("Saindo...")
            break
        elif escolha == '1':
            executar_prova()
        elif escolha == '2':
            cadastrar_questao()
        elif escolha == '3':
            listar_provas()
        else:
            print("Opção inválida.\n")
 
menu()