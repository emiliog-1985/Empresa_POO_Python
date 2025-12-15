class Proyecto:
    def __init__(self, proyecto_id:int = None, 
                 nombre_proyecto:str = None, 
                 fecha_inicio:str = None, 
                 fecha_termino:str = None, 
                 descripcion:str = None,
                 estado:str = None):
        self.__proyecto_id = proyecto_id
        self.__nombre_proyecto = nombre_proyecto
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__descripcion = descripcion
        self.__estado = estado
        
    @property
    def proyecto_id(self):
        return self.__proyecto_id
    @property
    def nombre_proyecto(self):
        return self.__nombre_proyecto
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def estado(self):
        return self.__estado
    
    @nombre_proyecto.setter
    def nombre_proyecto(self, value):
        self.__nombre_proyecto = value
    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value
    @fecha_termino.setter
    def fecha_termino(self, value):
        self.__fecha_termino = value
    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value
    @estado.setter
    def estado(self, value):
        self.__estado = value    
