n1 = float(input("Digite a primeira nota: "))
while n1 < 0 or n1 > 10:
    n1 = float(input("Valor Inválido! Tente Novamente: "))
n2 = float(input("Digite a segunda nota: "))
while n2 < 0 or n2 > 10:
    n2 = float(input("Valor Inválido! Tente Novamente: "))
media = (n1 + n2) / 2
print("MEDIA =", media)
