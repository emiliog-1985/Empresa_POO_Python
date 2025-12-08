from models.Conectar import Conectar

class EmpleadoDAO:
    def __init__(self):
        self.__conexion = Conectar()
    
    def crear_empleado(self, usuario_id, departamento_id, rol_id, codigo_empleado,nombre, apellido, direccion, telefono,email):
        sql = """
        INSERT INTO empleado (usuario_id, departamento_id, rol_id, codigo_empleado, nombre, apellido, direccion, telefono, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos = (usuario_id, departamento_id, rol_id, codigo_empleado,nombre, apellido, direccion, telefono,email)
        self.__conexion.ejecutar(sql, datos)    

    def actualizar_empleado(self, empleado_id, nombre, apellido, direccion, telefono, email):
        sql = "UPDATE empleado SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s WHERE empleado_id = %s"
        self.__conexion.ejecutar(sql, (nombre, apellido, direccion, telefono, email, empleado_id))
    
    def obtener_rol_id_por_usuario(self, nombre_usuario):
        sql = """
            SELECT r.rol_id
            FROM empleado e
            JOIN usuario u ON e.usuario_id = u.usuario_id
            JOIN rol r ON e.rol_id = r.rol_id
            WHERE u.nombre_usuario = %s
        """
        datos = self.__conexion.listar_uno(sql, (nombre_usuario,))
        if datos and 'rol_id' in datos:
            return datos['rol_id']
        return None
    
    def listar_empleados(self):
        sql = """
        SELECT e.empleado_id, u.nombre_usuario, d.nombre AS departamento, d.ubicacion, r.nombre AS rol, r.descripcion
        FROM empleado e
        JOIN usuario u ON e.usuario_id = u.usuario_id
        JOIN departamento d ON e.departamento_id = d.departamento_id
        JOIN rol r ON e.rol_id = r.rol_id
        """
        return self.__conexion.listar(sql)

    def obtener_nombre_empleado_por_usuario(self, nombre_usuario):
        sql = """
            SELECT e.nombre
            FROM empleado e
            JOIN usuario u ON e.usuario_id = u.usuario_id
            WHERE u.nombre_usuario = %s
        """
        datos = self.__conexion.listar_uno(sql, (nombre_usuario,))
        if datos and 'nombre' in datos:
            return datos['nombre']
        return None

    def mostrar_empleados(self):
        sql = 'SELECT empleado_id, nombre, apellido, direccion, telefono, email FROM empleado'
        return self.__conexion.listar(sql)


    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()