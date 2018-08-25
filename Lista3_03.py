#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    nome = input("Digite o seu nome[MAIOR QUE 3 CARACTERES]: ")
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Digite a sua idade[ENTRE 0 E 150]: "))
salario = float(input("Digite o seu salário: "))
while salario <= 0:
    salario = float(input("Digite o seu salário[MAIOR QUE 0]: "))
sexo = input("Digite o seu sexo [f, m]: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Digite o seu sexo[f OU m]: ")
estado_civil = input("Digite o seu estado cívil [s, c, v, d]: ")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input("Digite o seu estado civil[s, c, v, d]: ")
