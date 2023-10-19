print("Digite as tres distancias:")
d1 = float(input(""))
d2 = float(input(""))
d3 = float(input(""))
if d1 >= d2 and d1 >= d3:
    print("Maior distância =", d1)
else:
    if d2 >= d1 and d2 >= d3:
        print("Maior distância =", d2)
    else:
        print("Maior distância =", d3)
