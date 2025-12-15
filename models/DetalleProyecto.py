class DetalleProyecto:
    def __init__(self, detalle_proyecto_id:int = None,
                 empleado_id:int = None,
                 proyecto_id:int = None,
                 fecha_asignacion:str = None,
                 rol_en_proyecto:str = None,
                 horas_asignadas:int = None):
        self.__detalle_proyecto_id = detalle_proyecto_id
        self.__empleado_id = empleado_id
        self.__proyecto_id = proyecto_id
        self.__fecha_asignacion = fecha_asignacion
        self.__rol_en_proyecto = rol_en_proyecto
        self.__horas_asignadas = horas_asignadas
        
    @property
    def detalle_proyecto_id(self):
        return self.__detalle_proyecto_id
    @property
    def empleado_id(self):
        return self.__empleado_id
    @property
    def proyecto_id(self):
        return self.__proyecto_id
    @property
    def fecha_asignacion(self):
        return self.__fecha_asignacion
    @property
    def rol_en_proyecto(self):
        return self.__rol_en_proyecto
    @property
    def horas_asignadas(self):
        return self.__horas_asignadas
    
