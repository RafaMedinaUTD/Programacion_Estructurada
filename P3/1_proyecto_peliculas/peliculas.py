import mysql.connector
from mysql.connector import Error

pelicula ={}
respuesta = "si"

def borrarPantalla():
    import os
    os.system('cls')

def espereTecla():
    input("\n\t\t Presiona una tecla para continuar ...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        while respuesta := input("\n\t ¿Deseas agregar una nueva pelicula? (Si/No): ").lower().strip() == "si":
            print("\n\t .:: Agregar Películas ::.\n")
            pelicula.update({"nombre": input("\t Ingresa el nombre de la pelicula: ").upper().strip()})
            pelicula.update({"categoria": input("\t Ingresa la categoria de la pelicula: ").upper().strip()})
            pelicula.update({"clasificacion": input("\t Ingresa la clasificacion de la pelicula: ").upper().strip()})
            pelicula.update({"genero": input("\t Ingresa el genero de la pelicula: ").upper().strip()})
            pelicula.update({"idioma": input("\t Ingresa el idioma de la pelicula: ").upper().strip()})

                                     ########### SQL a BD ###########

            cursor=conexionBD.cursor()
            sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values (%s, %s, %s, %s, %s)"
            val=(pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])
            cursor.execute(sql, val)
            conexionBD.commit()
        
            print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
    

def mostrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor= conexionBD.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)

        print("\n\t .:: Mostrar Peliculas ::.\n")
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")
        else:
            print("\n\t .:: No hay peliculas en el sistema ::.")
        print("-"*80)

def buscarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Ingresa el nombre de la pelicula que deseas buscar: ").upper().strip()
        cursor= conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()


        print("\n\t .:: Buscar Peliculas ::.\n")
        if registros:
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")
        else:
            print("\n\t .:: No hay peliculas en el sistema con ese nombre ::.")
        print("-"*80)

def borrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Ingresa el nombre de la pelicula que deseas buscar: ").upper().strip()
        cursor= conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()


        print("\n\t .:: Borrar Peliculas ::.\n")
        if registros:
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")
            print("-"*80)
            resp=input(f"\n\t ¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
            if resp == "si":
                sql="delete from peliculas where nombre=%s"
                cursor.execute(sql, val)
                conexionBD.commit()
                print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
            else:
                print("\n\t\t ::: No se borro la pelicula :::")

        else:
            print("\n\t .:: No hay peliculas en el sistema con ese nombre ::.")

        print("-"*80)
def modificarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Ingresa el nombre de la pelicula que deseas buscar: ").upper().strip()
        cursor= conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()

        print("\n\t .:: Modificar Peliculas ::.\n")
        if registros:
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")
            print("-"*80)

            resp=input(f"\n\t ¿Deseas modificar la pelicula {nombre}? (Si/No): ").lower().strip()
            if resp == "si":
                nuevo_nombre = input("\t Ingresa el nuevo nombre de la pelicula: ").upper().strip()
                nueva_categoria = input("\t Ingresa la nueva categoria de la pelicula: ").upper().strip()
                nueva_clasificacion = input("\t Ingresa la nueva clasificacion de la pelicula: ").upper().strip()
                nuevo_genero = input("\t Ingresa el nuevo genero de la pelicula: ").upper().strip()
                nuevo_idioma = input("\t Ingresa el nuevo idioma de la pelicula: ").upper().strip()

                sql="update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
                val=(nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, nombre)
                cursor.execute(sql, val)
                conexionBD.commit()
                print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
            else:
                print("\n\t\t ::: No se modifico la pelicula :::")

        else:
            print("\n\t .:: No hay peliculas en el sistema con ese nombre ::.")

        print("-"*80)