class RegistroTiempo:
    def __init__(self, fecha:str = None, 
                 horas_trabajo:float = None, 
                 descripcion:str = None, 
                 registro_id:int = None, 
                 empleado_id:int = None,
                 proyecto_id:int = None):
        self.__fecha = fecha
        self.__horas_trabajo = horas_trabajo
        self.__descripcion = descripcion
        self.__registro_id = registro_id
        self.__empleado_id = empleado_id
        self.__proyecto_id = proyecto_id
        
    @property
    def fecha(self):
        return self.__fecha
    @property
    def horas_trabajo(self):
        return self.__horas_trabajo
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def registro_id(self):
        return self.__registro_id
    @property
    def empleado_id(self):
        return self.__empleado_id
    @property
    def proyecto_id(self):
        return self.__proyecto_id    
