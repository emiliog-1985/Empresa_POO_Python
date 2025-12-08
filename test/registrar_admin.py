import os
import sys
from models.UsuarioEmpleado import Usuario
from models.Conectar import Conectar
import mysql.connector

def registrar_admin():
    print('==== Registrar Administrador del Sistema ====' )
    nombre_usuario = input('Nombre de Usuario: ')
    hash_password = input('Ingrese Contraseña: ')
    fecha_ultimo_acceso = None

    usuario = Usuario(
        usuario_id=None,
        nombre=nombre_usuario,
        hash_password=hash_password,
        fecha_ultimo_acceso=fecha_ultimo_acceso
    )
    conn = Conectar()
    # Generar hash y salt
    password_hash, salt = usuario.hash_password(hash_password)
    sql = """
    INSERT INTO usuario (nombre_usuario, hash_password, salt, fecha_ultimo_acceso)
    VALUES (%s, %s, %s, %s)
    """
    datos = (nombre_usuario, password_hash, salt, fecha_ultimo_acceso)
    try:
        conn.ejecutar(sql, datos)
        print('Administrador registrado correctamente.')
    except mysql.connector.Error as e:
        print(f"Error de base de datos: {e}")
    finally:
        conn.cerrar_conexion()

if __name__ == "__main__":
    registrar_admin()
