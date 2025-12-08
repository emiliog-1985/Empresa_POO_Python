from models.Conectar import Conectar
from models.Departamento import Departamento

class DepartamentoDAO:
    def __init__(self, departamento:Departamento):
        self.__conexion = Conectar()
        self.__departamento = departamento
        
    def crear_departamento(self):
        sql = 'INSERT INTO departamento (nombre, ubicacion) VALUES (%s, %s)'
        datos = (self.__departamento.nombre, self.__departamento.ubicacion)
        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró crear departamento.')
        print('Se creó departamento')
    
    def editar_departamento(self):
        pass
    
    def buscar_departamento(self):
        pass
    
    def eliminar_departamento(self):
        pass
    
    def mostrar_departamentos(self):
        sql = 'SELECT * FROM departamento'
        return self.__conexion.listar(sql)
        
    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()
