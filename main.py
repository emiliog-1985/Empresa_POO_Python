import os
import mysql.connector
from datetime import date

from models.Usuario import Usuario
from dao.UsuarioDAO import UsuarioDAO
from models.RegistroTiempo import RegistroTiempo
from dao.RegistroTiempoDAO import RegistroTiempoDAO
from models.Proyecto import Proyecto
from dao.ProyectoDAO import ProyectoDAO

def menu_proyectos():
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Menú Proyectos ====')
        print('1. Listar proyectos')
        print('2. Crear proyecto')
        print('3. Editar proyecto')
        print('4. Eliminar proyecto')
        print('0. Atrás')
        opcion = input('Seleccione una opción: \n')
        
        if opcion == '1':
            os.system('cls')
            print('==== Listar proyectos ====')
            proyecto = Proyecto
            dao = ProyectoDAO(proyecto)
            dao.listar_proyectos()
            if dao is not None:
                dao.cerrar_dao()
            
        elif opcion == '2':
            crear_proyecto()
        
        elif opcion == '3':
            actualizar_proyecto()
        
        elif opcion == '4':
            eliminar_proyecto()
        
        elif opcion == '0':
            break
        
        else:
            print('Debe seleccionar una opción válida')
            
        input('Presione enter para continuar...')

def eliminar_proyecto():
    os.system('cls')
    print('==== Eliminar proyecto ====')
    try:
        proyecto_id = int(input('Ingrese el id del proyecto a eliminar: \n'))
    except ValueError:
        print('El ID del proyecto debe ser un número entero')
        return
    opcion = input('¿Está seguro de eliminar este proyecto?: \n').lower()
    if opcion == 'si':
        proyecto = Proyecto(proyecto_id=proyecto_id)
        dao = ProyectoDAO(proyecto)
        try:
            dao.eliminar_proyecto()
        except mysql.connector.Error as e:
            # Excepción específica de mysql.connector
            print(f"Error de base de datos al eliminar proyecto: {e}")
        except Exception as e:
            # Cualquier otro error INESPERADO
            print(f"Error inesperado al eliminar proyecto: {e}")
        finally:
            if dao is not None:
                dao.cerrar_dao()
        
def actualizar_proyecto():
    os.system('cls')
    print('==== Actualizar proyecto ====')
    try:
        proyecto_id = int(input('Ingrese el id del proyecto: \n'))
    except ValueError:
        print('El ID del proyecto debe ser un número entero')
        return
    nombre_proyecto = input('Ingrese el nuevo nombre del proyecto: \n')
    fecha_1 = input('Ingrese la nueva fecha de inicio YYYY-MM-DD: \n')
    fecha_2 = input('Ingrese la nueva fecha de término YYYY-MM-DD: \n')
    try:
        fecha_inicio = date.fromisoformat(fecha_1)
        fecha_termino = date.fromisoformat(fecha_2)
    except ValueError as e:
        print(f"Error en datos de las fechas: {e}")
        return
    if fecha_termino < fecha_inicio:
        print('La fecha de inicio debe ser anterior a la fecha de término')
        return 
    descripcion = input('Ingrese la nueva descripción del proyecto: \n')
    print('1. Planificación')
    print('2. En Progreso')
    print('3. Finalizado')
    print('4. Pausado')
    estado = input('Ingrese el nuevo estado del proyecto: \n')
     # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        proyecto = Proyecto(proyecto_id = proyecto_id,
            nombre_proyecto = nombre_proyecto, 
            fecha_inicio = fecha_inicio,
            fecha_termino = fecha_termino,
            descripcion = descripcion,
            estado = estado)
    except ValueError as e:
        # Aquí llegan las validaciones de proyecto (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del proyecto: {e}")
        return

    dao = None
    try:
        dao = ProyectoDAO(proyecto)
        dao.actualizar_proyecto()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al actualizar proyecto: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al actualizar proyecto: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()
        
def crear_proyecto():
    os.system('cls')
    print('==== Crear proyecto ====')
    nombre_proyecto = input('Ingrese el nombre del proyecto: \n')
    fecha_1 = input('Ingrese fecha de inicio YYYY-MM-DD: \n')
    fecha_2 = input('Ingrese fecha de término YYYY-MM-DD: \n')
    try:
        fecha_inicio = date.fromisoformat(fecha_1)
        fecha_termino = date.fromisoformat(fecha_2)
    except ValueError as e:
        print(f"Error en datos de las fechas: {e}")
        return
    if fecha_termino < fecha_inicio:
        print('La fecha de inicio debe ser anterior a la fecha de término')
        return 
    descripcion = input('Ingrese la descripción del proyecto: \n')
    print('1. Planificación')
    print('2. En Progreso')
    print('3. Finalizado')
    print('4. Pausado')
    estado = input('Ingrese el estado del proyecto: \n')
    
     # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        proyecto = Proyecto(
            nombre_proyecto = nombre_proyecto, 
            fecha_inicio = fecha_inicio,
            fecha_termino = fecha_termino,
            descripcion = descripcion,
            estado = estado)
    except ValueError as e:
        # Aquí llegan las validaciones de proyecto (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del proyecto: {e}")
        return

    dao = None
    try:
        dao = ProyectoDAO(proyecto)
        dao.crear_proyecto()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al registrar proyecto: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al registrar proyecto: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()
            

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
        os.system('cls') # Limpiar la pantalla
        print('=== Menu Principal ===') # Menu principal
        print('1. Iniciar Sesión')
        print('0. Salir')

        option = input('Seleccione una opción: ')
        
        if option == '1':
            iniciar_sesion()
        elif option == '0':
            os.system('cls')
            print('Saliendo del programa hasta luego...')
            break
            
def menu_sesion(user: Usuario):
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Menú principal ====')
        os.system('cls')
        print(f'Bienvenido: {user.nombre} {user.apellido}')
        print('1.')
        print('2. Crear registro tiempo')
        print('3. Menú de proyectos')
        print('0. Cerrar sesión')
        opcion = input('Ingrese su opción:\n')
        
        if opcion == '1':
            pass
        
        elif opcion == '3':
            menu_proyectos()
        
        elif opcion == '2':
            crear_registro_tiempo(user)
            
        elif opcion == '0':
            print(f'Hasta luego {user.nombre} {user.apellido}')
            user = None
            break
        
        input('Presione enter para continuar...')

menu_principal()