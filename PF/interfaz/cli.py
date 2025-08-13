from datetime import datetime
import os

def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("\n⏳ Presione Enter para continuar...")

def mostrar_menu():
    borrar_pantalla()
    print("\n📅 --- AGENDA SEMANAL ---")
    print("1. 📋 Mostrar agenda completa")
    print("2. ➕ Agregar actividad")
    print("3. ❌ Eliminar actividad")
    print("4. 🔢 Mostrar actividades de un día")
    print("5. 🔄 Reiniciar día")
    print("6. ♻️ Reiniciar semana")
    print("7. 📤 Exportar agenda a Excel y PDF")
    print("8. ❎ Salir")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("\nSeleccione una opción (1-8): "))
            if 1 <= opcion <= 8:
                return opcion
            print("⚠️ Por favor ingrese un número entre 1 y 8.")
        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese un número.")

def seleccionar_dia(agenda):
    borrar_pantalla()
    dias = list(agenda.keys())
    print("\n🔢 Días disponibles:")
    for i, dia in enumerate(dias, 1):
        print(f"{i}. {dia}")
    while True:
        try:
            seleccion = int(input("\nSeleccione un día (1-7): "))
            if 1 <= seleccion <= 7:
                return dias[seleccion - 1]
            print("⚠️ Por favor ingrese un número entre 1 y 7.")
        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese un número.")

def obtener_hora_valida():
    borrar_pantalla()
    while True:
        horaStr = input("🕒 Ingrese la hora (formato HH:MM): ").strip()
        try:
            hora = datetime.strptime(horaStr, "%H:%M").time()
            return hora.strftime("%H:%M")
        except ValueError:
            print("\n❌ Formato de hora inválido. Use HH:MM.")

def mostrar_agenda_completa(agenda):
    borrar_pantalla()
    print("\n📅 --- AGENDA SEMANAL COMPLETA ---")
    for dia, actividades in agenda.items():
        print(f"\n{dia}:")
        if not actividades:
            print("  ⚠️ No hay actividades programadas")
        else:
            for hora in sorted(actividades.keys()):
                info = actividades[hora]
                cat = f" [{info.get('categoria')}]" if info.get('categoria') else ""
                print(f"  {hora}: {info.get('actividad')}{cat}")
    esperar_tecla()

def mostrar_dia(agenda, dia):
    borrar_pantalla()
    actividades = agenda[dia]
    if not actividades:
        print(f"⚠️ No hay actividades programadas para el {dia}.")
        esperar_tecla()
        return
    print(f"\n📖 --- Actividades del {dia} ---")
    for hora in sorted(actividades.keys()):
        info = actividades[hora]
        cat = f" [{info.get('categoria')}]" if info.get('categoria') else ""
        print(f"{hora}: {info.get('actividad')}{cat}")
    esperar_tecla()

def mostrar_categorias(conn, listar_categorias_fn):
    cats = listar_categorias_fn(conn)
    if cats:
        print("\n📚 --- Categorías ---")
        for cid, nombre in cats:
            print(f"{cid}. {nombre}")
    else:
        print("\n⚠️ No se encontraron categorías.")
