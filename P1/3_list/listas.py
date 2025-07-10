'''
Ejemplo 1 Crear una lista de numeros e imprimir el contenido

Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

Ejemplo 3 Añadir elementos a la lista

Ejemplo 4 Crear un multidimensional que permita almacenar el nombre y telefono de una agenda
'''

import os

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ////Ejemplo 1////
print("\nContenido de la lista de números:")
for numero in numeros:
    print(numero)
input("\nPresione Enter para continuar...")

#////Ejemplo 2////
os.system("cls")

#1er forma
palabras=["hola","2023","Lebroncito","UTD","True","UTD"]
print(palabras)

palabra_buscar=input("\nIngrese una palabra a buscar: ")
if palabra_buscar in palabras:
    print(f"La palabra '{palabra_buscar}' se encuentra en la lista.")
else:
    print(f"La palabra '{palabra_buscar}' no se encuentra en la lista.")
input("\nPresione Enter para continuar...")

#2da forma
os.system("cls")

palabra_buscar = input("Ingrese una palabra a buscar: ")
encontro=False
posiciones = []
for i in range(0, len(palabras)):
    if palabras[i] == palabra_buscar:
        encontro = True
        posiciones.append(i)
if encontro:
    print(f"La palabra '{palabra_buscar}' se encuentra en la lista.")
else:
    print(f"La palabra '{palabra_buscar}' no se encuentra en la lista.")
input("\nPresione Enter para continuar...")

#////Ejemplo 3////
os.system("cls")
numeros=[]
opc = "si"

while opc=="si":
    opc=input("¿Desea agregar un número a la lista? (si/no): ").lower()
    if opc == "si":
        numero = float(input("Ingrese un número entero o decimal: "))
        numeros.append(numero)
    elif opc == "no":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
print("\nContenido de la lista de números:")
for numero in numeros:
    print(numero)
input("\nPresione Enter para continuar...")

#////Ejemplo 4////
os.system("cls")
agenda=[
    ["Juan Perez", "1234567890"],
    ["Maria Lopez", "0987654321"],
    ["Carlos Gomez", "1122334455"],
    ["Ana Torres", "5566778899"]
    ]

print("\nContenido de la agenda telefónica:")
for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
