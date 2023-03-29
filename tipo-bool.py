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


#Ejercicio 1 califica tu dia de trabajo
#pedir al usuario que califique su dia del 1 al 10

tired = int(input("How tired are you? (1-10) "))
if tired > 8:
    print("You should rest")
else:
    print("You should keep working")

#Ejercicio 2
#pedir al usuario que califique su dia del 2 al 10

dia = int(input("Que tal esta tu dia? Introduce un numero del 1 al 5: "))
if dia == 1:
    print("Hoy es un dia horrible")
elif dia == 2:
    print("Hoy es un dia malo")
elif dia == 3:
    print("Hoy es un dia normal")
elif dia == 4:
    print("Hoy es un dia bueno")
elif dia == 5:
    print("Hoy es un dia excelente")
else:
    print("Ese numero no esta en el rango")

#Ejercicio 3
#pedir al usuario que califique su nivel de ingles del 1 al 10

english = int(input("how good is your english type from 0 al 10: "))
if english == 0:
    print("your English level is A1")
elif english <= 1:
    print("your English level is A1")
elif english <= 2:
    print("your English level is A1")
elif english == 3:
    print("your English level is A2")
elif english <= 4:
    print("your English level is A2")
elif english == 5:
    print("your English level is B1")
elif english <= 6:
    print("your English level is B1")
elif english == 7:
    print("your English level is B2")
elif english <= 8:
    print("your English level is B2")
elif english == 9:
    print("your English level is C1")
elif english <= 10:
    print("your English level is C1")
else:
    print("Ese numero no esta en el rango")

#Ejercicio 4
#pedir al usuario su nivel en programacion de javascript del 1 al 5

js = int(input("how good is your javascript type from 0 al 5: "))
if js == 1:
    print("your javascript level is basic")
elif js == 2:
    print("your javascript level is intermediate")
elif js == 3:
    print("your javascript level is advanced")
elif js == 4:
    print("your javascript level is expert")
elif js == 5:
    print("your javascript level is ninja")
else:
    print("Ese numero no esta en el rango")