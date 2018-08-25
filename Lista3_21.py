#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("\nDigite um número: "))

if numero % 2 == 0 and numero != 2:
    print("não primo")
else:
    print("primo")
