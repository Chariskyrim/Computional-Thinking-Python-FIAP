#Enzo Luciano Barros de Oliveira
#RM 559557 - 1ESPR
import os
os.system('cls')

def cadastrar_candidatos():
    candidatos = {}
    for i in range(1, 4):
        numero = int(input(f"Número do candidato {i}: "))
        nome = input(f"Nome do candidato {i}: ")
        candidatos[numero] = {"nome": nome, "votos": 0}
    return candidatos


def exibir_menu(candidatos):
    print("\nCANDIDATOS")
    for numero, candidato in candidatos.items():
        print(f"{numero} - {candidato['nome']}")
    print("4 - APURAÇÃO")
    print("0 - FIM DA VOTAÇÃO")


def apuracao(candidatos, votos_nulos, parcial=True):
    total_votos = sum(c["votos"] for c in candidatos.values()) + votos_nulos
    print("\nAPURAÇÃO PARCIAL:" if parcial else "\nAPURAÇÃO FINAL:")

    if total_votos > 0:
        for num, candidato in candidatos.items():
            votos = candidato["votos"]
            percentual = (votos / total_votos) * 100
            print(f"{num} - {candidato['nome']} -> {votos} votos -> {percentual:.1f}%")
        percentual_nulos = (votos_nulos / total_votos) * 100
        print(f"NULOS -> {votos_nulos} votos -> {percentual_nulos:.1f}%")
    else:
        for num, candidato in candidatos.items():
            print(f"{num} - {candidato['nome']} -> {candidato['votos']} votos")
        print(f"NULOS -> {votos_nulos} votos")

    print(f"\nTOTAL DE VOTOS: {total_votos}")
    
    if parcial:
        input("\nPressione ENTER para voltar ao menu...")


def computar_voto(candidatos):
    votos_nulos = 0
    while True:
        exibir_menu(candidatos)
        escolha = input("\nDigite o número do seu voto: ")
        
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha in candidatos:
                candidatos[escolha]["votos"] += 1
                print(f"Voto computado para {candidatos[escolha]['nome']}!")
            elif escolha == 4:
                apuracao(candidatos, votos_nulos)
            elif escolha == 0:
                print("\nEncerrando votação...")
                apuracao(candidatos, votos_nulos, parcial=False)
                break
            else:
                votos_nulos += 1
                print("Voto computado como NULO.")
        else:
            print("Digite um número válido.")


print("Cadastro dos três candidatos\n")
candidatos = cadastrar_candidatos()
computar_voto(candidatos)
