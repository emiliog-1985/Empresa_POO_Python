from models.Conectar import Conectar
from models.Departamento import Departamento

class DepartamentoDAO:
    def __init__(self, departamento:Departamento):
        self.__conexion = Conectar()
        self.__departamento = departamento
        

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
        

    def mostrar_departamentos(self):
        sql = 'SELECT departamento_id, nombre, ubicacion FROM departamento'
        return self.__conexion.listar(sql)

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()
