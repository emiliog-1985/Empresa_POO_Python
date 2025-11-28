import mysql.connector # Importa el conector de MySQL (API de Python)

# Clase para la conexion a la base de datos para ejecutar consultas
class Conectar:
    def __init__(self):
        self.__conn = mysql.connector.connect(
            host='localhost',
            user='sistemas',
            password='sisT2025',
            database='empresa'
        )
# Metodo para consultar las tablas de la base de datos y probar la conexion a. Consultar
    def probar_conexion(self):
        cursor = self.__conn.cursor()
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(table)
        cursor.close()
        self.__conn.close() 
        print("Conexion cerrada")
# Metodo para ejecutar consultas SQL (INSERT, UPDATE, DELETE)
    def ejecutar(self, sql:str, datos=None):
        cursor = self.__conn.cursor() # Crea objeto tipo cursor
        cursor.execute(sql, datos)
        self.__conn.commit() # confirma cambios
        if cursor.rowcount > 0:
            return True
        return False
# Metodo para listar resultados de consultas SQL (SELECT)
    def listar(self, sql:str):
        cursor = self.__conn.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()
# Metodo para listar un solo resultado de consultas SQL (SELECT)    
    def listar_uno(self, sql:str, datos=None):
        cursor = self.__conn.cursor(dictionary=True)
        cursor.execute(sql, datos)
        return cursor.fetchone()    

    def cerrar_conexion(self):
        self.__conn.close()
        
conexion = Conectar() # Crea el objeto conexion para usar en otros archivos
conexion.probar_conexion() # Prueba la conexion a la base de datos
