import mysql.connector
from models.Conectar import Conectar
from models.UsuarioEmpleado import Usuario

class UsuarioDAO:
    def __init__(self, usuario: Usuario = None):
        self.__conexion = Conectar()
        self.__usuario = usuario

    def crear_rol(self, nombre, descripcion):       
        sql = """
        INSERT INTO rol (nombre, descripcion)
        VALUES (%s, %s)
        """
        datos = (nombre, descripcion)
        self.__conexion.ejecutar(sql, datos)

    def actualizar_rol(self, rol_id, nombre, descripcion):
        sql = "UPDATE rol SET nombre = %s, descripcion = %s WHERE rol_id = %s"
        self.__conexion.ejecutar(sql, (nombre, descripcion, rol_id))    


    def asignar_rol_a_usuario(self, usuario_id, rol_id):
        sql = "UPDATE usuario SET rol_id = %s WHERE usuario_id = %s"
        self.__conexion.ejecutar(sql, (rol_id, usuario_id)) 

    def asignar_departamento_a_usuario(self, usuario_id, departamento_id):
        sql = "UPDATE usuario SET departamento_id = %s WHERE usuario_id = %s"
        self.__conexion.ejecutar(sql, (departamento_id, usuario_id))
    
    def crear_departamento(self, nombre, ubicacion):
        sql = """
        INSERT INTO departamento (nombre, ubicacion)
        VALUES (%s, %s)
        """
        datos = (nombre, ubicacion)
        self.__conexion.ejecutar(sql, datos)

    def actualizar_departamento(self, departamento_id, nombre, ubicacion):
        sql = "UPDATE departamento SET nombre= %s, ubicacion = %s WHERE departamento_id = %s"
        self.__conexion.ejecutar(sql, (nombre, ubicacion, departamento_id))
    

    def existe_usuario(self, nombre_usuario):
        sql = 'SELECT nombre_usuario FROM usuario WHERE nombre_usuario = %s'
        datos = self.__conexion.listar_uno(sql, (nombre_usuario,))
        if datos and 'nombre_usuario' in datos:
            return True
        return False

    def mostrar_usuarios(self):
        sql = 'SELECT usuario_id, nombre_usuario FROM usuario'
        return self.__conexion.listar(sql)
    
    def mostrar_departamentos(self):
        sql = 'SELECT departamento_id, nombre_departamento FROM departamento'
        return self.__conexion.listar(sql)
    
    def mostrar_roles(self):
        sql = 'SELECT rol_id, nombre FROM rol'
        return self.__conexion.listar(sql)

    def actualizar_fecha_ultimo_acceso(self, nombre_usuario, fecha_actual):
        sql = "UPDATE usuario SET fecha_ultimo_acceso = %s WHERE nombre_usuario = %s"
        self.__conexion.ejecutar(sql, (fecha_actual, nombre_usuario))

    def iniciar_sesion(self):
        sql_salt = 'SELECT hash_password, salt FROM usuario WHERE nombre_usuario = %s'
        datos = self.__conexion.listar_uno(sql_salt, (self.__usuario.usuario,))
        #print(datos)
        if not self.__usuario.verify_password(self.__usuario.password, datos['hash_password'], datos['salt']):
            print('⚠️ Credenciales no válidas')
            return
        print('👌 Se logró iniciar sesión')
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

    def crear_usuario(self, nombre_usuario, password): # crear usuario
        usuario_temp = Usuario(nombre_usuario=nombre_usuario, hash_password=password)
        password_hash, salt = usuario_temp.hash_password(password)
    
        sql = """
        INSERT INTO usuario (nombre_usuario, hash_password, salt)
        VALUES (%s, %s, %s)
        """
        datos = (nombre_usuario, password_hash, salt)
        self.__conexion.ejecutar(sql, datos)

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()

    def mostrar_trabajadores(self):
        sql = '''
        SELECT p.rut, t.usuario, t.sueldo, p.nombre 
        FROM trabajador t JOIN persona p
        ON t.rut = p.rut'''
        return self.__conexion.listar(sql)

