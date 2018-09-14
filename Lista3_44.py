possiveis_votos = [1, 2, 3, 4, 5, 6]
candidatos = ['Ciro Gomes', 'Jair Bolsonaro', 'João Amoedo', 'Lula Molusco', 'Nulo', 'Branco']
votos = []

voto = True

while voto != 0:
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while voto not in possiveis_votos:
            print("[Voto invalido.]")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)

print("Quantidade de votos:\nJair Bolsonaro: ", )
