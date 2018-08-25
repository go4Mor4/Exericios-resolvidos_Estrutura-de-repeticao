#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Digite um número: "))
count1 = 0
count = 1
while count1 < numero:
    fatorial = numero * (numero - count)
    count = count - 1
    count1 = count + 1

print(fatorial)
