#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input("\nDigite um número: "))
lista = []


if numero % 2 != 0 or numero == 2:
    print("primo")
else:
    for i in range(numero):
        if numero % (i + 1) == 0:

            lista.append(i + 1)

print("Os números divisiveis por ", numero, " são ", lista)
