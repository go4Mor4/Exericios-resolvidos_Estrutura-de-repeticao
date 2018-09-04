quant_cds = int(input("Digite a quantidade de CD's : "))
cds = []
n_cd = 1

for i in range(quant_cds):
    print("CD número ", n_cd)
    valor_cd = cds.append(float(input("Digite o valor do CD: ")))
    n_cd += 1

media = sum(cds) / len(cds)
print("A media para cada CD é: ", media)
