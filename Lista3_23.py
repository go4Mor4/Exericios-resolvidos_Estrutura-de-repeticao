numero = int(input("\nDigite um número: "))
lista = []
divisoes = 0

for i in range(numero + 1):
    if i < 9:
        if i % 2 == 1 and i != 1:
            lista.append(i)
            divisoes += 1
    if i > 9:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 !=0:
            lista.append(i)
            divisoes += 1
    if i == 2:
        lista.append(i)
    else:
        divisoes += 1
print("Números primos: ", lista)
print("Número de divisões", divisoes)
