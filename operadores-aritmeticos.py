#operadores aritmeticos
# + suma
# - resta
# * multiplicacion
# / division
# % modulo
# ** potencia
# // division entera

#ejemplo de suma

operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print("El resultado de la suma es: ", suma)
print(f"El resultado de la suma es: {suma}") #{suma} se le llama interpolacion (incluir una variable dentro de un string) no olvidar el f antes del string para que funcione la interpolacion.



#ejemplo de resta
resta = operandoA - operandoB
print(f"resultado de la resta es: {resta} ")

#ejemplo de multiplicacion
multiplicacion = operandoA * operandoB
print(f"resultado de la multiplicacion es: {multiplicacion} ")

#ejemplo de division
division = operandoA / operandoB
division = operandoA // operandoB #division entera
print(f"resultado de la division es: {division}")
print(f"resultado de la division es (int): {division} ")

#ejemplo de modulo
modulo = operandoA % operandoB
print(f"resultado del modulo es: {modulo} ")

#ejemplo de potencia
potencia = operandoA ** operandoB
print(f"resultado de la potencia es: {potencia} ")

#ejemplo de division entera
divisionEntera = operandoA // operandoB
print(f"resultado de la division entera es: {divisionEntera} ")

#ejercicio 1
alto = int(input("ingrese el alto del rectangulo: "))
ancho = int(input("ingrese el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
#--------------------------------------------------------------------------------
"""
print(f"el area del rectangulo es: {area} y el perimetro es: {perimetro}") #forma 1"""
#-------------------------------------------------------------------------------
"""
print("Area: ", area)
print("Perimetro: ", perimetro) #forma 2"""
#-------------------------------------------------------------------------------
print("Area:", area, "Perimetro:", perimetro)

