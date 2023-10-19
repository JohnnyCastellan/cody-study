x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
if x > 0 and y > 0:
    print("Q1")
else:
    if x < 0 and y < 0:
        print("Q3")
    else:
        if x > 0 and y < 0:
            print("Q4")
        else:
            if x < 0 and y > 0:
                print("Q2")
            else:
                if x == 0 and y == 0:
                    print("Origem")
                else:
                    if x == 0 and y != 0:
                        print("Eixo Y")
                    else:
                        if x != 0 and y == 0:
                            print("Eixo X")
