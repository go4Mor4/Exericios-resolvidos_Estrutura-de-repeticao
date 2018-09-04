eleitores = int(input("Digite o número de eleitores: "))
votos = []

for i in range(eleitores):
    voto = votos.append(int(input("Qual candidato deseja votar? [1, 2, 3]: ")))

print("Quantidade de votos para candidato 1: ", votos.count(1))
print("Quantidade de votos para candidato 2: ", votos.count(2))
print("Quantidade de votos para candidato 3: ", votos.count(3))
