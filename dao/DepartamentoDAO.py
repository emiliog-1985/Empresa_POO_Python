from models.Conectar import Conectar

class DepartamentoDAO:
    def __init__(self):
        self.__conexion = Conectar()

    def mostrar_departamentos(self):
        sql = 'SELECT departamento_id, nombre, ubicacion FROM departamento'
        return self.__conexion.listar(sql)

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()