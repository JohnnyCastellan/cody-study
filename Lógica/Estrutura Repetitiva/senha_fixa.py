senha = 2002
x = int(input("Digite a senha: "))
if x == senha:
    print("Acesso permitido!")
else:
    while x != senha:
        x = int(input("Senha Inválida! Tente novamente: "))
    print("Acesso Permitido")
