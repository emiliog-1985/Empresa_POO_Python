from models.Proyecto import Proyecto
from models.conectar import Conectar

class ProyectoDAO:
    def __init__(self, proyecto:Proyecto):
        self.__conexion = Conectar()
        self.__proyecto = proyecto
        
    def listar_proyectos(self):
        sql = 'SELECT * FROM proyecto'
        lista = self.__conexion.listar(sql)
        for proyecto in lista:
            print(f'ID Proyecto: {proyecto["proyecto_id"]}')
            print(f'Nombre Proyecto: {proyecto["nombre_proyecto"]}')
            print(f'Fecha inicio: {proyecto["fecha_inicio"]}')
            print(f'Fecha término: {proyecto["fecha_termino"]}')
            print(f'Descripción: {proyecto["descripcion"]}')
            print(f'Estado: {proyecto["estado"]}')
            print('-'*60)
    
    def crear_proyecto(self):
        sql = '''INSERT INTO proyecto (nombre_proyecto, fecha_inicio, fecha_termino, descripcion, estado)
        VALUES (%s, %s, %s, %s, %s)'''
        datos = (self.__proyecto.nombre_proyecto, 
                 self.__proyecto.fecha_inicio,
                 self.__proyecto.fecha_termino,
                 self.__proyecto.descripcion,
                 self.__proyecto.estado)
        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró crear proyecto.')
        print('Se creó proyecto')
    
    def actualizar_proyecto(self):
        sql = '''UPDATE proyecto 
        SET nombre_proyecto = %s, fecha_inicio = %s, fecha_termino = %s, descripcion = %s, estado = %s
        WHERE proyecto_id = %s'''
        datos = (self.__proyecto.nombre_proyecto,
                 self.__proyecto.fecha_inicio,
                 self.__proyecto.fecha_termino,
                 self.__proyecto.descripcion,
                 self.__proyecto.estado,
                 self.__proyecto.proyecto_id)
        if self.__conexion.ejecutar(sql, datos):
            print('Se actualizó la tabla proyecto')
        else:
            print('No se logró actualizar tabla proyecto')
    
    def eliminar_proyecto(self):
        sql = 'DELETE FROM proyecto WHERE proyecto_id = %s'
        dato = (self.__proyecto.proyecto_id,)
        if self.__conexion.ejecutar(sql, dato):
            print('Proyecto eliminado')
        else:
            print('Proyecto no se logró eliminar')
    
    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()