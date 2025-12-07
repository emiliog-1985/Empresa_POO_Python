import mysql.connector
from models.Conectar import Conectar
from models.UsuarioEmpleado import Usuario

class UsuarioDAO:

    def mostrar_usuarios(self):
        sql = 'SELECT usuario_id, nombre_usuario FROM usuario'
        return self.__conexion.listar(sql)
    
    def mostrar_departamentos(self):
        sql = 'SELECT departamento_id, nombre_departamento FROM departamento'
        return self.__conexion.listar(sql)
    
    def mostrar_roles(self):
        sql = 'SELECT rol_id, nombre_rol FROM rol'
        return self.__conexion.listar(sql)

    def __init__(self, usuario: Usuario):
        # Si Conexion() falla, lanzará la excepción y la capa superior la atrapará
        self.__conexion = Conectar()
        self.__usuario = usuario

    def actualizar_fecha_ultimo_acceso(self, nombre_usuario, fecha_actual):
        sql = "UPDATE usuario SET fecha_ultimo_acceso = %s WHERE nombre_usuario = %s"
        self.__conexion.ejecutar(sql, (fecha_actual, nombre_usuario))

    def iniciar_sesion(self):
        sql_salt = 'SELECT hash_password, salt FROM usuario WHERE nombre_usuario = %s'
        datos = self.__conexion.listar_uno(sql_salt, (self.__usuario.usuario,))
        #print(datos)
        if not self.__usuario.verify_password(self.__usuario.password, datos['hash_password'], datos['salt']):
            print('Credenciales no validas')
            return
        print('Se logro iniciar sesion')
        # Aquí deberías ajustar la consulta para obtener los datos del usuario según tu modelo
        sql = '''
        SELECT usuario_id, nombre_usuario
        FROM usuario
        WHERE nombre_usuario = %s
        '''
        datos = self.__conexion.listar_uno(sql, (self.__usuario.usuario, ))
        #print(datos)
        if not datos:
            return False

        # Solo asignar los datos que existen en la consulta
        self.__usuario.usuario_id = datos.get('usuario_id')
        self.__usuario.nombre_usuario = datos.get('nombre_usuario')
        return True

    def crear_trabajador(self):
        # igual podrías dejar esta lógica como la tienes o adaptarla
        sql_persona = 'INSERT INTO persona(rut, nombre, direccion) VALUES (%s, %s, %s)'
        sql_trabajador = '''
            INSERT INTO trabajador(rut, usuario, id, password, sueldo, salt) 
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        datos_persona = (
            self.__trabajador.rut,
            self.__trabajador.nombre,
            self.__trabajador.direccion
        )
        if not self.__conexion.ejecutar(sql_persona, datos_persona):
            raise RuntimeError('No se logró crear persona (tabla persona).')

        password, salt = self.__trabajador.hash_password(self.__trabajador.password)
        print(password, salt)

        datos_trabajador = (
            self.__trabajador.rut,
            self.__trabajador.usuario,
            self.__trabajador.id,
            password,
            self.__trabajador.sueldo,
            salt
        )
        
        print(datos_trabajador)
        
        if not self.__conexion.ejecutar(sql_trabajador, datos_trabajador):
            raise RuntimeError('No se logró crear trabajador (tabla trabajador).')

        print('Se creó trabajador')

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()

    def mostrar_trabajadores(self):
        sql = '''
        SELECT p.rut, t.usuario, t.sueldo, p.nombre 
        FROM trabajador t JOIN persona p
        ON t.rut = p.rut'''
        return self.__conexion.listar(sql)

