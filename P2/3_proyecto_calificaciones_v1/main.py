import calificaciones

def main():
    datos = []

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion = False
                calificaciones.borrarPantalla()
                print("\n\t\t Terminaste la ejecución del Sistema ... Gracias ...\U0001F6AA")
                calificaciones.esperarTecla()
            case _:
                calificaciones.borrarPantalla()
                print("\n\t\t \u274COpción Invalida, intenta de nuevo ...\u274C")
                opcion = True
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()