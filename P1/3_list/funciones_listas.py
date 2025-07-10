'''
List (Array)
son colecciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se hace con un indice
numerico

Nota: sus valores si son modificables

La lista es una colección ordenada y modificable, Permite miembros duplicados
'''

import os
os.system("cls")

#Funciones más comunes en las listas
paises=["Mexico","España","Brasil","Canada"]

numeros=[23,45,8,24]

varios=["hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

print("///Recorrer la lista///\n")
print("\n*1er forma\n")
for i in paises:
    print(i)

print("\n*2da forma\n")
for i in range(0,len(paises)):
    print(paises[i])

print("\n*3era forma\n")
lista=""
for i in range(0,len(paises)):
    lista+=f"[{paises}],"
print(lista)

print("\n///Ordenar elementos de una lista///\n")
paises.sort()
print(paises)
numeros.sort()
print(numeros)

print("\n///Dar la vuelta a una lista///\n")
paises.reverse()
print(paises)

varios.reverse()
print(varios)

print("\n///Agregar, insertar, Añadir un elemento a una lista///\n")
print("\n*1er forma\n")
paises.append("Honduras")
print(paises)

print("\n*2da forma\n")
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

print("\n///Eliminar, borrar, suprimir, un elemento de una lista///\n")
print("\n*1er forma\n")
paises.pop(4)
print(paises)

print("\n*2da forma\n")
paises.remove("Honduras")
print(paises)

print("\n///Buscar un elemento dentro de la lista///\n")
print(paises)

resp="Brasil" in paises
print(resp)

print("\n///Contar el numero de veces que aparece un elemento dentro de una lista///\n")

print(numeros)

cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

print("\n///Conocer la posicion o indice en el que se encuentra un elemento "
      "de la lista///\n")
paises.reverse()
print(paises)
posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posicion: {posicion}")

print("\n///Unir el contenido de una lista dentro de otra///\n")

print(numeros)
numeros2=[100,200]

print(numeros2)

print("\n///Crear a partir de las listas de numeros 1 y 2 un resultante y mostrar"
      " el contenido ordenado descendentemente///\n")