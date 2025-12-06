from models.DetalleProyecto import DetalleProyecto
from models.conectar import Conectar

class DetalleProyectoDAO:
    def __init__(self, detalle_proyecto : DetalleProyecto):
        self.__conexion = Conectar()
        self.__detalle_proyecto = detalle_proyecto
        
    def asignar_proyecto(self):
        sql = '''INSERT INTO detalleproyecto (empleado_id, proyecto_id, fecha_asignacion, rol_en_proyecto, horas_asignadas)
        VALUES (%s, %s, %s, %s, %s)'''
        datos = (self.__detalle_proyecto.empleado_id, 
                 self.__detalle_proyecto.proyecto_id,
                 self.__detalle_proyecto.fecha_asignacion,
                 self.__detalle_proyecto.rol_en_proyecto,
                 self.__detalle_proyecto.horas_asignadas)
        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró asignar proyecto a empleado.')
        print('Se asignó proyecto a empleado')
    
    def desasignar_proyecto(self):
        sql = 'DELETE FROM detalleproyecto WHERE empleado_id = %s AND proyecto_id = %s'
        datos = (self.__detalle_proyecto.empleado_id, self.__detalle_proyecto.proyecto_id)
        if self.__conexion.ejecutar(sql, datos):
            print('Proyecto desasignado de empleado')
        else:
            print('Proyecto no se logró desasignar')
            
    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()