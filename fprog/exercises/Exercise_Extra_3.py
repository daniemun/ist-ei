#!/usr/bin/python3

while True:
    try:
        # Get input from user
        custo_fabrico = float(input("Custo de fabrico (€) = "))
        perc_lucro_vendedor = float(input("Lucro do vendedor (%) = "))
        perc_impostos = float(input("Impostos (%) = "))
        break
    except ValueError:
        print("Invalid number")
        
custo_final = custo_fabrico * ( 1 + ((perc_lucro_vendedor + perc_impostos) / 100))

print(f"Custo final: {custo_final:.2f} €")