escala = input("Você vai digitar a temperatura em qual escala (C/F)? ")
if escala == "F":
    temp_F = float(input("Digite a temperatura em Fahrenheit: "))
    temp_C = round((5 / 9) * (temp_F - 32), 2)
    print("Temperatura equivalente em Celsius:", temp_C)
else:
    temp_C = float(input("Digite a temperatura em Celsius: "))
    temp_F = round((temp_C * (9 / 5)) + 32, 2)
    print("Temperatura equivalente em Fahrenheit:", temp_F)
