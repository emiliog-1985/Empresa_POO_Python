import os
import colorama
import time
import sys

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
    contrasena = input(colorama.Fore.CYAN + 'Ingrese su contraseña: ' + colorama.Style.RESET_ALL)

def menu_principal():# Menú principal de la aplicación
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
    exit()

menu_principal()