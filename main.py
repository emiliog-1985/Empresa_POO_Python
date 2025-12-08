import os
import getpass
import sys
import mysql.connector

from models.UsuarioEmpleado import Usuario
from dao.UsuarioDAO import UsuarioDAO
from dao.EmpleadoDAO import EmpleadoDAO
from dao.DepartamentoDAO import DepartamentoDAO
from dao.RolDAO import RolDAO
from utils.generar_pdf import generar_pdf_usuarios


def crear_empleado():
    #funcion para crear un nuevo empleado
    print('==== Registrar nuevo empleado ====')
    usuario_id = input('ID de Usuario asociado: ')
    departamento_id = input('ID de Departamento: ')
    rol_id = input('ID de Rol: ')
    codigo_empleado = input('Codigo de empleado: ')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    direccion = input('Direccion: ')
    telefono = input('Telefono: ')
    email = input('Email: ')
    dao = EmpleadoDAO()
    try:
        dao.crear_empleado(usuario_id, departamento_id, rol_id, codigo_empleado,nombre, apellido, direccion, telefono,email)
        print('✅ Empleado registrado correctamente.')
    except mysql.connector.Error as e:
        print(f"❌ Error de base de datos: {e}")
    finally:
        dao.cerrar_dao()



def mantener_rol():
    #funcion para mantener roles
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Mantenedor de roles ====')
    print('1. Registrar nuevo rol')
    print('2. Actualizar rol existente')
    print('3. Mostrar roles disponibles')
    print('0. Salir')
    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        dao = RolDAO()
        nombre = input('Ingrese el nombre del rol: ')
        descripcion = input('Ingrese la descripcion del rol: ')
        try:
            dao.crear_rol(nombre, descripcion)
            print('✅ Rol registrado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()
    elif opcion == '2':
        dao = RolDAO()
        rol_id = input('Ingrese el ID del rol a actualizar: ')
        nombre = input('Ingrese el nuevo nombre del rol: ')
        descripcion = input('Ingrese la nueva descripcion del rol: ')
        try:
            dao.actualizar_rol(rol_id, nombre, descripcion)
            print('✅ Rol actualizado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()
    elif opcion == '3':
        print('Listado de roles disponibles:')
        dao = RolDAO()
        roles = dao.mostrar_roles()
        for rol in roles:
            print(f"rol_id: {rol['rol_id']}, Nombre: {rol['nombre']}, Descripcion: {rol['descripcion']}")
        dao.cerrar_dao()

    elif opcion == '0':
        print('Saliendo del mantenedor de roles...')
    else:
        print('Opcion no valida')
        input("⌨️ Presione Enter para continuar...")


def mantener_departamentos():
    #funcion para agregar y asignar departamentos a usuarios
    print('==== Mantenedor de departamentos ====')
    print('1. Registrar nuevo departamento')
    print('2. Actualizar departamento existente')
    print('3. Mostrar departamentos disponibles')
    print('0. Salir')
    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        dao = DepartamentoDAO()
        nombre = input('Ingrese el nombre del departamento: ')
        ubicacion = input('Ingrese la ubicacion del departamento: ')
        try:
            dao.crear_departamento(nombre, ubicacion)
            print('✅ Departamento registrado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()
    elif opcion == '2':
        dao = DepartamentoDAO()
        departamento_id = input('Ingrese el ID del departamento a actualizar: ')
        nombre = input('Ingrese el nuevo nombre del departamento: ')
        ubicacion = input('Ingrese la nueva ubicacion del departamento: ')
        try:
            dao.actualizar_departamento(departamento_id, nombre, ubicacion)
            print('✅ Departamento actualizado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()
    elif opcion == '3':
        print('Listado de departamentos disponibles:')
        dao = DepartamentoDAO()
        departamentos = dao.mostrar_departamentos()
        for dept in departamentos:
            print(f"departamento_id: {dept['departamento_id']}, Nombre: {dept['nombre']}, Ubicacion: {dept['ubicacion']}")
            dao.cerrar_dao()
    elif opcion == '0':
        print('Saliendo del mantenedor de departamentos...')
        
    else:
        print('Opcion no valida')
        input("⌨️ Presione Enter para continuar...")


def marcar_fecha_actual():
    #funcion para obtener la fecha y hora actual
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def revisar_usuario_existente(nombre_usuario):
    dao = UsuarioDAO()
    existe = dao.existe_usuario(nombre_usuario)
    dao.cerrar_dao()
    if not existe:
        print('👻 El usuario no existe. Por favor, registrese primero con el administrador de Sistemas.')
    return existe


def crear_usuario():
    #funcion para crear un nuevo usuario
    print('==== Registrar nuevo usuario ====')
    nombre_usuario = input('Nombre de Usuario: ')
    hash_password = getpass.getpass('Ingrese Contraseña: ')
    
    dao = UsuarioDAO()
    try:
        dao.crear_usuario(nombre_usuario, hash_password)
        print('✅ Usuario registrado correctamente.')
    except mysql.connector.Error as e:
        print(f"❌ Error de base de datos: {e}")
    finally:
        dao.cerrar_dao()


def iniciar_sesion():
    #funcion para iniciar sesion
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== 👤 Datos de usuario ====')
    usuario = input(str('🔠 Ingrese su usuario caracteres en minusculas :')).strip().lower()
    if usuario == '': # Verificar si está vacío
            print('😕 El usuario no puede estar vacío.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif ' ' in usuario: # Verificar espacios en blanco
            print('😕 El usuario no puede contener espacios.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif len(usuario) < 3: # Verificar longitud mínima
            print('😕 El usuario debe tener al menos 3 caracteres.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif not usuario.isalnum(): # Verificar si es alfanumérico
            print('😕 El usuario solo puede contener caracteres alfanuméricos.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif usuario.isdigit(): # Verificar si es solo numérico
            print('😕 El usuario no puede ser solo numérico.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif len(usuario) > 20: # Verificar longitud máxima
            print('😕 El usuario no puede tener más de 20 caracteres.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif not revisar_usuario_existente(usuario): # Verificar si el usuario existe
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return

    hash_password = getpass.getpass('🔑 Ingrese su contraseña: ').strip()

    try:
        usuario = Usuario(usuario_id=usuario, hash_password=hash_password)
    except ValueError as e:
        print(f"⚠️ Error en los datos ingresados: {e}")
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
            print(f"\n 👍 Inicio de sesión exitoso. 👋 Bienvenido {usuario.nombre}!")
            # Actualizar fecha_ultimo_acceso en la base de datos
            fecha_actual = marcar_fecha_actual()
            try:
                dao.actualizar_fecha_ultimo_acceso(usuario.nombre_usuario, fecha_actual)
                print(f" ⏱️ Fecha de último acceso actualizada: {fecha_actual}")
            except Exception as e:
                print(f" ⚠️ Error al actualizar la fecha de último acceso: {e}")
            input("Presione Enter para ir al menú principal...")
            menu_principal(usuario)
        else:
            print('⚠️ Usuario o contraseña incorrectos, intente nuevamente.')
    except mysql.connector.Error as e:
        # Errores propiamente de MySQL (conexión, query, etc.)
        print(f" ⚠️ Error de base de datos al iniciar sesión: {e}")
    except Exception as e:
        # Cualquier cosa inesperada (bug de código, etc.)
        print(f" ⚠️ Se produjo un error inesperado al iniciar sesión: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()

def mostrar_empleados():
    #funcion para mostrar los empleados registrados
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
    #funcion para mostrar el menu principal
    while True:
        # Limpiar pantalla para el menú  tanto en Windows como en Linux/Mac
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('🏠 Menu principal')
        print
        print(f'👋 Hola! Bienvenido: {usuario.nombre}')
        if usuario.rol_id == 2 or usuario.rol_id == 1:
            print('========================================')
            print('1. Crear usuarios 👤 ➜')
            print('2. Crear Empleados 🔐 ➜')
            print('3. Mantener roles 🔐 ➜')
            print('4. Mantener departamentos 🏢 ➜')
            print('5. Proyectos 📂 ➜')
            print('6. Exportar usuarios PDF📄 ➜')
            print('7. Ver datos empleados 👀 ➜')
            print('========================================')
            print('0. Cerrar sesion 🚪 ➜')
            print ('========================================')
        opcion = input('✅ Ingrese su opcion: ')
        print('=======================')
        os.system('clear' if os.name != "nt" else 'cls')
        
        if opcion == '1' and (usuario.rol_id == 1):
            crear_usuario()

        elif opcion == '2' and (usuario.rol_id == 1):
            crear_empleado()    
        
        elif opcion == '3' and (usuario.rol_id == 2 or usuario.rol_id == 1):
            mantener_rol()
        
        elif opcion == '4' and (usuario.rol_id == 2 or usuario.rol_id == 1):
            mantener_departamentos()

        elif opcion == '5' and (usuario.rol_id == 2 or usuario.rol_id == 1):
            print('Proyectos no implementado aún.')    

        elif opcion == '6' and (usuario.rol_id == 3 or usuario.rol_id == 2 or usuario.rol_id == 1):
            print('Exportando usuarios a PDF no implementado aún.')
        

        elif opcion == '7' and (usuario.rol_id == 1):    
            print('Mantenedor de empleados no implementado aún.')

        elif opcion == '0':
            print(f'Hasta luego {usuario.nombre}')
            usuario = None
            break
        
        input('Presione enter para continuar...')
    
def menu_inicio_sesion():
    #funcion para mostrar el menu de inicio de sesion    
    while True:
        # Limpiar pantalla
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== 👥 Menu Inicio sesión ====')
        print('==== 1. Iniciar sesión 🔑 ➜   =')
        print('==== 0. Salir 🚪 ➜            =')
        print('===============================')
        
        opcion = input('✅ Ingrese su opcion: ')
        os.system('clear' if os.name != "nt" else 'cls')

        
        if opcion == '1':
            iniciar_sesion()
        elif opcion == '0':
            print('▶ Saliendo del sistema...')
            break    
        input(' ↳ presione intro para continuar...')
    
if __name__ == "__main__":
    try:
        menu_inicio_sesion()
    except KeyboardInterrupt:
        print('\n\n⚠️ El programa fue interrumpido por el usuario.')
        print('👋 ¡Hasta luego!')
    except Exception as e:
        print(f'\n\n❌ Error inesperado: {e}')   