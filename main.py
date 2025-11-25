import os
import colorama
import time
import sys

from models.Usuario import Usuario
from dao.UsuarioDAO import UsuarioDAO

symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']

def inicio_empresa(duration=2): # Animación de salida de la aplicación 
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        sys.stdout.write('\r' + symbols[i % len(symbols)] + ' Bienvenido a la empresa POO CRUD')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(symbols[0]) + len(' Bienvenido a la empresa POO CRUD')) + '\r') # Clear the line
    sys.stdout.flush()

def iniciar_sesion(): # Función para iniciar sesión
    usuario = input(colorama.Fore.CYAN + 'Ingrese su usuario: ' + colorama.Style.RESET_ALL)
    password = input(colorama.Fore.CYAN + 'Ingrese su contraseña: ' + colorama.Style.RESET_ALL)
    # Instanciando objeto tipo usuario
    user = Usuario(usuario=usuario, password=password)
    # Instanciamos objeto dao para usuario
    dao = UsuarioDAO(user)
    if dao.iniciar_sesion():
        menu_sesion(user)
    else:
        print('Error en datos, intente nuevamente.')

def menu_principal():# Menú principal de la aplicación
    while True:
        inicio_empresa() # animacion de bienvenida
        os.system('clear') # Limpiar la pantalla
        print(colorama.Fore.GREEN + '=== Menu Principal ===' + colorama.Style.RESET_ALL) # Menu principal
        print('1. Iniciar Sesión')
        print('0. Salir')

        option = input(colorama.Fore.YELLOW + 'Seleccione una opción: ' + colorama.Style.RESET_ALL)
        
        if option == '1':
            iniciar_sesion()
        elif option == '0':
            os.system('clear')
            print(colorama.Fore.RED + 'Saliendo del programa hasta luego...' + colorama.Style.RESET_ALL)
            break
            
def menu_sesion(user: Usuario):
    while True:
        # Limpiar pantalla
        os.system('clear')
        # Cargamos opciones
        print('==== Menú principal ====')
        os.system('clear')
        print(f'Bienvenido: {user.nombre} {user.apellido}')
        print('1.')
        print('2.')
        print('0. Cerrar sesión')
        opcion = input('Ingrese su opción:\n')
        
        if opcion == '0':
            print(f'Hasta luego {user.nombre} {user.apellido}')
            user = None
            break
        
        input('Presione enter para continuar...')

menu_principal()
