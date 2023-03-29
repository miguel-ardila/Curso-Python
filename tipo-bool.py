#tipos bool (booleanos - boolean)
#True (verdadero) y False (falso)

myvariable = True
print(myvariable)
print(type(myvariable))

myvariable2 = 3 > 5
print(myvariable2)

if myvariable2:
    print("Es verdadero")
else:
    print("Es falso")


#Funcion input para pedir datos al usuario
myvariable3 = input("Introduce un valor: ")
print(myvariable3)
print(type(myvariable3))
print("fin del programa")

#conversion de entrada de datos
myvariable4 = int(input("Introduce un valor: "))
print(myvariable4)
print(type(myvariable4))
print("fin del programa")

numero1 = int(input("Introduzca el primer numero: ")) #convertimos a entero (int)
numero2 = int(input("Introduzca el segundo numero: ")) #convertimos a entero (int) agregamos el int para que no se sume como string y pueda sumar los 2 numeros que se ingresan
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
