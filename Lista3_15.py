ultimo = 1
penultimo = 1
count = 1
print(ultimo)
print(penultimo)
while count <= 9:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)
