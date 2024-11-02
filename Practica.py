x=0
promedio=0
suma=0
personas=int(input("Ingrese la cantidad de examenes realizados: "))
while x<personas:
    nota=int(input("Digite la nota del examen: "))
    x=x+1
    suma=suma+nota
promedio=suma/personas
print("La nota final del estudiante es de: ",promedio)
if promedio>=70:
    print("El estudiante esta aprobado")
elif promedio<70 and promedio>=60:
    print("El estudiante debe ir a ampliación")
elif promedio<60:
    print("El estudiante esta reprobado")
else:
    print("Error, por favor intentelo de nuevo")