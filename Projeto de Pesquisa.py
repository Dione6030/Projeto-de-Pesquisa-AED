import csv
import os
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
    
    ordenados = sorted(grupo.items(), key=lambda x: x[1][0])
    
    for i, (estudante_id, (idade, genero, grau_estudo, habitacao)) in enumerate(ordenados[:10], 1):
        print(f"{i:2}. {estudante_id:12}: {idade:5}: {genero:10}: {grau_estudo:12}: {habitacao:10}")
    
    limpar_tela()
    
    todos = input("Deseja ver todos? (s/n): ")
    if todos.lower() == "s":
        for i, (estudante_id, (idade, genero, grau_estudo, habitacao)) in enumerate(ordenados, 1):
            print(f"{i:2}. {estudante_id:12}: {idade:5}: {genero:10}: {grau_estudo:12}: {habitacao:10}")

def ordena_velhos():
    titulo("Ordem dos Mais Velhos")
    
    print("N..: Estudante ID: Idade: Gênero: Grau Estudo: Habitação:")
    
    grupo = {}
    
    for coluna in estudantes:
        estudante_id = coluna["student_id"]
        idade = int(coluna["age"])
        genero = coluna["gender"]
        grau_estudo = coluna["college_tier"]
        habitacao = coluna["urban_or_rural"]
        grupo[estudante_id] = (idade, genero, grau_estudo, habitacao)
    
    ordenados = sorted(grupo.items(), key=lambda x: x[1][0], reverse=True)
    
    for i, (estudante_id, (idade, genero, grau_estudo, habitacao)) in enumerate(ordenados[:10], 1):
        print(f"{i:2}. {estudante_id:12}: {idade:5}: {genero:10}: {grau_estudo:12}: {habitacao:10}")
    
    limpar_tela()
    
    todos = input("Deseja ver todos? (s/n): ")
    if todos.lower() == "s":
        for i, (estudante_id, (idade, genero, grau_estudo, habitacao)) in enumerate(ordenados, 1):
            print(f"{i:2}. {estudante_id:12}: {idade:5}: {genero:10}: {grau_estudo:12}: {habitacao:10}")

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

def comparacao_ias():
    titulo("Comparação de IAs Mais Usadas")
    print("N.: Inteligencia Artificial: Usuários:")
    
    grupo = {}
    
    for linha in estudantes:
        if linha['primary_ai_tools_used'] != 'None':
            ia = linha['primary_ai_tools_used']
        usuarios = 0
        for estudante in estudantes:
            if estudante['primary_ai_tools_used'] == ia:
                usuarios += 1
        grupo[ia] = usuarios
    
    ordenado = sorted(grupo.items(), key=lambda x: x[1], reverse=True)
    
    for i, (ia, usuarios) in enumerate(ordenado, 1):
        print(f"{i:2}: {ia:23}: {usuarios:8}:")

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
        limpar_tela()
        ordem_Idade()
    
    elif opcao == "2":
        limpar_tela()
        comparacao_ias()
    
    else:
        break