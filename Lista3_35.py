numero = int(input("\nDigite um número: "))
lista = []

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print("Números primos: ", lista)
