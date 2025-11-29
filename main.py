import os
import sys

from models.Usuario import Usuario 
from dao.UsuarioDAO import UsuarioDAO

#funcion para iniciar sesion
def iniciar_sesion():
    usuario = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
# Instanciando objeto tipo usuario
    user = Usuario(usuario=usuario, password=password)
# Instanciamos objeto dao para usuario
    dao = UsuarioDAO(user)
    if dao.iniciar_sesion():
        menu_sesion(user)
    else:
        print('Error en datos, intente nuevamente.')

def registrar_usuario():
    usuario = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
    # Instanciando objeto tipo usuario
    user = Usuario(usuario=usuario, password=password)
    # Instanciamos objeto dao para usuario
    dao = UsuarioDAO(user)
    if dao.registrar_usuario():
        print('Usuario registrado con éxito.')
    else:
        print('Error al registrar el usuario.')

def menu_principal():# Menú principal de la aplicación
    while True:
        os.system('clear') # Limpiar la pantalla
        print('=== Menu Principal ===') # Menu principal
        print('1. Iniciar Sesión')
        print('0. Salir')

        option = input('Seleccione una opción: ')
        
        if option == '1':
            iniciar_sesion()
        elif option == '0':
            os.system('clear')
            print('Saliendo del programa hasta luego...')
            break
            
def menu_sesion(user: Usuario):
    while True:
        # Limpiar pantalla
        os.system('clear')
        # Cargamos opciones
        print('==== Menú principal ====')
        os.system('clear')
        print(f'Bienvenido: {user.nombre} {user.apellido}')
        print('1. Registro de Usuario')
        print('2.')
        print('0. Cerrar sesión')
        opcion = input('Ingrese su opción:\n')
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '0':
            print(f'Hasta luego {user.nombre} {user.apellido}')
            user = None       
        input('Presione enter para continuar...')
        break

menu_principal()
