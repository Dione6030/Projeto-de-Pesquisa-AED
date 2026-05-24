import csv
import os
import subprocess
import time

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
    
    time.sleep(5)
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
    
    time.sleep(5)
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

def comparacao_usuarios_ia():
    titulo("Comparação de Usuários de IA por Gênero")
    print("N.: Gênero....: Usuários: Não-Usuários:")
    
    grupo = {}
    
    for linha in estudantes:
        genero = linha["gender"]
        usuarios = 0
        non_usuarios = 0
        for estudante in estudantes:
            if estudante['gender'] == genero:
                if estudante['primary_ai_tools_used'] == 'None':
                    non_usuarios += 1
                else:
                    usuarios += 1
        grupo[genero] = (usuarios, non_usuarios)

    ordenado = sorted(grupo.items(), key=lambda x: x[1][0], reverse=True)
    
    for i, (genero, (usuarios, non_usuarios)) in enumerate(ordenado, 1):
        print(f"{i:2}: {genero:10}: {usuarios:8}: {non_usuarios:12}:")


def operacoes_com_zonas_e_graus():
    titulo("Menu de Operções")
    
    alunos_rurais = set()
    for coluna in estudantes:
        if coluna['urban_or_rural'] == 'Rural':
            alunos_rurais.add(coluna['student_id'])
    alunos_urbanos = set()
    for coluna in estudantes:
        if coluna['urban_or_rural'] == 'Urban':
            alunos_urbanos.add(coluna['student_id'])
    
    alunos_tier1 = set()
    for col in estudantes:
        if col['college_tier'] == 'Tier 1':
            alunos_tier1.add(col['student_id'])
    alunos_tier2 = set()
    for col in estudantes:
        if col['college_tier'] == 'Tier 2':
            alunos_tier2.add(col['student_id'])
    alunos_tier3 = set()
    for col in estudantes:
        if col['college_tier'] == 'Tier 3':
            alunos_tier3.add(col['student_id'])
    
    print("1. Quantidade de alunos urbanos em cada Grau da Faculdade")
    print("2. Quantidade de alunos rurais em cada Grau da Faculdade")
    
    opcao = input('Opção: ')
    
    if opcao == '1':
        limpar_tela()
        titulo('Resultados')
        urbanos_tier1 = alunos_urbanos.intersection(alunos_tier1)
        print(f"1º Grau: {len(urbanos_tier1)} Alunos")
        urbanos_tier2 = alunos_urbanos.intersection(alunos_tier2)
        print(f"2º Grau: {len(urbanos_tier2)} Alunos")
        urbanos_tier3 = alunos_urbanos.intersection(alunos_tier3)
        print(f"3º Grau: {len(urbanos_tier3)} Alunos")
        time.sleep(5)
    
    elif opcao == '2':
        limpar_tela()
        titulo('Resulatado')
        rurais_tier1 = alunos_rurais.intersection(alunos_tier1)
        print(f"1º Grau: {len(rurais_tier1)} Alunos")
        rurais_tier2 = alunos_rurais.intersection(alunos_tier2)
        print(f"2º Grau: {len(rurais_tier2)} Alunos")
        rurais_tier3 = alunos_rurais.intersection(alunos_tier3)
        print(f"3º Grau: {len(rurais_tier3)} Alunos")
        time.sleep(5)

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
    
    elif opcao == "3":
        limpar_tela()
        comparacao_usuarios_ia()
    
    elif opcao == "4":
        limpar_tela()
        operacoes_com_zonas_e_graus()
    
    else:
        limpar_tela()
        break