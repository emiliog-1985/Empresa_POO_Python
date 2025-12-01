import os
import sys
import mysql.connector
from datetime import date

from models.Usuario import Usuario
from dao.UsuarioDAO import UsuarioDAO
from models.RegistroTiempo import RegistroTiempo
from dao.RegistroTiempoDAO import RegistroTiempoDAO

def crear_registro_tiempo(user: Usuario):
    print('==== Crear Registro Tiempo ====')
    try:
        proyecto_id = int(input('Ingrese proyecto id: \n'))
        horas_trabajo = float(input('Ingrese horas trabajadas: \n'))
    except ValueError:
        print('Debe ingresar los datos como números')
    empleado_id = user.empleado_id
    descripcion = input('Ingrese descripcion: \n')
    fecha = date.today()
     # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        registro_tiempo = RegistroTiempo(
            empleado_id = empleado_id,
            proyecto_id = proyecto_id,
            horas_trabajo = horas_trabajo,
            descripcion = descripcion,
            fecha = fecha)
    except ValueError as e:
        # Aquí llegan las validaciones de Persona/Trabajador (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del registro tiempo: {e}")
        return
    dao = None
    try:
        dao = RegistroTiempoDAO(registro_tiempo)
        dao.crear_registro_tiempo()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al registrar tiempo: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al registrar tiempo: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()

def iniciar_sesion(): # Función para iniciar sesión
    usuario = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
    # Instanciando objeto tipo usuario
    user = Usuario(usuario=usuario, password=password)
    # Instanciamos objeto dao para usuario
    dao = UsuarioDAO(user)
    if dao.iniciar_sesion():
        menu_sesion(user)
    else:
        print('Error en datos, intente nuevamente.')

def menu_principal():# Menú principal de la aplicación
    while True:
        os.system('clear') # Limpiar la pantalla
        print('=== Menu Principal ===') # Menu principal
        print('1. Iniciar Sesión')
        print('0. Salir')

        option = input('Seleccione una opción: ')
        
        if option == '1':
            iniciar_sesion()
        elif option == '0':
            os.system('clear')
            print('Saliendo del programa hasta luego...')
            break
            
def menu_sesion(user: Usuario):
    while True:
        # Limpiar pantalla
        os.system('clear')
        # Cargamos opciones
        print('==== Menú principal ====')
        os.system('clear')
        print(f'Bienvenido: {user.nombre} {user.apellido}')
        print('1.')
        print('2.')
        print('0. Cerrar sesión')
        opcion = input('Ingrese su opción:\n')
        
        if opcion == '0':
            print(f'Hasta luego {user.nombre} {user.apellido}')
            user = None
            break
        
        input('Presione enter para continuar...')

menu_principal()
