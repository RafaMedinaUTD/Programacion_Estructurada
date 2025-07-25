import funciones
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
            else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
            funciones.esperarTecla()

        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email,password)
            if len(lista_usuarios)>0:
              menu_notas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
              print(f"\n\tE-mail y/o contraseña incorrectas por favor verifique ....")
              funciones.esperarTecla()  

        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 


def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo = input("\t Título de la nota: ")
            descripcion = input("\t Descripción de la nota: ")
            #Agregar codigo
            resultado = nota.crear(usuario_id, titulo, descripcion)
            if resultado:
                print(f"\n\tNota creada correctamente.")
            else:
                print(f"\n\tNo fue posible crear la nota en este momento, intentalo mas tarde ...")
            funciones.esperarTecla()

        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
                print(f"\n \t .:: Notas de {nombre} {apellidos} ::. \n")
                print(f"\t {'ID':<10} {'TITULO':<15} {'DESCRIPCION':<15} {'FECHA':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"\t {fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15}")
                print(f"-"*80)
            else:
                print("\n\tNo tienes notas creadas.")
            funciones.esperarTecla()
    
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            resultado = nota.cambiar(id, titulo, descripcion)
            if resultado:
                print(f"\n\tNota actualizada correctamente.")
            else:
                print(f"\n\tNo fue posible actualizar la nota en este momento, intentalo mas tarde ...")
            funciones.esperarTecla()  

        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
                print(f"\n \t .:: Notas de {nombre} {apellidos} ::. \n")
                print(f"\t {'ID':<10} {'TITULO':<15} {'DESCRIPCION':<15} {'FECHA':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"\t {fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15}")
                print(f"-"*80)
            else:
                print("\n\tNo tienes notas creadas.")
            resp=input("¿Deseas borrar alguna nota (Si/No): ").lower().strip()
            if resp=="si":
                id = input("\t \t ID de la nota a eliminar: ")
                #Agregar codigo
                respuesta = nota.borrar(id)
                if respuesta:
                    print(f"\n\tNota eliminada correctamente.")
                else:
                    print(f"\n\tNo fue posible eliminar la nota en este momento, intentalo mas tarde ...")
                funciones.esperarTecla()
            else:
                print("\n\tNo se elimino ninguna nota.")
                funciones.esperarTecla()


        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


