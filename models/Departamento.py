class Departamento:
    def __init__(self, departameto_id:int = None, nombre:str = None, ubicacion:str = None):
        self.__departamento_id =  departameto_id
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        
    @property
    def deparamento_id(self):
        return self.__departamento_id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def ubicacion(self):
        return self.__ubicacion