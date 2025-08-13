from base_datos.conector import conectar
from servicios.agenda_servicio import (
    crear_agenda, listar_categorias, agregar_actividad,
    eliminar_actividad, reiniciar_dia, nueva_semana
)
from interfaz.cli import (
    mostrar_menu, obtener_opcion, seleccionar_dia, obtener_hora_valida,
    mostrar_agenda_completa, mostrar_dia, esperar_tecla, mostrar_categorias
)
from exportar.exportador import exportar_agenda

def main():
    conn = conectar()
    agenda = crear_agenda(conn)
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            mostrar_agenda_completa(agenda)

        elif opcion == 2:
            dia = seleccionar_dia(agenda)
            hora = obtener_hora_valida()
            actividad = input("✍️ Describe la actividad: ").strip()
            print()
            mostrar_categorias(conn, listar_categorias)
            try:
                categoria_input = input("\nIngrese ID de categoría (0 para ninguna): ").strip()
                categoria_id = int(categoria_input) if categoria_input != "" else None
                if categoria_id == 0:
                    categoria_id = None
            except ValueError:
                categoria_id = None

            ok, msg = agregar_actividad(conn, agenda, dia, hora, actividad, categoria_id)
            if ok:
                print("\n✅ Actividad agregada.")
            else:
                if msg == "existe":
                    sobrescribir = input("⚠️ Ya existe actividad en esa hora. ¿Desea sobrescribir? (s/n): ").lower()
                    if sobrescribir == 's':
                        if hora in agenda[dia]:
                            agenda[dia].pop(hora, None)
                        ok2, msg2 = agregar_actividad(conn, agenda, dia, hora, actividad, categoria_id)
                        if ok2:
                            print("\n✅ Actividad sobrescrita.")
                        else:
                            print(f"\n❌ Error al sobrescribir: {msg2}")
                    else:
                        print("\nℹ️ Operación cancelada.")
                else:
                    print(f"\n❌ Error: {msg}")
            esperar_tecla()

        elif opcion == 3:
            mostrar_agenda_completa(agenda)
            dia = seleccionar_dia(agenda)
            if not agenda[dia]:
                print("\n⚠️ No hay actividades para eliminar en este día.")
                esperar_tecla()
            else:
                for i, (hora, info) in enumerate(sorted(agenda[dia].items()), 1):
                    cat = f" [{info.get('categoria')}]" if info.get('categoria') else ""
                    print(f"{i}. {hora}: {info.get('actividad')}{cat}")
                try:
                    seleccion = int(input("\nSeleccione el número de actividad a eliminar (0 para cancelar): "))
                    if seleccion == 0:
                        continue
                    hora_sel = list(sorted(agenda[dia].keys()))[seleccion - 1]
                    ok, res = eliminar_actividad(conn, agenda, dia, hora_sel)
                    if ok:
                        print(f"\n👌 Actividad eliminada: {hora_sel} - {res.get('actividad')}")
                    else:
                        print(f"\n❌ Error: {res}")
                except (ValueError, IndexError):
                    print("\n⚠️ Selección inválida.")
                esperar_tecla()

        elif opcion == 4:
            dia = seleccionar_dia(agenda)
            mostrar_dia(agenda, dia)

        elif opcion == 5:
            dia = seleccionar_dia(agenda)
            ok, msg = reiniciar_dia(conn, agenda, dia)
            if ok:
                print(f"\n✅ Todas las actividades del {dia} han sido eliminadas")
            else:
                print(f"\n❌ Error al reiniciar día: {msg}")
            esperar_tecla()

        elif opcion == 6:
            print("\n⚠️  Esta acción reiniciará toda la agenda semanal.")
            confirmacion = input("❓ ¿Estás seguro de que quieres reiniciar la agenda? (s/n): ").lower()
            if confirmacion == 's':
                ok, msg = nueva_semana(conn, agenda)
                if ok:
                    print("\n✅ Agenda reiniciada: Todos los días están ahora vacíos")
                else:
                    print(f"\n❌ Error: {msg}")
            else:
                print("\n❌ Operación cancelada")
            esperar_tecla()

        elif opcion == 7:
            exportar_agenda(agenda)
            esperar_tecla()

        elif opcion == 8:
            print("\n👋 Saliendo...")
            if conn:
                conn.close()
            break

if __name__ == "__main__":
    main()
