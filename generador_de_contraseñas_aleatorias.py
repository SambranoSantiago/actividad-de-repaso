import random
import string

def generar_contrasena():
    # Definir los caracteres permitidos para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar una contraseña aleatoria de al menos 12 caracteres
    longitud_minima = 12
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud_minima))

    return contrasena

# Generar la contraseña
contrasena_generada = generar_contrasena()

# Mostrar la contraseña al usuario
print(f"Contraseña generada: {contrasena_generada}")
