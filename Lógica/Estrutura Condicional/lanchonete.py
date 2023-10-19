codigo_produto = int(input("Codigo do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))
if codigo_produto == 1:
    valor = 5
else:
    if codigo_produto == 2:
        valor = 3.5
    else:
        if codigo_produto == 3:
            valor = 4.8
        else:
            if codigo_produto == 4:
                valor = 8.9
            else:
                if codigo_produto == 5:
                    valor = 7.32
                else:
                    print("Este código de produto não está em nosso sistema!")
valor_a_pagar = quantidade * valor
print("Valor a pagar: R$", valor_a_pagar)
