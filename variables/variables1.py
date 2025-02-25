# VARIABLES: Se crean cuando se les asigna un valor que puede variar. Se pueden declarar con comillas dobles o simples y se diferencian entre mayúsculas y minúsculas en sus nombres.

x = 5 #Declara la variable x y le asigna el valor 5.
print(x) #Permite imprimir el valor que almacena x.

a = b = c = "Banana" #Permite declarar más de una variable con el mismo valor
print(a, b, c)

d, e, f, g, h = 'John', 'Neifer', 'Smith', "Morales", "Reinoso" #Permite asignar más de un valor a más de una variable en una misma línea.
print(d, e, f, g, h)

print("Hola, buenos días Bianny. ¿Cómo estás?")

#CONVERSIÓN DE DATOS

x = str(5) #Hace que el 5 sea tipo string (cadena)
y = int(3) #Hace que el 3 sea tipo int (entero)
z = float(9) #Hace que el 9 sea tipo float (decimal)
print(x, y, z)

#Type: Se utiliza para saber el tipo de dato que hay dentro de una variable.

print(type(z)) 

TropicalFruits = ["Guineo", "Sapote", "Guayaba", "Tamarindo"] #Esto es una lista, se escribe entre [] y es mutable.
x, y, l, m = TropicalFruits #Permite declar variable dentro de la lista
print(x, y, l, m)