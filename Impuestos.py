#Para determinar un determinado impuesto se debe ser mayor de 18 años y tener ingresos de 500000 colones mensualmente 

edad = int(input("Digite su edad: "))
ingreso = float(input("Digiste el total de su salario menusalmente: "))
if edad >= 18 and ingreso >= 500000:
    print("Tributa para pagar el impuesto")
else: 
    print("No tributa para pagar el impuesto")