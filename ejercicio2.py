numerador = float(input("Introduce el primer número (numerador): "))

divisor = float(input("Introduce el segundo número (divisor): "))

if divisor == 0:
    print("Error: No se puede dividir por cero.")
else:
    resultado = numerador / divisor
    print(f"El resultado de la división es: {resultado}")
