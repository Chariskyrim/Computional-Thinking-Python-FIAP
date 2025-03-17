import os
os.system("cls")
 
perguntas = {
    'Pergunta 1':
    {
        'pergunta': 'Quanto é 2+2? ',
        'respostas':
        {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2':
    {
        'pergunta': 'Quanto é 3x2? ',
        'respostas':
        {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3':
    {
        'pergunta': 'Quanto é 1x1? ',
        'respostas':
        {
            'a': '4',
            'b': '101',
            'c': '1',
            'd': '0'
        },
        'resposta_certa': 'c',
    },
}
 
print("PROVA ELETRÔNICA")
print("-"*16)
 
respostas_certas = 0
 
print(f"\nRESPONDA AS {len(perguntas)} PERGUNTAS\n")
 
 
respostas_certas = 0
# Exibe o numero da pergunta e a descrição
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: \n\t{dados_pergunta["pergunta"]}')
 
    # Exibe as alternativas
    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'\t\t{resposta}) {dados_resposta}')
 
    print()
    # Lê a respost do usuário
    resposta_usuario = input('Sua resposta: ')
 
    # verifica se acertou ou não
    if resposta_usuario == dados_pergunta['resposta_certa']:
        print("Resposta CORRETA!")
        respostas_certas += 1
    else:
        print("Resposta INCORRETA!")
 
    print()
 
 
# mostra a nota
quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print("-"*40)
print(f'Questões corretas.............: {respostas_certas}')
print(f'Porcentagem de acerto.........: {porcentagem_acerto:.1f}%')
print("-"*40)