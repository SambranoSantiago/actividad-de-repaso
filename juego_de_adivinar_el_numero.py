
import random

def jugar_adivina_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    intentos = 0
    while True:
        intentos += 1
        try:
            # Solicitar al jugador que ingrese un número
            numero_ingresado = int(input("Adivina el número (entre 1 y 100): "))

            # Verificar si el número es correcto
            if numero_ingresado == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
            elif numero_ingresado < numero_secreto:
                print("El número es demasiado bajo. Intenta con un número más grande.")
            else:
                print("El número es demasiado alto. Intenta con un número más pequeño.")
        except ValueError:
            print("Ingresa un número válido.")

if __name__ == "__main__":
    jugar_adivina_numero()
