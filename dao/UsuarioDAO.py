import mysql.connector
from models.Conectar import Conectar
from models.UsuarioEmpleado import Usuario

class UsuarioDAO:
    def __init__(self, usuario: Usuario = None):
        self.__conexion = Conectar()
        self.__usuario = usuario


    def eliminar_usuario(self, nombre_usuario):
    # eliminar usuario
        sql = "DELETE FROM usuario WHERE nombre_usuario = %s"
        self.__conexion.ejecutar(sql, (nombre_usuario,))

    def crear_usuario(self, nombre_usuario, password): # crear usuario
        usuario_temp = Usuario(usuario_id=nombre_usuario, hash_password=password)
        password_hash, salt = usuario_temp.hash_password(password)
    
        sql = """
        INSERT INTO usuario (nombre_usuario, hash_password, salt)
        VALUES (%s, %s, %s)
        """
        datos = (nombre_usuario, password_hash, salt)
        self.__conexion.ejecutar(sql, datos)

    def actualizar_usuario(self, nombre_usuario, password): # actualizar usuario
        usuario_temp = Usuario(usuario_id=nombre_usuario, hash_password=password)
        password_hash, salt = usuario_temp.hash_password(password)
    
        sql = "UPDATE usuario SET hash_password = %s, salt = %s WHERE nombre_usuario = %s"
        self.__conexion.ejecutar(sql, (password_hash, salt, nombre_usuario))


    def existe_usuario(self, nombre_usuario):
        sql = 'SELECT nombre_usuario FROM usuario WHERE nombre_usuario = %s'
        datos = self.__conexion.listar_uno(sql, (nombre_usuario,))
        if datos and 'nombre_usuario' in datos:
            return True
        return False
    
    def mostrar_usuarios_pdf(self):
        sql = '''
        SELECT u.nombre_usuario, e.nombre, e.apellido, e.direccion, e.telefono, e.email 
        FROM usuario u JOIN empleado e 
        ON u.usuario_id = e.usuario_id'''
        return self.__conexion.listar(sql)


    def mostrar_usuarios(self):
        sql = 'SELECT usuario_id, nombre_usuario, fecha_ultimo_acceso FROM usuario'
        return self.__conexion.listar(sql)
    
    def mostrar_departamentos(self):
        sql = 'SELECT departamento_id, nombre_departamento FROM departamento'
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

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()
