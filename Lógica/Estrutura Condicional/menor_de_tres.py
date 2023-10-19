primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundos valor: "))
terceiro = int(input("Terceiro valor: "))
if primeiro <= segundo and primeiro <= terceiro:
    print("Menor =", primeiro)
else:
    if segundo <= primeiro and segundo <= terceiro:
        print("Menor =", segundo)
    else:
        print("Menor =", terceiro)
        
