x = 1
y = 1
while x or y != 0:
    print("Digite os valores das coordenadas X e Y:")
    x = float(input(""))
    y = float(input(""))
    if x == 0 or y == 0:
        quit()
    else:
        if x > 0 and y > 0:
            print("Quadrante Q1")
        else:
            if x < 0 and y > 0:
                print("Quadrante Q2")
            else:
                if x < 0 and y < 0:
                    print("Quadrante Q3")
                else:
                    if x > 0 and y < 0:
                        print("Quadrante Q4")
