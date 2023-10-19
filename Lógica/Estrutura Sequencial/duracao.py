segundos = int(input("Digite a duracao em segundos: "))
horas = (segundos // 60) // 60
minutos = (segundos // 60) % 60
segundos_finais = segundos % 60
print(horas,":", minutos, ":", segundos_finais)


