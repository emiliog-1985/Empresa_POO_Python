from models.Usuario import Usuario
from models.conectar import Conectar

class UsuarioDAO:
    def __init__(self, usuario:Usuario):
        self.__conexion = Conectar()
        self.__usuario = usuario
        
    def iniciar_sesion(self):
        sql = '''
        SELECT e.nombre, e.apellido, e.direccion, e.telefono, e.email, e.empleado_id, e.usuario_id, e.departamento_id, e.rol_id 
        FROM usuario u JOIN empleado e 
        ON u.usuario_id = e.usuario_id
        WHERE nombre_usuario = %s AND hash_password = %s;'''
        datos = self.__conexion.listar_uno(sql, (self.__usuario.usuario, self.__usuario.password))
        if datos:
            self.__usuario.nombre = datos['nombre']
            self.__usuario.apellido = datos['apellido']
            self.__usuario.direccion = datos['direccion']
            self.__usuario.telefono = datos['telefono']
            self.__usuario.email = datos['email']
            self.__usuario.empleado_id = datos['empleado_id']
            self.__usuario.usuario_id = datos['usuario_id']
            self.__usuario.departamento_id = datos['departamento_id']
            self.__usuario.rol_id = datos['rol_id']
            return True
        return False
    
    def registrar_usuario(self):
        sql = '''
        INSERT INTO usuario (nombre_usuario, hash_password)
        VALUES (%s, %s);
        '''
        valores = (self.__usuario.usuario, self.__usuario.password)
        resultado = self.__conexion.ejecutar(sql, valores)
        return resultado > 0
        return False 

