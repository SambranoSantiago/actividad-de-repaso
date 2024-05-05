
def factorial_recursivo(n):
    """Calcula el factorial de un número utilizando recursión."""
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero positivo: "))
resultado_recursivo = factorial_recursivo(numero)
print(f"El factorial de {numero} es {resultado_recursivo}")
