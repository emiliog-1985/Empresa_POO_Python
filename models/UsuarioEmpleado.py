from models.Conectar import Conectar
import hashlib
import os

class Empleado:
    def __init__(self, rut=None, nombre=None, direccion=None, usuario: str = None, password: str = None, sueldo: int = None, id: int = None, salt: str = None):
        self.__rut = rut
        self.__nombre = nombre
        self.__direccion = direccion
        self.__usuario = self.validar_usuario(usuario)
        self.__password = password
        self.__salt = salt
        self.__sueldo = sueldo
        self.__id = id

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, value):
        self.__rut = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        self.__usuario = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, value):
        self.__sueldo = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def salt(self):
        return self.__salt

    @salt.setter
    def salt(self, value):
        self.__salt = value

    def validar_usuario(self, usuario: str):
        if usuario is None:
            return
        if usuario.strip() == "":
            raise ValueError('Nombre de usuario no debe ser vacio')
        elif len(usuario) > 20:
            raise ValueError('Nombre de usuario no puede ser mayor a 20 caracteres')
        return usuario

    def hash_password(self, password, salt=None): 
        if salt is None:
            salt = os.urandom(16)  # Genera una sal aleatoria de 16 bytes
        else:
            salt = salt.encode('utf-8')
        password_hash = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        return password_hash, salt.hex() # Convertir la sal a hexadecimal para almacenarla como cadena 

    def verify_password(self, password, stored_password_hash, salt):
        new_password_hash = hashlib.sha256(bytes.fromhex(salt) + password.encode('utf-8')).hexdigest()
        #print(f"Hash generado:   {new_password_hash}")     
        #print(f"Hash almacenado: {stored_password_hash}")
        return new_password_hash == stored_password_hash

class Usuario(Empleado):
    def __init__(self,
                 usuario_id=None,
                 departamento_id=None,
                 rol_id=None,
                 codigo_empleado=None,
                 nombre=None,
                 apellido=None,
                 direccion=None,
                 telefono=None,
                 email=None,
                 empleado_id=None,
                 hash_password: str = None):
        super().__init__(rut=departamento_id, nombre=nombre, direccion=direccion, usuario=usuario_id, password=hash_password, sueldo=None, id=empleado_id, salt=None)
        self.__nombre_usuario = usuario_id
        self.__hash_password = hash_password

    @property
    def usuario(self):
        return self.__nombre_usuario

    @property
    def password(self):
        return self.__hash_password

