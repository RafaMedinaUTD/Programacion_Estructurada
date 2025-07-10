'''
dict.-
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo
de datos, pero en lugar de tener como las listas
indices numericos, tiene alfanuméricos. Es decir, es algo parecido
como los Objetos

Tambien se conoce como un arreglo asociativo u Objeto JSON

El dicccionario es una coleccion ordenada y modificable. 
No hay miembros duplicados.

'''
import os
os.system('cls')

paises = ["Mexico", "Brasil", "España", "Canada"]

pais1={
    "nombre":"México",
    "capital":"CDMX",
    "poblacion":126000000,
    "idioma":"español",
    "status":True 
        }

pais2={
    "nombre":"Brasil",
    "capital":"Brasilia",
    "poblacion":213000000,
    "idioma":"portugues",
    "status":True 
        }
pais3={
    "nombre":"Canada",
    "capital":"Ottawa",
    "poblacion":38000000,
    "idioma":["ingles", "frances"],
    "status":True     
        }
print(pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")

#Agregar un atributo a un objeto
pais1["Altitud"]=2240
for i in pais1:
    print(f"{i}={pais1[i]}")

#Modificar un valor de un item o atributo que ya existe
pais1.update({"altitud":2500})
for i in pais1:
    print(f"{i}={pais1[i]}")

#Quitar el ultimo atributo de un objeto
pais1.popitem()
for i in pais1:
    print(f"{i}={pais1[i]}")

#Quitar un atributo en especifico de un objeto
pais1.pop("status")
for i in pais1:
    print(f"{i}={pais1[i]}")