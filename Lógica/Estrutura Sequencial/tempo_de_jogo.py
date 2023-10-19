hora_i = int(input("Hora inicial: "))
hora_f = int(input("Hora final: "))
if hora_f > hora_i:
    duracao = hora_f - hora_i
else:
    if hora_f == hora_i:
        duracao = 24
    else:
        if hora_i > hora_f:
            duracao = (24 - hora_i) + hora_f
print("O jogo durou", duracao, "Hora(s)")
