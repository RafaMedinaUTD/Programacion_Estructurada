import calificaciones

def main():
    while True:
        opcion = calificaciones.menu_principal()
        if opcion == '1':
            calificaciones.agregar_calificaciones()
        elif opcion == '2':
            calificaciones.mostrar_calificaciones()
        elif opcion == '3':
            calificaciones.calcular_promedios()
        elif opcion == '4':
            print("\n👋 Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
           


if __name__ == '__main__':
    main()