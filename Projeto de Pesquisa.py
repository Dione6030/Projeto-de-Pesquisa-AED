import csv
import os
import time
import subprocess

estudantes = []

with open("ai_dependency_career_anxiety_students.csv") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        estudantes.append(linha)

def limpar_tela():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def titulo(text, traco="-"):
    print()
    print(text.upper())
    print(traco*40)

def ordena_jovens():
    titulo("Ordem dos Mais Jovens")
    
    print("N..: Estudante ID: Idade: Gênero: Grau Estudo: Habitação:")
    
    grupo = {}
    
    for coluna in estudantes:
        estudante_id = coluna["student_id"]
        idade = int(coluna["age"])
        genero = coluna["gender"]
        grau_estudo = coluna["college_tier"]
        habitacao = coluna["urban_or_rural"]
        grupo[estudante_id] = (idade, genero, grau_estudo, habitacao)
    
    ordenados_novos = sorted(grupo.items(), key=lambda x: x[1][0])
    ordenados_velhos = sorted(grupo.items(), key=lambda x: x[1][0], reverse=True)
    

def ordem_Idade():
    titulo("Menu de Apresentação")
    print("1. Ordem Dos Mais Jovens")
    print("2. Ordem Dos Mais Velhos")
    
    opcao = input("Opção: ")
    if opcao == "1":
        ordena_jovens()
    elif opcao == "2":
        ordena_velhos()
    else:
        print("Opção Inválida")
        return

while True:
    titulo("Menu Principal")
    print("1. Apresenta os Estudante em Ordem de Idade")
    print("2. Apresenta as IAs mais Usadas")
    print("3. Número de Usuarios de IA por Gênero")
    print("4. Operações Com Zonas de Habitação e Grau de Estudo")
    print("5. Grafico de IAs mais Usadas")
    print("6. Grafico de Média de Idade por Grau de Estudo")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        ordem_Idade()
    
    else:
        break