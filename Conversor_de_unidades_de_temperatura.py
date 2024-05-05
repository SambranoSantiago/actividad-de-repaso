def celsius_a_farenheit(celsius):
    """Convierte grados Celsius a Farenheit."""
    farenheit = (celsius * 1.8) + 32
    return farenheit

def farenheit_a_celsius(farenheit):
    """Convierte grados Farenheit a Celsius."""
    celsius = (farenheit - 32) / 1.8
    return celsius

temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de temperatura (C para Celsius, F para Farenheit): ").upper()

if unidad == "C":
    farenheit = celsius_a_farenheit(temperatura)
    print(f"{temperatura:.2f}°C equivale a {farenheit:.2f}°F")
elif unidad == "F":
    celsius = farenheit_a_celsius(temperatura)
    print(f"{temperatura:.2f}°F equivale a {celsius:.2f}°C")
else:
    print("Unidad de temperatura no válida. Ingrese 'C' o 'F'.")