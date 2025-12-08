import os
import sys

from dao.UsuarioDAO import UsuarioDAO
from dao.DepartamentoDAO import DepartamentoDAO
from dao.RolDAO import RolDAO
from models.UsuarioEmpleado import Usuario
from models.Conectar import Conectar
import mysql.connector

def mostrar_usuarios_con_dao():
    dao = UsuarioDAO(Usuario())
    usuarios = dao.mostrar_usuarios()
    print("\n=== Usuarios ===")
    if usuarios:
        for u in usuarios:
            print(f"ID: {u['usuario_id']} | Usuario: {u['nombre_usuario']}")
            print("-----------------------")
    else:
        print("No hay usuarios registrados.")
    dao.cerrar_dao()
    return usuarios

def mostrar_departamentos_con_dao():
    dao = DepartamentoDAO()
    departamentos = dao.mostrar_departamentos()
    print("\n=== Departamentos ===")
    if departamentos:
        for d in departamentos:
            print(f"ID: {d['departamento_id']} | Nombre: {d['nombre']} | Ubicación: {d['ubicacion']}")
            print("-----------------------")
    else:
        print("No hay departamentos registrados.")
    dao.cerrar_dao()
    return departamentos

def mostrar_roles_con_dao():
    dao = RolDAO()
    roles = dao.mostrar_roles()
    print("\n=== Roles ===")
    if roles:
        for r in roles:
            print(f"ID: {r['rol_id']} | Nombre: {r['nombre']} | Descripción: {r['descripcion']}")
            print("-----------------------")
    else:
        print("No hay roles registrados.")
    dao.cerrar_dao()
    return roles

def registrar_empleado():
    print("==== Registrar nuevo empleado ====")
    mostrar_usuarios_con_dao()
    usuario_id = int(input("Ingrese el ID del usuario: "))

    mostrar_departamentos_con_dao()
    departamento_id = int(input("Ingrese el ID del departamento: "))

    mostrar_roles_con_dao()
    rol_id = int(input("Ingrese el ID del rol: "))
    
    codigo_empleado = input("Ingrese el código del empleado: ")
    print("-----------------------")
    nombre = input("Ingrese el nombre del empleado: ")
    print("-----------------------")
    apellido = input("Ingrese el apellido del empleado: ")
    print("-----------------------")
    direccion = input("Ingrese la dirección del empleado: ")
    print("-----------------------")
    telefono = input("Ingrese el teléfono del empleado: ")
    print("-----------------------")
    email = input("Ingrese el email del empleado: ")
    print("-----------------------")
    conn = Conectar()
    sql = "INSERT INTO empleado (usuario_id, departamento_id, rol_id, codigo_empleado, nombre, apellido, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    datos = (usuario_id, departamento_id, rol_id, codigo_empleado, nombre, apellido, direccion, telefono, email)
    try:
        conn.ejecutar(sql, datos)
        print("Empleado registrado correctamente.")
    except mysql.connector.Error as e:
        print(f"Error al registrar empleado: {e}")
    finally:
        conn.cerrar_conexion()

if __name__ == "__main__":
    registrar_empleado()

