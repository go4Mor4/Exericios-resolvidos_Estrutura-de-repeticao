#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

import math
lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: "))
    while numero // 1 != numero or numero < 0 or 0 or numero < 16:
        numero = float(input("Digite um número[erro]: "))
    else:
        print("Fatorial do número digitado: ", math.factorial(numero))
    count += 1
