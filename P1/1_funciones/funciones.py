#Nota: en las funciones indica por numeros, ej: solicitardatos(1), solicitardatos(2), etc.


"""
   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#1.- Funcion que no recibe parametros y no regresa valor
def solicitardatos1():
    nombre=input("nombre: ")
    telefono=input("telefono: ")
    print(f"el nomnre es: {nombre} y su telefono es: {telefono}")

#3-_ funcion que recibe parametros y no regresa valor

def solicitardatos2(nom,tel):
    nombre=nom
    telefono=tel
    print(f"el nombre es:{nombre} y su telefono es: {telefono}")

#2.- funcion que no recibe parametros y regresa valor

def solicitardatos3():
    nombre=input("nombre: ")
    telefono=input("telefono: ")
    return nombre, telefono

#4.- funcion que recibe parametros y regresa valor

def solicitardatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre, telefono

#5.- Invocar las funciones

solicitardatos1()

nombre,telefono=solicitardatos2()
print (f"\n\tAgenda telefonica\n\tNombre: {nombre}\n\tTelefono: {telefono}")

solicitardatos3(nom="daniel guzman",tel="618 213 45 67")

nombre=input("nombre: ")
telefono=input("telefono: ")
solicitardatos3(nombre,telefono)

nombre=input("nombre: ")
telefono=input("telefono: ")
nombre,telefono=solicitardatos4(nombre,telefono)
print (f"\n\tAgenda telefonica\n\tNombre: {nombre}\n\tTelefono: {telefono}")



