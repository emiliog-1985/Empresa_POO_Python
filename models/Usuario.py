from models.Empleado import Empleado
from models.conectar import Conectar    

class Usuario(Empleado):
    def __init__(self,
                 usuario = None, 
                 apellido = None, 
                 direccion = None, 
                 telefono = None, 
                 email = None, 
                 empleado_id = None, 
                 usuario_id = None, 
                 departamento_id = None, 
                 rol_id = None,
                 password:str = None):
        super().__init__(usuario, apellido, direccion, telefono, email, empleado_id, usuario_id, departamento_id, rol_id)
        self.__nombre_usuario = usuario
        self.__hash_password = password
        
    @property
    def usuario(self):
        return self.__nombre_usuario
    
    @property
    def password(self):
        return self.__hash_password