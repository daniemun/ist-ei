ano = int(input("ano: "))
mes = int(input("mês: "))
dia = int(input("dia: "))

is_ano_bissexto = False
mes_valido = False
dia_valido = False


if (ano % 4 == 0) and (ano % 100 != 0):
	is_ano_bissexto = True
elif (ano % 400 == 0):
	is_ano_bissexto = True

if ( mes == 4 or mes == 6 or mes == 9 or mes == 11 ):
	mes_valido = True
	if ( dia > 0 and dia <= 30 ):
		  dia_valido = True

elif ( mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 ):
	mes_valido = True
	if (dia > 0 and dia <= 31 ):
		dia_valido = True

elif ( mes == 2 ):
	mes_valido = True
	if is_ano_bissexto:
		if ( dia > 0 and dia <= 29 ):
			dia_valido = True
	else:
		if ( dia > 0 and dia <= 28 ):
			dia_valido = True

if ( mes_valido and dia_valido ):
	print("válida")
else:
	print("inválida")
