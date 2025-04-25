n = int(input())

estudantes = {}

for _ in range(n):
    
    nome_nota = input().split()

    nome = nome_nota[0]
    notas = list(map(float, nome_nota[1:]))

    estudantes[nome] = notas

consulta = input()

consultar_notas = estudantes[consulta]

media = (sum(consultar_notas))/len(consultar_notas)

print(f"{media:.2f}")




