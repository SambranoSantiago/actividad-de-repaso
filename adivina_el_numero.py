def adivina_numero():
    print("Piensa en un número entre 1 y 100.")
    input("Cuando estés listo, presiona Enter para comenzar...")

    minimo = 1
    maximo = 100

    while True:
        # Calculamos el número medio
        intento = (minimo + maximo) // 2

        respuesta = input(f"¿Es {intento} tu número? (mayor/menor/igual): ").lower()

        if respuesta == "igual":
            print(f"¡Adiviné! El número es {intento}.")
            break
        elif respuesta == "mayor":
            minimo = intento + 1
        elif respuesta == "menor":
            maximo = intento - 1
        else:
            print("Por favor, responde con 'mayor', 'menor' o 'igual'.")

if __name__ == "__main__":
    adivina_numero()

