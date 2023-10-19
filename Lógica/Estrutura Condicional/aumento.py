salario_atual = float(input("Digite o salario da pessoa: "))
if salario_atual <= 1000:
    porcent = 20
    aumento = 0.2 * salario_atual
    novo_salario = salario_atual + aumento
else:
    if salario_atual > 1000 and salario_atual <= 3000:
        porcent = 15
        aumento = 0.15 * salario_atual
        novo_salario = salario_atual + aumento
    else:
        if salario_atual > 3000 and salario_atual <= 8000:
            porcent = 10
            aumento = 0.1 * salario_atual
            novo_salario = salario_atual + aumento
        else:
            porcent = 5
            aumento = 0.05 * salario_atual
            novo_salario = salario_atual + aumento
print("Novo salario = R$", novo_salario)
print("Aumento = R$", aumento)
print("Porcentagem =", porcent, "%")
    
    
