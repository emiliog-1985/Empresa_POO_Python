from models.Empleado import Empleado

class Usuario(Empleado):
    def __init__(self, nombre = None, 
                 apellido = None, 
                 direccion = None, 
                 telefono = None, 
                 email = None, 
                 empleado_id = None, 
                 usuario_id = None, 
                 departamento_id = None, 
                 rol_id = None,
                 usuario:str = None,
                 password:str = None):
        super().__init__(nombre, apellido, direccion, telefono, email, empleado_id, usuario_id, departamento_id, rol_id)
        self.__usuario = usuario
        self.__password = password
        
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def password(self):
        return self.__password
