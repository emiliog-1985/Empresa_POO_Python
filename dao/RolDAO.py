from models.Conectar import Conectar

class RolDAO:
    def __init__(self):
        self.__conexion = Conectar()

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


    def mostrar_roles(self):
        sql = 'SELECT rol_id, nombre, descripcion FROM rol'
        return self.__conexion.listar(sql)

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()