populacao1 = int(input("Digite a população 1: "))
populacao2 = int(input("Digite a população 2: "))
crescimento1 = input("Porcentagem de crescimento anual da população 1: ")
crescimento2 = input("Porcentagem de crescimento anual da população 2: ")

ano = 0
crescimento1.split('%')
crescimento2.split('%')
crescimento_porcentagem1 = int(crescimento1[0]) / 100
crescimento_porcentagem2 = int(crescimento2[0]) / 100

if populacao1 > populacao2:
    if crescimento_porcentagem2 > crescimento_porcentagem1:
        while populacao1 > populacao2:
            populacao1 += populacao1 * crescimento_porcentagem1
            populacao2 += populacao2 * crescimento_porcentagem2
            ano += 1

        print("Vai levar ", ano, " anos para a populacao 2 ultrapassar a 1")
    else:
        while crescimento_porcentagem2 > crescimento_porcentagem1:
            print("O crescimento da menor população deve ser maior que o da maior população")
            crescimento1 = input("Porcentagem de crescimento anual da população 1: ")
            crescimento2 = input("Porcentagem de crescimento anual da população 2: ")
elif populacao1 < populacao2:
    if crescimento_porcentagem2 < crescimento_porcentagem1:
        while populacao1 > populacao2:
            populacao1 += populacao1 * crescimento_porcentagem1
            populacao2 += populacao2 * crescimento_porcentagem2
            ano += 1

        print("Vai levar ", ano, " anos para a populacao 1 ultrapassar a 2")
    else:
        while crescimento_porcentagem2 < crescimento_porcentagem1:
            print("O crescimento da menor população deve ser maior que o da maior população")
            crescimento1 = input("Porcentagem de crescimento anual da população 1: ")
            crescimento2 = input("Porcentagem de crescimento anual da população 2: ")
else:
    while populacao1 == populacao2:
        print("As populações não podem ser iguais")
        populacao1 = int(input("Digite a população 1: "))
        populacao2 = int(input("Digite a população 2: "))
