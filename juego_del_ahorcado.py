import random

# Lista de palabras en castellano
palabras = ["manzana", "perro", "gato", "coche", "casa", "sol", "playa", "amigo"]

def seleccionar_palabra():
    """Selecciona una palabra aleatoria de la lista."""
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    """Muestra la palabra oculta con las letras adivinadas."""
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def main():
    palabra_secreta = seleccionar_palabra()
    intentos_maximos = 5
    letras_adivinadas = set()

    print("¡Bienvenido al juego del ahorcado!")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")
    print(mostrar_palabra(palabra_secreta, letras_adivinadas))

    while intentos_maximos > 0:
        letra = input("Introduce una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. ¡Intenta con otra!")
        elif letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print(mostrar_palabra(palabra_secreta, letras_adivinadas))
            if palabra_secreta == mostrar_palabra(palabra_secreta, letras_adivinadas):
                print("¡Felicidades! ¡Adivinaste la palabra!")
                break
        else:
            intentos_maximos -= 1
            print(f"Letra incorrecta. Te quedan {intentos_maximos} intentos.")

    if intentos_maximos == 0:
        print(f"¡Se acabaron los intentos! La palabra era '{palabra_secreta}'.")

if __name__ == "__main__":
    main()

