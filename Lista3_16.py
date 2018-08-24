ultimo = 1
penultimo = 1
print(ultimo)
print(penultimo)
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo)
    else:
        print("O proximo valor será maior que 500")
