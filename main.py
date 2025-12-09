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


def mantener_empleado():
    #funcion para mantener empleados
    os.system('clear' if os.name != "nt" else 'cls') #limpiar pantalla 
    print('==== Mantenedor de empleados ====')
    print('1. 👥 Crear nuevo empleado')
    print('2. 🔄 Actualizar empleado existente')
    print('3. 📋 Mostrar empleados registrados')
    print('0. 🚪 Salir')
    
    opcion = input('Seleccione una opción: ')
    
    if opcion == '1':
        dao = EmpleadoDAO()
        print('==== Ingrese los datos del nuevo empleado ====')
        usuario_id = input('ID de Usuario asociado: ')
        if usuario_id.strip() == "" or usuario_id is None:
            print('❌ El ID de usuario no puede estar vacío.')
            return
        departamento_id = input('ID de Departamento: ')
        rol_id = input('ID de Rol: ')
        codigo_empleado = input('Codigo de empleado: ')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        direccion = input('Direccion: ')
        telefono = input('Telefono: ')
        email = input('Email: ')
        try:
            dao.crear_empleado(usuario_id, departamento_id, rol_id, codigo_empleado,nombre, apellido, direccion, telefono,email)
            print('✅ Empleado registrado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()

    elif opcion == '2':
        dao = EmpleadoDAO()
        empleado_id = input('Ingrese el ID del empleado a actualizar: ')
        nombre = input('Ingrese el nuevo nombre del empleado: ')
        apellido = input('Ingrese el nuevo apellido del empleado: ')
        direccion = input('Ingrese la nueva direccion del empleado: ')
        telefono = input('Ingrese el nuevo telefono del empleado: ')
        email = input('Ingrese el nuevo email del empleado: ')
        try:
            dao.actualizar_empleado(empleado_id, nombre, apellido, direccion, telefono, email)
            print('✅ Empleado actualizado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()

    elif opcion == '3':
        dao = EmpleadoDAO()
        empleados = dao.mostrar_empleados()
        print('Listado de empleados registrados:')
        for emp in empleados:
            print(f"empleado_id: {emp['empleado_id']}, Nombre: {emp['nombre']}, Apellido: {emp['apellido']}, Direccion: {emp['direccion']}, Telefono: {emp['telefono']}, Email: {emp['email']}")
        dao.cerrar_dao()

    elif opcion == '0':
        print('Saliendo del mantenedor de empleados...')
    else:
        print('Opcion no valida')
        input("⌨️ Presione Enter para continuar...") 

def mantener_rol():
    #funcion para mantener roles
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Mantenedor de roles ====')
    print('1. 👤 Registrar nuevo rol')
    print('2. 🔄 Actualizar rol existente')
    print('3. 📋 Mostrar roles disponibles')
    print('0. 🚪 Salir')
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

def mantener_usuario():
    #funcion para crear un nuevo usuario
    print('==== Mantenedor de usuario ====')
    os.system('clear' if os.name != "nt" else 'cls')
    print('1. 👤 Registrar nuevo usuario')
    print('2. 🔄 Actualizar contraseña de usuario existente')
    print('3. 📋 Mostrar usuarios disponibles')
    print('4. 🗑️  Eliminar usuario existente')
    print('0. 🚪 Salir')
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        dao = UsuarioDAO()
        nombre_usuario = input('Nombre de Usuario: ')
        if nombre_usuario.strip() == "" or nombre_usuario is None or nombre_usuario.isspace() or len(nombre_usuario) <3 or not nombre_usuario.isalnum() or nombre_usuario.isdigit() or len(nombre_usuario) >10:
            print('❌ No cumple con los requisitos minimos para el usuario. Intente nuevamente.')
            return
        hash_password = getpass.getpass('Ingrese Contraseña: ')
        try:
            dao.crear_usuario(nombre_usuario, hash_password)
            print('✅ Usuario registrado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()

    elif opcion == '2':
        dao = UsuarioDAO()
        nombre_usuario = input('Ingrese el Nombre de Usuario a actualizar: ')
        hash_password = getpass.getpass('Ingrese la nueva Contraseña: ')
        try:
            dao.actualizar_usuario(nombre_usuario, hash_password)
            print('✅ Usuario actualizado correctamente.')
        except mysql.connector.Error as e:
            print(f"❌ Error de base de datos: {e}")
        finally:
            dao.cerrar_dao()
    
    elif opcion == '3':
        print('Listado de usuarios disponibles:')
        dao = UsuarioDAO()
        usuarios = dao.mostrar_usuarios()
        for user in usuarios:
            print(f"usuario_id: {user['usuario_id']}, Nombre de Usuario: {user['nombre_usuario']}")
        dao.cerrar_dao()

    elif opcion == '4':
        dao = UsuarioDAO()
        nombre_usuario = input('Ingrese el Nombre de Usuario a eliminar: ')
        print(f'⚠️ Advertencia: Está a punto de eliminar el usuario "{nombre_usuario}". Recuede haberlo eliminado de ser empleado. Esta acción es irreversible.')
        confirmacion = input(f'¿Está seguro que desea eliminar el usuario "{nombre_usuario}"? Esta acción no se puede deshacer. (s/n): ')
        if confirmacion.lower() == 's': 
            try:
                dao.eliminar_usuario(nombre_usuario)
                print('✅ Usuario eliminado correctamente.')
            except mysql.connector.Error as e:
                print(f"❌ Error de base de datos: {e}")
            finally:
                dao.cerrar_dao()
        else:
            print('Operación de eliminación cancelada.')    

    elif opcion == '0':
        print('Saliendo del mantenedor de usuarios...')
    else:
        print('Opcion no valida')
        input("⌨️ Presione Enter para continuar...")

def iniciar_sesion():

    #funcion para iniciar sesion
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== 👤 Datos de usuario ====')
    usuario = input(str('🔠 Ingrese su usuario caracteres en minusculas :')).strip().lower()
    if usuario == '' or usuario is None or usuario == ' ' or usuario.isspace() or len(usuario) < 3 or not usuario.isalnum() or usuario.isdigit() or len(usuario) > 10:
    # Verificar si el usuario está vacío, contiene solo espacios, o es None, verificar longitud mínima y máxima, si es alfanumérico y no solo numérico
            print('😕 ingreso un usuario invalido no cumple con los requisitos, intente nuevamente.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()
            return
    elif not revisar_usuario_existente(usuario): # Verificar si el usuario existe
            input(" ➡️ Presione Enter")
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

def menu_principal(usuario: Usuario):
    #funcion para mostrar el menu principal
    while True:
        # Limpiar pantalla para el menú  tanto en Windows como en Linux/Mac
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('🏠 Menu principal')
        print
        print(f'👋 Hola! Bienvenido: {usuario.nombre}')
        if usuario.rol_id == 1:
            print('========================================')
            print('1. Mantener usuarios 👤 ➜')
            print('2. Mantener empleados 🔐 ➜')
            print('3. Mantener roles 🏷️ ➜')
            print('4. Mantener departamentos 🏢 ➜')
            print('5. Mantener proyectos 📁 ➜')
            print('6. Exportar usuarios PDF📄 ➜')
            print('0. Cerrar sesion 🚪➜')
            print ('========================================')
        elif usuario.rol_id == 3 or usuario.rol_id == 2 or usuario.rol_id == 1:
            print('========================================')   
            print('6. Exportar usuarios PDF📄 ➜')
            print('0. Cerrar sesion 🚪 ➜')
            print ('========================================')
        opcion = input('✅ Ingrese su opcion: ')
        print('=======================')
        os.system('clear' if os.name != "nt" else 'cls')
        
        if opcion == '1' and (usuario.rol_id == 1):
            mantener_usuario()

        elif opcion == '2' and (usuario.rol_id == 1):
            mantener_empleado()    
        
        elif opcion == '3' and (usuario.rol_id == 1):
            mantener_rol()
        
        elif opcion == '4' and (usuario.rol_id == 1):
            mantener_departamentos()

        elif opcion == '5' and (usuario.rol_id == 1):
            print('Proyectos no implementado aún.')    

        elif opcion == '6' and (usuario.rol_id == 3 or usuario.rol_id == 2 or usuario.rol_id == 1):
            print('Exportando usuarios a PDF no implementado aún.')
        

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
        print('==== 👥 Menu inicio sesión ====')
        print('==== 1. Iniciar sesión 🔑 ➜   =')
        print('==== 0. Salir 🚪 ➜            =')
        print('===============================')
        
        opcion = input('✅ Ingrese su opcion: ')
        os.system('clear' if os.name != "nt" else 'cls')

        
        if opcion == '1':
            iniciar_sesion()
        elif opcion == '0':
            print('=============================')
            print('======👋 ¡Hasta luego! ======')
            print('==Saliendo del sistema...====')
            print('=============================')
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