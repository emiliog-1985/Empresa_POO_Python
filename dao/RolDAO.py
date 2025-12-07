from models.Conectar import Conectar

class RolDAO:
    def __init__(self):
        self.__conexion = Conectar()

    def mostrar_roles(self):
        sql = 'SELECT rol_id, nombre, descripcion FROM rol'
        return self.__conexion.listar(sql)

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()