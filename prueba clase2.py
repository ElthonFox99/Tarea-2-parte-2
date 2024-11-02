#print palabra reservada
print("Hola Mundo")

#input es para solicitar datos 
#input("Dijite su nombre: ")

#Variables
"""
nombre = input("Digite su nombre: ")
print ("Hola "+nombre)
"""

#Paso 1 asignar nombre
#Asignacion de datos

#Tipos de datos
#String ----- Caddena de caracteres------ Letras/numeros/simbolos "" ''
#Int-----------numeros
#float------------ numeros decimales 1.56 -2.2
#boleanos --------- True or False 

"""
nombre=input("Digite su nombre:")
if ("kei"==nombre):
   print("el nombre es igual")
else: print("el nombre no es igual")
"""

"""
#Escribir un programa que muestre si el usuario es mayor de edad o no
edad=int(input("Digite su edad"))
if edad>=18:
    print("Es mayor de edad")
else: 
    print("No es mayor de edad")
"""

#Escribir un programa que pida al usuario dos numeros su division. Si el usuario introduce un 0 como divisor 
#Debemos mostrar que existe un error 
"""
num1=float(input("Digite el primer numero: "))
num2=float(input("Digite el segundo numero: "))

if num1 !=0 and num2 !=0:
    print(num1/num2)
else:
    print("ERROR)
"""

edad = 0
nombre = ""
estatura = 0.0
esPar = True 

print(edad, nombre, estatura, esPar)
nombre =  input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
estatura = float(input("Digite su estatura: "))
esPar = input

print("Su nombre es: "+nombre+"Su edad es: ",edad, "Su altura es:", estatura)
print("Su edad es: ", edad)
print("Su estatura es: ", estatura)