"""
List (Array)

Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un 
indice numerico.

Nota: sus valores si son modificables.

La lista es una coleccion ordenada y modificable.
Permite miembros duplicados.
"""
import os
os.system("clear")

#funciones mas comunes en las listas
#ALT + 123 {}
#ALT + 91= []
paises=["Mexico","España","Brasil","Canada"]

numeros=[23,45,8,24]

varios= ["Hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#1ra forma
for i in paises:
    print(i)

#2da forma
for i in range (0,len(paises)):
    print(paises[i])

#3ra forma
lista=""
for i in range (0,len(paises)):
    lista+=f"[{paises[i]}],"
    print(lista)

#Ordenar elementos de una lista
paises.sort()
print(paises)
numeros.sort()
print(numeros)
#Nota: no puedes enumerar tipos de datos distintos, como cadenas, numeros y logicos
#EJ: varios.sort()

#Invertir la lista de izquierda a derecha
#Empieza del ultimo valor hasta el primero
paises.reverse()
print(paises)

varios.reverse()
print(varios)

#Agregar, Insertar, Añadir un elemento a una lista -.Append()
#1ra forma - RECOMENDABLE
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

#Eliminar, depurar, suprimir un elemento de una lista - .pop(y el numero de la lista que quieres borrar)
#1er forma
paises.pop(4)
print(paises)

#2da forma - .remove
paises.remove("Honduras")
print(paises)
#NOTA: solo va a borrar la primera que se encuentre

#Buscar un elemento dentro de la lista
print(paises)
"Brasil" in paises #Solo tiene una salida en True o False

resp="Brasil" in paises

print("Brasil" in paises)

#Contar el numero de veces que aparece un elemento dentro de una lista
#Si un valor se repite, te dira cuantas veces aparece en la lista
print(numeros)

#Recibe un parametro
cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

#Conocer la posicion o indice que se encuentra un elemento de la lista
paises.reverse()
paises.append("Canada")
print(paises)

posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posicion: ", posicion)

#Copia y pega el contenido de una lista dentro de otra lista
print(numeros)
numeros2=[100,200]

print(numeros2)

#Crear a partir de las listas de numeros 1 y 2 una resultante
#Mostrar el contenido ordenado de manera descendente

#la funcion Extend puede unir mas

numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)

#La de arriba no ordena los numeros

numeros.reverse()
print(numeros)

#Lend sirve para sacar el numero de datos de la lista de la variable, 
#EJ: paises=mexico, españa, etc. y la imprime de forma ascendente

