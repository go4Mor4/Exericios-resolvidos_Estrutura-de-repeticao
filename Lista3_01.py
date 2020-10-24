#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota entre zero e 10: "))

while nota > 10 or nota < 0:
    nota = float(input("Informe um valor válido: "))
  print(nota)
