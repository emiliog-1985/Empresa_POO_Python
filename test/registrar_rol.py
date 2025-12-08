import os
import sys
from models.UsuarioEmpleado import Usuario
from models.Conectar import Conectar
import mysql.connector

def registrar_rol_usuario():
    print('==== Registrar roles de Usuario ====' )
    nombre = input('Nombre del rol: ')
    descripcion = input('Descripcion: ')

    rol_id=None
    nombre=nombre
    descripcion=descripcion
    conn = Conectar()
    sql = """
    INSERT INTO rol (nombre, descripcion)
    VALUES (%s, %s)
    """
    datos = (nombre, descripcion)
    try:
        conn.ejecutar(sql, datos)
        print('Rol registrado correctamente.')
    except mysql.connector.Error as e:
        print(f"Error de base de datos: {e}")
    finally:
        conn.cerrar_conexion()

if __name__ == "__main__":
    registrar_rol_usuario()
