import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))
delta = (b ** 2) - 4 * a * c
if delta < 0:
    print("Esta equação não possui raízes reais")
else:
    if delta == 0:
        x = - b / (2 * a)
        print("X1 =", x)
        print("X2 =", x)
    else:
        x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
        x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
        print("X1 =", x1)
        print("X2 =", x2)
