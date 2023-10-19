cont = 1
while cont == 1:
    print("Digite dois numeros:")
    n1 = int(input(""))
    n2 = int(input(""))
    if n1 < n2:
        print("Crescente")
    else:
        if n1 > n2:
            print("Decrescente")
        else:
            print("Iguais")
