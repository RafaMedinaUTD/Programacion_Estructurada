# base_datos/conector.py
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agsemanal"
        )
        return conexion
    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None
