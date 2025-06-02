import os
os.system("clear")

#ej1: crear una lista de numeros e imprimir el contenido

numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

#ej2: crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
print("Presiona Enter para el siguiente codigo:")
input() 
os.system("clear")


palabras = ["materia", "pensar", "python", "programacion", "asistencia"]
print(palabras)
buscador=input("di la palabra a buscar: ")

encontro=False
for i in palabras:
   if i==buscador:
     encontro=True 
if encontro:
   print("Se encontro la palabra en la lista")
else:
   print("No se encontro la palabra en la lista")

#ej3: añadir elementos a la lista
opc = "si"
while opc == "si":
    nueva_palabra = input("introduzca una palabra para añadir a la lista: ").lower() #Lower sirve para convertir las palabras a minusculas
    palabras.append(nueva_palabra)
    opc = input("¿Deseas continuar? ").lower()

print(f"La lista de palabras actualizada es: {palabras}")

print("Presiona Enter para el siguiente codigo:")
input() 
os.system("clear")

#ej4: crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda = [
    ["Cecilia Perez", "112565469"],
    ["Camila Promiscua", "8852165"],
    ["Carlos Paez", "2615856"]
]

print("Agenda (Lista)")
for contacto in agenda:
    nombre = contacto[0]
    telefono = contacto[1]
    print(f"Nombre: {nombre}, Teléfono: {telefono}")
    
for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 