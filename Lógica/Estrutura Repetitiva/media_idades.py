print("Digite as idades: ")
tot = 0
quant = 0
n = int(input(""))
if n > 0:
    while n > 0:
        tot = n + tot
        quant = 1 + quant
        n = int(input(""))
        
    media = tot / quant
    print("Média =", media)
else:
    print("Impossível Calcular")
    
