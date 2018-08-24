nome = input("Digite o seu nome de usuario: ")
senha = input("Digite a sua senha: ")

while senha == nome:
    print("Erro, a senha não pode ser igual ao nome de usuario!")
    nome = input("Digite o seu nome de usuario: ")
    senha = input("Digite a sua senha: ")
