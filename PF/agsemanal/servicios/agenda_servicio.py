from datetime import datetime
import mysql.connector

def crear_agenda(conn):
    agenda = {"Lunes": {}, "Martes": {}, "Miércoles": {}, "Jueves": {}, "Viernes": {}, "Sábado": {}, "Domingo": {}}
    if not conn:
        return agenda
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.dia, a.hora, a.actividad, a.categoria_id, c.nombre
            FROM agenda a
            LEFT JOIN categorias c ON a.categoria_id = c.id;
        """)
        for dia, hora, actividad, categoria_id, categoria_nombre in cursor.fetchall():
            if hasattr(hora, "strftime"):
                hora_str = hora.strftime("%H:%M")
            else:
                try:
                    total_seconds = int(hora.total_seconds())
                    hours = total_seconds // 3600
                    minutes = (total_seconds % 3600) // 60
                    hora_str = f"{hours:02d}:{minutes:02d}"
                except Exception:
                    hora_str = str(hora)
            agenda[dia][hora_str] = {
                "actividad": actividad,
                "categoria_id": categoria_id,
                "categoria": categoria_nombre if categoria_nombre else ""
            }
        cursor.close()
    except mysql.connector.Error:
        pass
    return agenda

def listar_categorias(conn):
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM categorias ORDER BY id;")
        categorias = cursor.fetchall()
        cursor.close()
        return categorias
    except mysql.connector.Error:
        return []

def obtener_nombre_categoria(conn, categoria_id):
    if not conn or not categoria_id:
        return ""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM categorias WHERE id = %s;", (categoria_id,))
        res = cursor.fetchone()
        cursor.close()
        return res[0] if res else ""
    except mysql.connector.Error:
        return ""

def agregar_actividad(conn, agenda, dia, hora, actividad, categoria_id):
    if hora in agenda[dia]:
        return False, "existe"
    if not conn:
        return False, "sin_conexion"
    try:
        cursor = conn.cursor()
        cursor.execute(
            "REPLACE INTO agenda (dia, hora, actividad, categoria_id) VALUES (%s, %s, %s, %s);",
            (dia, hora, actividad, categoria_id)
        )
        conn.commit()
        cursor.close()
        nombre_cat = obtener_nombre_categoria(conn, categoria_id)
        agenda[dia][hora] = {"actividad": actividad, "categoria_id": categoria_id, "categoria": nombre_cat}
        return True, None
    except mysql.connector.Error as e:
        return False, str(e)

def eliminar_actividad(conn, agenda, dia, hora):
    if hora not in agenda[dia]:
        return False, "no_existe"
    if not conn:
        return False, "sin_conexion"
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM agenda WHERE dia = %s AND hora = %s;", (dia, hora))
        conn.commit()
        cursor.close()
        actividad = agenda[dia].pop(hora, None)
        return True, actividad
    except mysql.connector.Error as e:
        return False, str(e)

def reiniciar_dia(conn, agenda, dia):
    if not conn:
        return False, "sin_conexion"
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM agenda WHERE dia = %s;", (dia,))
        conn.commit()
        cursor.close()
        agenda[dia].clear()
        return True, None
    except mysql.connector.Error as e:
        return False, str(e)

def nueva_semana(conn, agenda):
    if not conn:
        return False, "sin_conexion"
    try:
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE agenda;")
        conn.commit()
        cursor.close()
        for d in agenda:
            agenda[d].clear()
        return True, None
    except mysql.connector.Error as e:
        return False, str(e)
