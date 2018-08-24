base = int(input("Digite a base: "))
expoente = int(input("Digite expoente: "))
resultado = 1

for i in range(expoente):
    resultado = base * base
    resultado = base * resultado

print(resultado)
