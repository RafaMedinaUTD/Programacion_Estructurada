#Dict u objeto que permita almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero,
# idioma) de peliculas

pelicula ={}
respuesta = "si"

def borrarPantalla():
    import os
    os.system('cls')

def espereTecla():
    input("\n\t\t Presiona una tecla para continuar ...")

def crearPeliculas():
    borrarPantalla()
    while respuesta := input("\n\t ¿Deseas agregar una nueva pelicula? (Si/No): ").lower().strip() == "si":
         print("\n\t .:: Agregar Películas ::.\n")
         pelicula.update({"nombre": input("\t Ingresa el nombre de la pelicula: ").upper().strip()})
         pelicula.update({"categoria": input("\t Ingresa la categoria de la pelicula: ").upper().strip()})
         pelicula.update({"clasificacion": input("\t Ingresa la clasificacion de la pelicula: ").upper().strip()})
         pelicula.update({"genero": input("\t Ingresa el genero de la pelicula: ").upper().strip()})
         pelicula.update({"idioma": input("\t Ingresa el idioma de la pelicula: ").upper().strip()})
    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t .:: Mostrar Peliculas ::.\n")

    if len(pelicula) >0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
    else:
        print("\n\t .:: No hay peliculas en el sistema ::.")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t .:: Borrar Peliculas ::.\n")
    if len(pelicula) == 0:
        print("\n\t No hay peliculas en el sistema.")
    else:
        resp=input("¿Deseas borrar la pelicula? (Si/No): ").lower().strip()
        if resp == "si":
            pelicula.clear()
            print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t .:: Agregar Característica a Peliculas ::.\n")
    if len(pelicula) == 0:
        print("\n\t No hay peliculas en el sistema.")
    else:
        carac = input("\t Ingresa la característica a agregar: ").upper().strip()
        valor = input(f"\t Ingresa el valor para '{carac}': ").upper().strip()
        pelicula.update({carac: valor})
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t .:: Modificar Característica de Peliculas ::.\n")
    if len(pelicula) == 0:
        print("\n\t No hay peliculas en el sistema.")
    else:
        for caracteristica in pelicula:
            resp = input(f"\t ¿Deseas modificar la característica '{caracteristica}'? (Si/No): ").lower().strip()
            if resp == "si":
                nuevo_valor = input(f"\t Ingresa el nuevo valor para '{caracteristica}': ").upper().strip()
                pelicula[caracteristica] = nuevo_valor
                print(f"\n\t La característica '{caracteristica}' ha sido modificada a '{nuevo_valor}'.")
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")



def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t .:: Borrar Característica de Peliculas ::.\n")
    if len(pelicula) == 0:
        print("\n\t No hay peliculas en el sistema.")
    else:
          for i in pelicula:
            print(f"{i} : {pelicula[i]}")
    caracborrar = input(f"\t ¿Que caracteristica deseas borrar?: ").lower().strip()
    if caracborrar in pelicula:
        del pelicula[caracborrar]
        print(f"\n\t La característica '{caracborrar}' ha sido borrada.")
    else:
        print(f"\n\t La característica '{caracborrar}' no existe en la lista de peliculas.")