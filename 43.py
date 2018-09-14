menu = [item1[100, 'Cachorro Quente', 1.20], item2[101, 'Bauru Simples', 1.30], item3[102, 'Bauru Com Ovo', 1.50], item4[103, 'Hamburguer', 1.20], item5[104, 'ChesseBurguer', 1.30], item6[105, 'Refrigerante', 1.0]]

codigo = True
while codigo != 0:
    codigo = int(input("Digite o código do alimento: "))
    if codigo in menu:
        
