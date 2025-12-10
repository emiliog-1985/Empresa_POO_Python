import os
import mysql.connector
import getpass
import datetime
from datetime import date
from utils.generar_pdf import generar_pdf
from models.UsuarioEmpleado import Usuario
from dao.UsuarioDAO import UsuarioDAO
from models.RegistroTiempo import RegistroTiempo
from dao.RegistroTiempoDAO import RegistroTiempoDAO
from models.Proyecto import Proyecto
from dao.ProyectoDAO import ProyectoDAO
from models.DetalleProyecto import DetalleProyecto
from dao.DetalleProyectoDAO import DetalleProyectoDAO
from models.Departamento import Departamento
from dao.DepartamentoDAO import DepartamentoDAO
from dao.RolDAO import RolDAO
from dao.EmpleadoDAO import EmpleadoDAO



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
    user = Usuario
    dao = UsuarioDAO(user)
    lista = dao.mostrar_usuarios_pdf()
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
            
def crear_registro_tiempo(): # Función para crear un registro de tiempo
    print('==== Crear Registro Tiempo ====')
    try:
        proyecto_id = int(input('Ingrese el id de proyecto: \n'))
        empleado_id = int(input('Ingrese el id de empleado:\n'))
        horas_trabajo = float(input('Ingrese horas trabajadas: \n'))
        
    except ValueError:
        print('Debe ingresar los datos como números')
    
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

def crear_departamento():
    os.system('clear' if os.name != "nt" else 'cls')
    print("=== Crear nuevo Departamento ===\n")

    try:
        nombre = input("Nombre del departamento: ").strip()
        if not nombre:
            print("El nombre es obligatorio")
            input('Presione enter para continuar...')
            return

        ubicacion = input("Ubicación: ").strip()
        if not ubicacion:
            print("La ubicación es obligatoria")
            input('Presione enter para continuar...')
            return

        departamento = Departamento(nombre=nombre, ubicacion=ubicacion)
        dao = DepartamentoDAO(departamento)
        dao.crear_departamento()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        input('Presione enter para continuar...')

def editar_departamento(): # Función para actualizar un proyecto
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Editar departamento ====')
    try:
        departamento_id = int(input('Ingrese el id del departamento: \n'))
    except ValueError:
        print('El ID del departamento debe ser un número entero')
        return
    nombre = input('Ingrese el nuevo nombre del departamento3: \n')
    ubicacion = input('Ingrese la nueva ubicacion del departamento: \n')

     # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        departamento = Departamento(departamento_id = departamento_id,
                                    
            nombre = nombre, 
            ubicacion = ubicacion)
        
    except ValueError as e:
        # Aquí llegan las validaciones de proyecto (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del proyecto: {e}")
        return

    dao = None
    try:
        dao = DepartamentoDAO(departamento)
        dao.editar_departamento()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al actualizar departamento: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al actualizar departamento: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()

def buscar_departamento():
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Buscar departamento ====')

    try:
        departamento_id = int(input('Ingrese el id del departamento: \n'))
    except ValueError as e:
        print ("Solo se puede ingresar numeros...")
        return
    departamento = Departamento(departamento_id=departamento_id)
    dao = DepartamentoDAO(departamento)
    dao.buscar_departamento()
    if dao is not None:
        dao.cerrar_dao()

def eliminar_departamento():
    os.system('clear' if os.name != "nt" else 'cls')
    print("=== Eliminar Departamento ===\n")

    try:
        departamento_id = input("Ingrese ID del departamento: ").strip()

        if not departamento_id:
            print("Debe ingresar un ID")
            input("Enter para continuar...")
            return

        departamento_id = int(departamento_id)

        temp = Departamento(departamento_id=departamento_id)
        dao = DepartamentoDAO(temp)

        try:
            dao.eliminar_departamento()
            print("Departamento eliminado correctamente")

        except RuntimeError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        input("Presione enter para continuar...")

def mantener_departamentos():
    #funcion para agregar y asignar departamentos a usuarios
    print('==== Mantenedor de departamentos ====')
    print('1. Registrar nuevo departamento')
    print('2. Actualizar departamento existente')
    print('3. Buscar departamento')
    print('4. Mostrar departamentos disponibles')
    print('5. Eliminar departamento')
    print('0. Salir')
    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        crear_departamento()
        
    elif opcion == '2':
        editar_departamento()
    
    elif opcion == '3':
        buscar_departamento()
        
    elif opcion == '4':
        print('Listado de departamentos disponibles:')
        departamento = Departamento
        dao = DepartamentoDAO(departamento)
        departamentos = dao.mostrar_departamentos()
        for dept in departamentos:
            print(f"departamento_id: {dept['departamento_id']}, Nombre: {dept['nombre']}, Ubicacion: {dept['ubicacion']}")
            dao.cerrar_dao()
            
    elif opcion == '5':
        eliminar_departamento()
    
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
    os.system('clear' if os.name != "nt" else 'cls')
    print('==== Mantenedor de usuario ====')
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
        if nombre_usuario.strip() == "" or nombre_usuario is None or nombre_usuario.isspace() or len(nombre_usuario) <3 or not nombre_usuario.isalnum() or nombre_usuario.isdigit() or len(nombre_usuario) >10:
            print('❌ No cumple con los requisitos minimos para el usuario. Intente nuevamente.')
            return
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
            print(f"usuario_id: {user['usuario_id']} ❯❯❯❯ Nombre de Usuario: {user['nombre_usuario']} ❯❯❯❯ Ultimo acceso: {user['fecha_ultimo_acceso']}")
        dao.cerrar_dao()
        input("Presione Enter para volver al mantenedor de usuarios 👤 ")
        mantener_usuario()

    elif opcion == '4':
        dao = UsuarioDAO()
        nombre_usuario = input('Ingrese el Nombre de Usuario a eliminar: ')
        if nombre_usuario.strip() == "" or nombre_usuario is None or nombre_usuario.isspace() or len(nombre_usuario) <3 or not nombre_usuario.isalnum() or nombre_usuario.isdigit() or len(nombre_usuario) >10:
            print('❌ No cumple con los requisitos minimos para el usuario. Intente nuevamente.')
            return
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

def menu_exportar():
    while True:
        os.system('clear' if os.name != "nt" else 'cls')
        print('==== Menú Exportar ====')
        print('1. Exportar Empleados a pdf')
        print('2. Exportar Proyectos a pdf')
        print('3. Exportar Departamentos a pdf')
        print('4. Exportar Registros de Tiempo a pdf')
        print('0. Atrás')
        opcion = input('Ingrese su opción:\n')
        if opcion == '1':
            exportar_empleados()
        elif opcion == '2':
            exportar_proyectos()
        elif opcion == '3':
            exportar_departamentos()
        elif opcion == '4':
            exportar_registro_tiempo()
        elif opcion == '0':
            break
        else:
            print('Debe ingresar una opción válida')
            
        input('Presione enter para continuar...')

def iniciar_sesion():
    while True:
        #funcion para iniciar sesion
        os.system('clear' if os.name != "nt" else 'cls')
        print('==== 👤 Datos de usuario ====')
        usuario = input(str('🔠 Ingrese su usuario caracteres en minusculas :')).strip().lower()
        if usuario == '' or usuario is None or usuario == ' ' or usuario.isspace() or len(usuario) < 3 or not usuario.isalnum() or usuario.isdigit() or len(usuario) > 10:
        # Verificar si el usuario está vacío, contiene solo espacios, o es None, verificar longitud mínima y máxima, si es alfanumérico y no solo numérico
            print('😕 ingreso un usuario invalido no cumple con los requisitos, intente nuevamente.')
            input("⌨️ Presione Enter para intentar de nuevo...")
            iniciar_sesion()


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
            print('6. Crear registro tiempo ➜')
            print('7. Exportar a PDF📄 ➜')
            print('0. Cerrar sesion 🚪➜')
            print ('========================================')
        elif usuario.rol_id == 3 or usuario.rol_id == 2 or usuario.rol_id == 1:
            print('========================================')
            print('6. Crear registro tiempo ➜')   
            print('7. Exportar a PDF📄 ➜')
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
            menu_proyectos()    

        elif opcion == '6':
            crear_registro_tiempo()

        elif opcion == '7' and (usuario.rol_id == 3 or usuario.rol_id == 2 or usuario.rol_id == 1):
            menu_exportar()
        
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
