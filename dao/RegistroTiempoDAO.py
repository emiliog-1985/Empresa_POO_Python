from models.RegistroTiempo import RegistroTiempo
from models.Conectar import Conectar

class RegistroTiempoDAO:
    def __init__(self, registro_tiempo:RegistroTiempo):
        self.__conexion = Conectar()
        self.__registro_tiempo = registro_tiempo
        
    def crear_registro_tiempo(self):
        sql = '''
        INSERT INTO registrotiempo (empleado_id, proyecto_id, fecha, horas_trabajo, descripcion)
        VALUES (%s, %s, %s, %s, %s)'''
        datos = (self.__registro_tiempo.empleado_id, 
                 self.__registro_tiempo.proyecto_id, 
                 self.__registro_tiempo.fecha,
                 self.__registro_tiempo.horas_trabajo,
                 self.__registro_tiempo.descripcion)
        if not self.__conexion.ejecutar(sql, datos):
            raise RuntimeError('No se logró crear registro tiempo.')
        print('Se creó registro tiempo')
        
    def mostrar_registros(self):
        sql = '''
        SELECT r.registro_id, p.nombre_proyecto, e.nombre, e.apellido, r.fecha, r.horas_trabajo, r.descripcion
        FROM registrotiempo r 
        JOIN empleado e ON r.empleado_id = e.empleado_id
        JOIN proyecto p ON r.proyecto_id = p.proyecto_id'''
        return self.__conexion.listar(sql)
        
    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()
