import os
import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def esperar_tecla():
    input("\n\t\t ⏲️ Presiona una tecla para continuar ...")


def menu_principal():
    borrar_pantalla()
    print("📂 .:: Sistema de Gestión de Calificaciones ::.. 📂")
    print("\t1️⃣ Agregar")
    print("\t2️⃣ Mostrar")
    print("\t3️⃣ Calcular Promedios")
    print("\t4️⃣ Salir")
    opcion = input("Elige una opción (1-4): ")
    return opcion.strip()


def agregar_calificaciones():
    borrar_pantalla()
    print("\n\t📝 .:: Agregar Calificaciones ::. 📝\n")
    nombre = input("\t👤 Nombre del alumno: ").strip().upper()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"\t📧 Calificación #{i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10")
            except ValueError:
                print("Ingresa un valor numérico")

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = ("INSERT INTO calificaciones (alumno, calificacion1, calificacion2, calificacion3, promedio) "
               "VALUES (%s, %s, %s, %s, %s)")
        valores = (nombre, calificaciones[0], calificaciones[1], calificaciones[2], 0)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            print("\n\t✔️  ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!  ✔️")
        except Error as e:
            print(f"Error al insertar datos: {e}")
        finally:
            cursor.close()
            conn.close()
    esperar_tecla()


def mostrar_calificaciones():
    borrar_pantalla()
    print("\n\t📝 .:: Mostrar Calificaciones ::. 📝\n")
    conn = conectar()
    if not conn:
        return

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, alumno, calificacion1, calificacion2, calificacion3, promedio FROM calificaciones")
        filas = cursor.fetchall()
        if filas:
            print(f"{'ID':<3} {'Nombre':<15} {'C1':<6} {'C2':<6} {'C3':<6} {'Promedio':<8}")
            print('-' * 50)
            for f in filas:
                print(f"{f[0]:<3} {f[1]:<15} {f[2]:<6.2f} {f[3]:<6.2f} {f[4]:<6.2f} {f[5]:<8.2f}")
            print('-' * 50)
            print(f"\n👤 Total de alumnos: {len(filas)}")
        else:
            print("\n🔍  No hay calificaciones en el sistema  🔍")
    except Error as e:
        print(f"Error al consultar la base de datos: {e}")
    finally:
        cursor.close()
        conn.close()
        esperar_tecla()


def calcular_promedios():
    borrar_pantalla()
    print("\n\t.:: Calcular Promedios ::.\n")
    conn = conectar()
    if not conn:
        return

    cursor = conn.cursor()
    try:
        actualizar_sql = (
            "UPDATE calificaciones SET promedio = (calificacion1 + calificacion2 + calificacion3) / 3"
        )
        cursor.execute(actualizar_sql)
        conn.commit()

        cursor.execute("SELECT alumno, promedio FROM calificaciones")
        filas = cursor.fetchall()
        if filas:
            print(f"{'Nombre':<15} {'Promedio':<8}")
            print('-' * 30)
            suma = 0
            for nombre, prom in filas:
                print(f"{nombre:<15} {prom:<8.2f}")
                suma += prom
            print('-' * 30)
            grupal = suma / len(filas)
            print(f"\n Promedio grupal: {grupal:.2f}")
            print(f"\n 👤 Total de alumnos: {len(filas)}")
        else:
            print("\n❌  No hay calificaciones en el sistema  ❌")
    except Error as e:
        print(f"Error al actualizar/calcular promedios: {e}")
    finally:
        cursor.close()
        conn.close()
        esperar_tecla()


def main():
    while True:
        opcion = menu_principal()
        if opcion == '1':
            agregar_calificaciones()
        elif opcion == '2':
            mostrar_calificaciones()
        elif opcion == '3':
            calcular_promedios()
        elif opcion == '4':
            print("\n👋 Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            esperar_tecla()


if __name__ == '__main__':
    main()
