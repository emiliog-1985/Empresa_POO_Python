class UsuarioDAO:
    def __init__(self, usuario:Usuario):
        self.__conexion = conectar()
        self.__usuario = usuario
        
    def iniciar_sesion(self):
        sql = '''
        SELECT e.nombre, e.apellido 
        FROM usuario u JOIN empleado e 
        ON u.usuario_id = e.usuario_id;
        WHERE nombre_usuario = %s AND hash_password = %s'''
        datos = self.__conexion.listar_uno(sql, (self.__usuario.usuario, self.__usuario.password))
        if datos:
            self.__usuario.nombre = datos['nombre']
            self.__usuario.apellido = datos['apellido']
            return True
        return False
