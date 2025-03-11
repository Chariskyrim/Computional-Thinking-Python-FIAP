"""import os
os.system("cls")
 
def criar_candidato(numero, nome):
    return {"numero": numero, "nome": nome, "votos": 0}
 
def adicionar_voto(candidato):
    candidato["votos"] += 1
 
def cadastrar_candidatos():
    candidatos = []
    numeros_cadastrados = []
    print("CADASTRO DOS CANDIDATOS")
    for i in range(3):
        numero = int(input(f"Número do candidato: "))
        while numero in numeros_cadastrados:
            print("Número já cadastrado. Escolha outro.")
            numero = int(input(f"Número do candidato: "))
        nome = input(f"Nome do candidato: ")
        candidatos.append(criar_candidato(numero, nome))
        numeros_cadastrados.append(numero)
    print("Candidatos cadastrados com sucesso!\n")
    return candidatos
 
def menu_votacao(candidatos):
    votos_nulos = 0
    while True:
        print("MENU DE VOTAÇÃO")
        for c in candidatos:
            print(f"{c['numero']} - {c['nome']}")
        print("4 - APURAÇÃO PARCIAL")
        print("0 - FIM DA VOTAÇÃO")
       
        voto = input("VOTO: ")
        if voto == "0":
            return votos_nulos
        elif voto == "4":
            apuracao_parcial(candidatos, votos_nulos)
        else:
            voto = int(voto)
            candidato_encontrado = False
            for c in candidatos:
                if c["numero"] == voto:
                    adicionar_voto(c)
                    candidato_encontrado = True
                    break
            if not candidato_encontrado:
                votos_nulos += 1
 
def apuracao_parcial(candidatos, votos_nulos):
    total_votos = sum(c["votos"] for c in candidatos) + votos_nulos
    print("\nAPURAÇÃO PARCIAL")
    print("CANDIDATOS:")
    for c in candidatos:
        percentual = (c["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{c['numero']} - {c['nome']} -> {c['votos']} votos -> {percentual:.2f}%")
    percentual_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
    print(f"NULOS -> {votos_nulos} votos -> {percentual_nulos:.2f}%")
    print(f"TOTAL DE VOTOS: {total_votos}\n")
 
def apuracao_final(candidatos, votos_nulos):
    total_votos = sum(c["votos"] for c in candidatos) + votos_nulos
    print("\nAPURAÇÃO FINAL")
    print("CANDIDATOS:")
    for c in candidatos:
        percentual = (c["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{c['numero']} - {c['nome']} -> {c['votos']} votos -> {percentual:.2f}%")
    percentual_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
    print(f"NULOS -> {votos_nulos} votos -> {percentual_nulos:.2f}%")
    print(f"TOTAL DE VOTOS: {total_votos}\n")
 
# Execução do programa
candidatos = cadastrar_candidatos()
votos_nulos = menu_votacao(candidatos)
apuracao_final(candidatos, votos_nulos)"""