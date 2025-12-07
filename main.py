import os
import getpass
import sys

import mysql.connector
from models.UsuarioEmpleado import Usuario
from dao.UsuarioDAO import UsuarioDAO
from dao.EmpleadoDAO import EmpleadoDAO
from utils.generar_pdf import generar_pdf_usuarios

def marcar_fecha_actual():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def revisar_usuario_existente(usuario):
    dao = UsuarioDAO(Usuario())
    sql = 'SELECT nombre_usuario FROM usuario WHERE nombre_usuario = %s'
    datos = dao._UsuarioDAO__conexion.listar_uno(sql, (usuario,))
    dao.cerrar_dao()
    if datos and 'nombre_usuario' in datos:
        return datos['nombre_usuario']
    return

def exportar_usuarios_pdf():
    print('==== Expotar usuarios pdf ====')
    t = Usuario()
    dao = UsuarioDAO(t)
    lista = dao.mostrar_usuarios()
    print(lista)
    generar_pdf_usuarios(lista)

def marcar_fecha_actual():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def crear_usuario():
    print('==== Registrar Nuevo Usuario ====')
    nombre_usuario = input('Nombre de Usuario: ')
    hash_password = input('Ingrese Contraseña: ')
    fecha_ultimo_acceso = marcar_fecha_actual()
    
    print('2. Administrador')
    print('3. Trabajador')
    rol_str = input('Ingrese rol: ')

    # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        usuario = Usuario(
            nombre_usuario=nombre_usuario,
            hash_password=hash_password,
            fecha_ultimo_acceso=fecha_ultimo_acceso,
        )
    except ValueError as e:
        # Aquí llegan las validaciones de Persona/Trabajador (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del trabajador: {e}")
        return

    dao = None
    try:
        dao = UsuarioDAO(usuario)
        dao.crear_usuario()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al registrar trabajador: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al registrar trabajador: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()
            
def iniciar_sesion():
    print('==== Datos de usuario ====')
    usuario = input(str('Ingrese su usuario caracteres en minusculas :')).strip().lower()
    if usuario == '': # Verificar si está vacío
            print('El usuario no puede estar vacío.')
            iniciar_sesion()
    elif ' ' in usuario: # Verificar espacios en blanco
            print('El usuario no puede contener espacios.')
            iniciar_sesion()
    elif len(usuario) < 3: # Verificar longitud mínima
            print('El usuario debe tener al menos 3 caracteres.')
            iniciar_sesion()
    elif not usuario.isalnum(): # Verificar si es alfanumérico
            print('El usuario solo puede contener caracteres alfanuméricos.')
            iniciar_sesion()
    elif usuario.isdigit(): # Verificar si es solo numérico
            print('El usuario no puede ser solo numérico.')
            iniciar_sesion()  
    elif len(usuario) > 20: # Verificar longitud máxima
            print('El usuario no puede tener más de 20 caracteres.')
            iniciar_sesion()
    elif not usuario == revisar_usuario_existente(usuario): # Verificar si el usuario existe
            print('El usuario no existe. Por favor, registrese primero con el administrador de Sistemas.')
            iniciar_sesion()                     
    hash_password = getpass.getpass('Ingrese su contraseña: ').strip()
    # 1) Validaciones del modelo (ValueError)
    try:
        usuario = Usuario(usuario_id=usuario, hash_password=hash_password)
    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
        iniciar_sesion()
    dao = None
    try:
        dao = UsuarioDAO(usuario)
        if dao.iniciar_sesion():            
            empleado_dao = EmpleadoDAO()
            nombre_empleado = empleado_dao.obtener_nombre_empleado_por_usuario(usuario.nombre_usuario)
            # Agrega esta línea para obtener el rol_id
            rol_id = empleado_dao.obtener_rol_id_por_usuario(usuario.nombre_usuario)
            usuario.rol_id = rol_id
            empleado_dao.cerrar_dao()
            if nombre_empleado:
                usuario.nombre = nombre_empleado
            else:
                usuario.nombre = usuario.nombre_usuario
            print(f"\nInicio de sesión exitoso. Bienvenido {usuario.nombre}!")
            # Actualizar fecha_ultimo_acceso en la base de datos
            fecha_actual = marcar_fecha_actual()
            try:
                dao.actualizar_fecha_ultimo_acceso(usuario.nombre_usuario, fecha_actual)
                print(f"Fecha de último acceso actualizada: {fecha_actual}")
            except Exception as e:
                print(f"Error al actualizar la fecha de último acceso: {e}")
            input("Presione Enter para ir al menú principal...")
            menu_principal(usuario)
        else:
            print('Usuario o contraseña incorrectos, intente nuevamente.')
    except mysql.connector.Error as e:
        # Errores propiamente de MySQL (conexión, query, etc.)
        print(f"Error de base de datos al iniciar sesión: {e}")
    except Exception as e:
        # Cualquier cosa inesperada (bug de código, etc.)
        print(f"Se produjo un error inesperado al iniciar sesión: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()

def mostrar_empleados():
    dao = EmpleadoDAO()
    empleados = dao.listar_empleados()
    print("\n=== Empleados registrados ===")
    if empleados:
        for e in empleados:
            print(f"ID: {e['empleado_id']} | Usuario: {e['nombre_usuario']} | Departamento: {e['departamento']} ({e['ubicacion']}) | Rol: {e['rol']} ({e['descripcion']})")
            print("-----------------------")
    else:
        print("No hay empleados registrados.")
    dao.cerrar_dao()

def menu_principal(usuario: Usuario):
    while True:
        # Limpiar pantalla para el menú  tanto en Windows como en Linux/Mac
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== Menu principal ====')
        print(f'Bienvenido: {usuario.nombre}')
        if usuario.rol_id == 2 or usuario.rol_id == 1:
            print('1. Crear usuarios')
            print('2. Exportar usuarios')
        print('3. Ver datos')
        print('0. Cerrar sesion')
        
        opcion = input('Ingrese su opcion: ')
        os.system('clear' if os.name != "nt" else 'cls')
        
        if opcion == '1' and (usuario.rol_id == 2 or usuario.rol_id == 1):
            crear_usuario()

        if opcion == '2' and (usuario.rol_id == 2 or usuario.rol_id == 1):
            exportar_usuarios_pdf()
        
        elif opcion == '3':
            mostrar_empleados()
        
        elif opcion == '0':
            print(f'Hasta luego {usuario.nombre}')
            usuario = None
            break
        
        input('Presione enter para continuar...')
    
def menu_inicio_sesion():    
    while True:
        # Limpiar pantalla
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== Inicio sesion ====')
        print('1. Iniciar sesion')
        print('0. Salir')
        
        opcion = input('Ingrese su opcion: ')
        os.system('clear' if os.name != "nt" else 'cls')

        
        if opcion == '1':
            iniciar_sesion()
        elif opcion == '0':
            print('Saliendo del sistema...')
            break    
        input('Presione enter para continuar...')
    
    
menu_inicio_sesion()