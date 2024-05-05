
def validar_contrasena(contrasena):
    # Verificar la longitud mínima
    if len(contrasena) < 8:
        return False

    # Verificar si hay al menos una letra mayúscula, una letra minúscula, un número y un carácter especial
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        else:
            # Puedes personalizar la lista de caracteres especiales según tus necesidades
            caracteres_especiales = "!@#$%^&*()_+{}[]|:<>.?/~"
            if caracter in caracteres_especiales:
                tiene_especial = True

    # Verificar si cumple con todos los requisitos
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False

# Solicitar la contraseña al usuario
contrasena_usuario = input("Ingresa una contraseña: ")

# Validar la contraseña
if validar_contrasena(contrasena_usuario):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")

