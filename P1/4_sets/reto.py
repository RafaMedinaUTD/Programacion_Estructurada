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