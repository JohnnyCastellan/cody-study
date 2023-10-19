glicose = float(input("Digite a medida da glicose: "))
if glicose <= 100:
    print("Classificação: Normal")
else:
    if glicose > 100 and glicose <= 140:
        print("Classificação: Elevado")
    else:
        print("Classificação: Diabetes")
