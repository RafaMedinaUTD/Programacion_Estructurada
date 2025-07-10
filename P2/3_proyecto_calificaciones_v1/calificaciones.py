# lista=[
#     ["Ruben",10.0,10.0,10.0]
#     ["Andres",8.0,9.5,6.8]
# ]
lista = []

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t\t \U0001F552Presiona una tecla para continuar ...")

def menu_principal():
    print("\U0001F4C2.:: Sistema de Gestión de Calificaciones ::..\U0001F4C2 \n\t\U00000031\U0000FE0F\U000020E3 " \
    "Agregar \n\t\U00000032\U0000FE0F\U000020E3 Mostrar \n\t\U00000033\U0000FE0F\U000020E3 " \
    "CalcularPromedios \n\t\U00000034\U0000FE0F\U000020E3 Salir")
    opcion=input("Elige una opcion (1-4): ")
    return opcion

def agregar_calificaciones(datos):
    borrarPantalla()
    print("\n\t\U0001F4DD .:: Agregar Calificaciones ::.\U0001F4DD\n")
    nombre = input("\t \U0001F464Nombre del alumno: ").strip().upper()
    calificaciones = []
    for i in range(1,4):
        continua = True
        while continua:
            try:  
                cal=float(input(f"\t \U0001F4E7Calificación #{i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("La calificación debe estar entre 0 y 10")
            except ValueError:
                print("Ingresa un valor numérico")
    lista.append([nombre] + calificaciones)
    print("\n\t\t \u2705::: ¡LA OPERACION SE REALIZO CON EXITO! :::\u2705")

def mostrar_calificaciones(datos):
    borrarPantalla()
    print("\n\t \U0001F4DD.:: Mostrar Calificaciones ::.\U0001F4DD\n")
    if len(lista) > 0:
        print(f"{'Nombre':<15}   {'Calif. 1':<10}   {'Calif. 2':<10}   {'Calif. 3':<10}")
        print("-" * 60)
        for fila in lista:
            print(f"{fila[0]:<15}   {fila[1]:<10}   {fila[2]:<10}   {fila[3]:<10}")
        print("-" * 60)
        cuantos= len(lista)
        print(f"\n \U0001F464Total de alumnos: {cuantos}")
    else:
        print("\n\t \U0001F50D.:: No hay calificaciones en el sistema ::.\U0001F50D")

def calcular_promedios(datos):
    borrarPantalla()
    print("\n\t .:: Calcular Promedios ::.\n")
    if len(lista) > 0:
        print(f"{'Nombre':<15}   {'Promedio':<10}")
        print("-" * 40)
        promedio_grupal = 0
        for fila in lista:
            nombre= fila[0]
            # promedio =(fila[1] + fila[2] + fila[3]) / 3
            promedio =sum(fila[1:])/3
            print(f"{nombre:<15}   {promedio:.2f}")
            promedio_grupal+= promedio
        print("-" * 40)
        promedio_grupal=promedio_grupal / len(lista)
        print(f"\n Promedio grupal: {promedio_grupal:.2f}")
        cuantos= len(lista)
        print(f"\n \U0001F464Total de alumnos: {cuantos}")
    else:
        print("\n\t \u274C.:: No hay calificaciones en el sistema ::.\u274C")