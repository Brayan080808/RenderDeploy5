import psycopg2
from psycopg2 import sql
import os

# Variables de conexión
HOST = "dpg-cs4ti85umphs73akbbv0-a"               # Reemplaza con el host de tu base de datos
USERNAME = "dbfreshshopdeploy2_user"        # Reemplaza con tu nombre de usuario
DATABASE_NAME = "dbfreshshopdeploy2" # Reemplaza con el nombre de tu base de datos
PASSWORD = "Tl8etFMP7DI5psIoLLqaAjbVcdhlVtsu"     # Reemplaza con tu contraseña

def enable_pg_trgm():
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            dbname=DATABASE_NAME
        )
        conn.autocommit = True  # Habilitar autocommit para crear extensiones

        with conn.cursor() as cursor:
            # Crear la extensión si no existe
            cursor.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
            print("La extensión pg_trgm se ha habilitado correctamente.")

    except Exception as e:
        print(f"Error al habilitar la extensión pg_trgm: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    enable_pg_trgm()