x = 0
alcool = 0
gasolina = 0
diesel = 0
while x != 4:
    x = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
    while x != 1 or x != 2 or x != 3:
        x = int(input("Valor inválido! Tente novamente: "))
    if x == 1:
        alcool = alcool + 1
    else:
        if x == 2:
                gasolina = gasolina + 1
        else:
            if x == 3:
                diesel = diesel + 1
print("Muito obrigado!")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)


