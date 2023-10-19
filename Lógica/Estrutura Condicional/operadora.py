minutos = int(input("Digite a quantidade de minutos: "))
if minutos <= 100:
    valor_a_pagar = 50
    print("Valor a pagar: R$", valor_a_pagar)
else:
    valor_a_pagar = 50 + 2 * (minutos - 100)
    print("Valor a pagar: R$", valor_a_pagar)
