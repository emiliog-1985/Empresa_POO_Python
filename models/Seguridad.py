import hashlib
import os

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # Genera una sal aleatoria de 16 bytes
    else:
        salt = salt.encode('utf-8')
    # Combina la contraseña y la sal antes de hashear
    hash_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    return hash_password, salt.hex()

def verify_password(password, stored_password_hash, salt):
    # Recalcula el hash de la contraseña con la misma sal
    new_password_hash = hashlib.sha256(bytes.fromhex(salt) + password.encode('utf-8')).hexdigest()
    # Compara el hash calculado con el hash almacenado
    return new_password_hash == stored_password_hash

# Ejemplo de uso
password = "1234"
stored_password_hash, salt = hash_password(password)

# Almacenar el hash y la sal en una base de datos o en otro lugar seguro
print("Hash de contraseña almacenado:", stored_password_hash)
print("Sal utilizada:", salt)

# Verificación de una contraseña
input_password = input('Ingrese contraseña')
if verify_password(input_password, stored_password_hash, salt):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")