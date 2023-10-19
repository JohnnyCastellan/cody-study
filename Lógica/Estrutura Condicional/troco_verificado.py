preco_unitario = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))
if recebido < (preco_unitario * quantidade):
    falta = (quantidade * preco_unitario) - recebido
    print("Dinheiro insuficiente. Faltam", falta, "Reais")
else:
    troco = recebido - (quantidade * preco_unitario)
    print("Troco = R$", troco)
