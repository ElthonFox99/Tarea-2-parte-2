num_exam = int(input("Digite la cantidad de examenes realizados: "))
nota1 = int(input("Digite su primera nota: "))
nota2 = int(input("Digite su primera nota: "))
nota3 = int(input("Digite su primera nota: "))

promedio = sum(nota1+nota2+nota3)/ num_exam

print("Su promedio es:",promedio)

if promedio >=70:
    print("Aprovaste")
elif promedio >=60:
    print("Tiene que ir a ampliacion")
else:
    print("reprovaste")