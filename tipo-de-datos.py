#Tipos de Datos 
#Integer: Tipo de dato para números enteros, ya sean positivos o negativos.
#Float: Tipo de dato para números con precisión decimal, pueden ser negativos o positivos.
#String: Tipo de dato para cadena de texto con caracteres alfanuméricos
#Boolean: Tipo de dato que solo puede tener dos valores, True (Verdadero) o False (Falso)
#La función type() regresa el tipo de dato de una variable o valor

#ejemplo
x = "Hello World" #str (tipo de dato string)
print(type(x))

#otro ejemplo
x = 20 #int (tipo de dato entero)
print(type(x))

#otro ejemplo
x = 20.5 #float (tipo de dato decimal)
print(type(x))

#otro ejemplo
x = 1j #complex (tipo de dato complejo)
print(type(x))

#otro ejemplo
x = ["apple", "banana", "cherry"] #list (tipo de dato lista)
print(type(x))

#otro ejemplo
x = ("apple", "banana", "cherry") #tuple (tipo de dato tupla)
print(type(x))

#otro ejemplo
x = range(6) #range (tipo de dato rango)
print(type(x))

#otro ejemplo
x = {"name" : "John", "age" : 36} #dict (tipo de dato diccionario)
print(type(x))

#otro ejemplo
x = {"apple", "banana", "cherry"} #set (tipo de dato conjunto)
print(type(x))

#otro ejemplo
x = frozenset({"apple", "banana", "cherry"}) #frozenset (tipo de dato conjunto inmutable)
print(type(x))

#otro ejemplo
x = True #bool (tipo de dato booleano)Se caracterizan por tener solo dos valores True o False y ambos deben escribirse con su primer letra en mayúscula.
print(type(x))

#otro ejemplo
x = b"Hello" #bytes (tipo de dato bytes)
print(type(x))

#otro ejemplo
x = bytearray(5) #bytearray (tipo de dato bytearray)
print(type(x))

#otro ejemplo
x = memoryview(bytes(5)) #memoryview (tipo de dato memoryview)
print(type(x))
