#exercicio nao incluido no hackerRank, apenas para treinar sobre dicionarios.

import os
alunos = {}

qtd_alunos = int(input("digite a quantidade de alunos que quer cadastrar:"))

for i in range(qtd_alunos):
    nome = input(f"digite o nome do aluno {i+1}: ")
    input_notas = (input(f"digite as 2 notas de {nome}:(separadas por espaço!)"))
    notas = list(map(float, input_notas.split()))
    alunos[nome] = notas
    media = sum(notas)/len(notas)
    alunos[nome] = notas + [media]

os.system('cls') or None
consulta = input("digite o nome do aluno que deseja consultar a nota: ")

if alunos.get(consulta) == None: print("nome nao encontrado!")
else: 
    print(alunos.get(nome))

