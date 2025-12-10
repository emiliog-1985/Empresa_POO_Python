from models.Conectar import Conectar
from models.Departamento import Departamento

class DepartamentoDAO:
    def __init__(self, departamento:Departamento):
        self.__conexion = Conectar()
        self.__departamento = departamento
        
    def asignar_departamento_a_usuario(self, usuario_id, departamento_id):
        sql = "UPDATE usuario SET departamento_id = %s WHERE usuario_id = %s"
        self.__conexion.ejecutar(sql, (departamento_id, usuario_id))
        
    def mostrar_departamentos(self):
        sql = 'SELECT departamento_id, nombre, ubicacion FROM departamento'
        return self.__conexion.listar(sql)

    def crear_departamento(self):
        sql = 'INSERT INTO departamento (nombre, ubicacion) VALUES (%s, %s)'
        datos = (self.__departamento.nombre, self.__departamento.ubicacion)
        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró crear departamento.')
        print('Se creó departamento')
    
    def editar_departamento(self):
        sql = 'UPDATE departamento SET nombre = %s, ubicacion = %s WHERE departamento_id = %s'
        datos = (self.__departamento.nombre,
                 self.__departamento.ubicacion,
                 self.__departamento.departamento_id)

        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró editar el departamento.')
        print('Se editó departamento correctamente')

    
    def buscar_departamento(self):

        sql = 'SELECT * FROM departamento WHERE departamento_id = %s'
        datos = (self.__departamento.departamento_id,)
        lista = self.__conexion.listar_uno(sql,datos)
        
        print(f'ID: {lista["departamento_id"]}')
        print(f'Nombre departamento: {lista["nombre"]}')
        print(f'Ubicacion: {lista["ubicacion"]}')

    
    def eliminar_departamento(self):
        sql = 'DELETE FROM departamento WHERE departamento_id = %s'
        datos = (self.__departamento.departamento_id,)
        
        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró eliminar el departamento.')
        print('Se eliminó departamento correctamente')
    
    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()
