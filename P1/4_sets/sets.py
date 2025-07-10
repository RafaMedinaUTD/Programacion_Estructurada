'''

Sets.-
Es un tipo de datos para tener una coleccion de valores pero no tienen
ni indices ni orden.

Set es una coleccion desordenada, inmutable y no indexada.
No hay miembros duplicados.

'''


import os
os.system('cls')


paises={"México","Brasil","España","Canada","Canada"}
print(paises)

varios={True,"UTD",33,3.14}
print(varios)

#Funciones u Operaciones
paises.add("Mexico") 
print(paises)

paises.pop()
print(paises)

paises.remove("Mexico")
print(paises)

# lista={""}
# respuesta="si"


# while respuesta=="si":
#     alumnos=input("Ingrese email: ")
#     lista.add(alumnos)
#     print(lista)

#     respuesta=input("Desea? ingresar otro?: ").lower()

#Solucion 2
lista=[]
respuesta="si"


while respuesta=="si":
    lista.append(input("Ingrese email: "))
    respuesta=input("Desea? ingresar otro?: ").lower()
    lista_set=set(lista) #Quito los duplicados
    lista=list(lista_set)
    print(lista)