import math
base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))
area = base * altura
perimetro = round((base * 2) + (altura * 2), 4)
diagonal = round(math.sqrt((base ** 2) + (altura ** 2)), 4)
print("Base do retangulo:", base)
print("Altura do retangulo:", altura)
print("Area =", area)
print("Perimetro =", perimetro)
print("Diagonal =", diagonal)
