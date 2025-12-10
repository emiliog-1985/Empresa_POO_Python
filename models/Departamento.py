class Departamento:
    def __init__(self, departamento_id:int = None, nombre:str = None, ubicacion:str = None):
        self.__departamento_id =  departamento_id
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        
    @property
    def departamento_id(self):
        return self.__departamento_id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def ubicacion(self):
        return self.__ubicacion