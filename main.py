import os
import mysql.connector
import datetime
from datetime import date
from utils.generar_pdf import generar_pdf
from models.Usuario import Usuario
from dao.UsuarioDAO import UsuarioDAO
from models.RegistroTiempo import RegistroTiempo
from dao.RegistroTiempoDAO import RegistroTiempoDAO
from models.Proyecto import Proyecto
from dao.ProyectoDAO import ProyectoDAO
from models.DetalleProyecto import DetalleProyecto
from dao.DetalleProyectoDAO import DetalleProyectoDAO
from models.Departamento import Departamento
from dao.DepartamentoDAO import DepartamentoDAO


def exportar_departamentos(): # Función para exportar departamentos en formato pdf
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Exportar Departamentos ====')
    departamento = Departamento
    dao = DepartamentoDAO(departamento)
    lista = dao.mostrar_departamentos()
    nombre_archivo = 'reporte_departamentos.pdf'
    generar_pdf(lista, nombre_archivo)
    if dao is not None:
        dao.cerrar_dao()

def exportar_empleados(): # Función para exportar empleados en formato pdf
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Exportar Empleados ====')
    usuario = Usuario
    dao = UsuarioDAO(usuario)
    lista = dao.mostrar_usuarios()
    nombre_archivo = 'reporte_empleados.pdf'
    generar_pdf(lista, nombre_archivo)
    if dao is not None:
        dao.cerrar_dao()

def exportar_registro_tiempo(): # Función para exportar registros de tiempo en formato pdf
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Exportar Registro Tiempo ====')
    registro_tiempo = RegistroTiempo
    dao = RegistroTiempoDAO(registro_tiempo)
    lista = dao.mostrar_registros()
    nombre_archivo = 'reporte_registro_tiempo.pdf'
    generar_pdf(lista, nombre_archivo)
    if dao is not None:
        dao.cerrar_dao()

def exportar_proyectos(): # Función para exportar proyectos en formato pdf
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Exportar Proyectos ====')
    proyecto = Proyecto
    dao = ProyectoDAO(proyecto)
    lista = dao.mostrar_proyectos()
    nombre_archivo = 'reporte_proyectos.pdf'
    generar_pdf(lista, nombre_archivo)
    if dao is not None:
        dao.cerrar_dao()

def menu_proyectos(): # Función para el menú de proyectos
    while True:
        # Limpiar pantalla
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== Menú Proyectos ====')
        print('1. Listar proyectos')
        print('2. Crear proyecto')
        print('3. Editar proyecto')
        print('4. Eliminar proyecto')
        print('5. Asignar empleado a proyecto')
        print('6. Desasignar empleado de proyecto')
        print('7. Generar reporte de proyectos')
        print('0. Atrás')
        opcion = input('Seleccione una opción: \n')
        
        if opcion == '1':
            os.system('clear' if os.name != "nt" else 'cls')
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
            
        elif opcion == '5':
            asignar_proyecto()
        
        elif opcion == '6':
            desasignar_proyecto()
            
        elif opcion == '7':
            exportar_proyectos()
        
        elif opcion == '0':
            break
        
        else:
            print('Debe seleccionar una opción válida')
            
        input('Presione enter para continuar...')
        
def asignar_proyecto(): # Función para asignar un empleado a un proyecto
    print('==== Asignar empleado a proyecto ====')
    try:
        empleado_id = int(input('Ingrese el id de empleado: \n'))
        proyecto_id = int(input('Ingrese el id de proyecto: \n'))
        horas_asignadas = int(input('Ingrese la cantidad de horas asignadas: \n'))
    except ValueError:
        print('Debe ingresar los id y las horas como números enteros')
        return
    fecha_asignacion = datetime.datetime.now()
    rol_en_proyecto = input('Ingrese el rol en proyecto: \n')
     # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        detalle_proyecto = DetalleProyecto(
            empleado_id = empleado_id, 
            proyecto_id = proyecto_id,
            fecha_asignacion = fecha_asignacion,
            rol_en_proyecto = rol_en_proyecto,
            horas_asignadas = horas_asignadas)
    except ValueError as e:
        # Aquí llegan las validaciones de proyecto (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del empleado/proyecto: {e}")
        return

    dao = None
    try:
        dao = DetalleProyectoDAO(detalle_proyecto)
        dao.asignar_proyecto()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al asignar empleado a proyecto: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al asignar empleado a proyecto: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()

def desasignar_proyecto(): # Función para desasigar un empleado de un proyecto
    print('==== Desasignar empleado de proyecto ====')
    try:
        empleado_id = int(input('Ingrese el id de empleado: \n'))
        proyecto_id = int(input('Ingrese el id de proyecto: \n'))
    except ValueError:
        print('Debe ingresar los id como números enteros')
        return
    opcion = input('¿Está seguro de desasignar el empleado al proyecto?').lower()
    if opcion == 'si':
        detalle_proyecto = DetalleProyecto(empleado_id = empleado_id, proyecto_id = proyecto_id)
        dao = DetalleProyectoDAO(detalle_proyecto)
        try:
            dao.desasignar_proyecto()
        except mysql.connector.Error as e:
            # Excepción específica de mysql.connector
            print(f"Error de base de datos al desasignar empleado de proyecto: {e}")
        except Exception as e:
            # Cualquier otro error INESPERADO
            print(f"Error inesperado al desasignar empleado de proyecto: {e}")
        finally:
            if dao is not None:
                dao.cerrar_dao()
    
def eliminar_proyecto(): # Función para eliminar un proyecto
    os.system('clear' if os.name != "nt" else 'cls')
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
        
def actualizar_proyecto(): # Función para actualizar un proyecto
    os.system('clear' if os.name != "nt" else 'cls')
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
        
def crear_proyecto(): # Función para crear un proyecto
    os.system('clear' if os.name != "nt" else 'cls')
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
            
def crear_registro_tiempo(user: Usuario): # Función para crear un registro de tiempo
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

def menu_departamentos(): # Función para el menú de departamentos
    while True:
        # Limpiar pantalla
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== Menú de Departamentos ====')
        print('4. Generar informe de departamentos en pdf')
        print('0. Atrás')
        opcion = input('Ingrese su opción:\n')
        if opcion == '1':
            pass
        
        elif opcion == '4':
            exportar_departamentos()
            
        elif opcion == '0':
            break
        
        else:
            print('Debe seleccionar una opción válida')
        
        input('Presione enter para continuar...')

def menu_usuarios(): # Función para el menú de usuarios
    pass

def menu_empleados(): # Función para el menú de empleados
    while True:
        # Limpiar pantalla
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== Menú de Empleados ====')
        print('4. Crear registro de tiempo de trabajo')
        print('5. Generar informe de empleados en pdf')
        print('6. Generar informe de registro tiempo en pdf')
        print('0. Atrás')
        opcion = input('Ingrese su opción:\n')
        if opcion == '1':
            pass
        
        elif opcion == '4':
            crear_registro_tiempo()
        
        elif opcion == '5':
            exportar_empleados()
            
        elif opcion == '6':
            exportar_registro_tiempo()
            
        elif opcion == '0':
            break
        
        else:
            print('Debe seleccionar una opción válida')
            
        input('Presione enter para continuar...')
        
def iniciar_sesion(): # Función para iniciar sesión
    usuario = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
    # Instanciando objeto tipo usuario
    user = Usuario(usuario=usuario, password=password)
    # Instanciamos objeto dao para usuario
    dao = UsuarioDAO(user)
    if dao.iniciar_sesion():
        menu_principal(user)
    else:
        print('Error en datos, intente nuevamente.')

def menu_inicio_sesion(): # Menú para iniciar sesión
    while True:
        os.system('clear' if os.name != "nt" else 'cls') # Limpiar la pantalla
        print('=== Menu Principal ===') # Menu principal
        print('1. Iniciar Sesión')
        print('0. Salir')

        option = input('Seleccione una opción: ')
        
        if option == '1':
            iniciar_sesion()
        elif option == '0':
            os.system('clear' if os.name != "nt" else 'cls')
            print('Saliendo del programa hasta luego...')
            break
            
def menu_principal(user: Usuario): # Menú principal de la aplicación
    while True:
        # Limpiar pantalla
        os.system('clear' if os.name != "nt" else 'cls')
        # Cargamos opciones
        print('==== Menú principal ====')
        print(f'Bienvenido: {user.nombre} {user.apellido}')
        print('1. Menú de usuarios')
        print('2. Menú de empleados')
        print('3. Menú de roles')
        print('4. Menú de departamentos')
        print('5. Menú de proyectos')
        print('0. Cerrar sesión')
        opcion = input('Ingrese su opción:\n')
        
        if opcion == '1':
            menu_usuarios()
        
        elif opcion == '2':
            menu_empleados()
        
        elif opcion == '3':
            pass
        
        elif opcion == '4':
            menu_departamentos()
            
        elif opcion == '5':
            menu_proyectos()
            
        elif opcion == '0':
            print(f'Hasta luego {user.nombre} {user.apellido}')
            user = None
            break
        
        input('Presione enter para continuar...')

menu_inicio_sesion()