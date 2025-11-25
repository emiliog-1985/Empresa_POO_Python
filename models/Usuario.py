from models.Empleado import Empleado

class Usuario(Empleado):
    def __init__(self, nombre = None, apellido = None, usuario:str = None, password:str = None):
        super().__init__(nombre, apellido)
        self.__usuario = usuario
        self.__password = password
        
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def password(self):
        return self.__password
