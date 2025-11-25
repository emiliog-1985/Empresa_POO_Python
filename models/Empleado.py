class Empleado:
    def __init__(self, nombre:str = None, 
                 apellido:str = None,
                 direccion:str = None,
                 telefono:str = None,
                 email:str = None, 
                 empleado_id:int = None, 
                 usuario_id:int = None, 
                 departamento_id:int = None, 
                 rol_id:int = None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__empleado_id = empleado_id
        self.__usuario_id = usuario_id
        self.__departamento_id = departamento_id
        self.__rol_id = rol_id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def email(self):
        return self.__email
    
    @property
    def empleado_id(self):
        return self.__empleado_id
        
    @property
    def usuario_id(self):
        return self.__usuario_id
    
    @property
    def departamento_id(self):
        return self.__departamento_id
    
    @property
    def rol_id(self):
        return self.__rol_id    
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value
        
    @direccion.setter
    def direccion(self, value):
        self.__direccion = value
        
    @telefono.setter
    def telefono(self, value):
        self.__telefono = value
        
    @email.setter
    def email(self, value):
        self.__email = value

    @empleado_id.setter
    def empleado_id(self, value):
        self.__empleado_id = value
        
    @usuario_id.setter
    def usuario_id(self, value):
        self.__usuario_id = value
        
    @departamento_id.setter
    def departamento_id(self, value):
        self.__departamento_id = value
        
    @rol_id.setter
    def rol_id(self, value):
        self.__rol_id = value
        
