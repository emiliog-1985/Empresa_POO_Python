class Empleado:
    def __init__(self, nombre:str = None, apellido:str = None):
        self.__nombre = nombre
        self.__apellido = apellido
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value
