import time

while True:
    precos_produtos = []
    preco_produto = True
    n_produto = 1

    while preco_produto != 0:
        print("Produto n° ", n_produto)
        preco_produto = float(input("Digite o preço do produto: "))
        precos_produtos.append(preco_produto)
        n_produto += 1

    print("Total: ", sum(precos_produtos))
    dinheiro = float(input("Digite a quantida que irá pagar: "))

    while dinheiro < sum(precos_produtos):
        dinheiro = float(input("Digite a quantida que irá pagar[maior que o total da compra] : "))

    print("Dinheiro: R$", dinheiro)
    print("Troco: R$", dinheiro - sum(precos_produtos))
    print("\nPróxima compra em 3 segundos...")
    time.sleep(3)
    print("\n" * 5)
