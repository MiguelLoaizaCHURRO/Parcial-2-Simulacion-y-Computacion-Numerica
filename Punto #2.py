import numpy as np
import matplotlib.pyplot as plt
import math

def funcion_a(x):
    """f(x) = sqrt(34 * e^2) / (cos(23.7) + 12)"""
    return np.full_like(x, np.sqrt(34 * np.exp(2)) / (np.cos(23.7) + 12))

def funcion_b(x):
    """f(x) = 7 * e^(-x) + 3.54"""
    return 7 * np.exp(-x) + 3.54

def funcion_c(x):
    """f(x) = 20 * log((25.4/pi))"""
    return np.full_like(x, 20 * np.log(25.4 / math.pi))

def funcion_d(x):
    """f(x) = ((3+5i)^3 - 1) / sqrt(0.5 - 3i)"""
    complex_num = (3 + 5j)**3 - 1
    denominator = np.sqrt(0.5 - 3j)
    return np.full_like(x, (complex_num / denominator).real)  # Devuelve solo la parte real

def seleccionar_funcion():
    while True:
        print("\nSelecciona la función a graficar:")
        print("a) f(x) = sqrt(34 * e^2) / (cos(23.7) + 12)")
        print("b) f(x) = 7 * e^(-x) + 3.54")
        print("c) f(x) = 20 * log((25.4/pi))")
        print("d) f(x) = ((3+5i)^3 - 1) / sqrt(0.5 - 3i)")
        print("e) Salir")

        opcion = input("Introduce la letra de la opción (a/b/c/d/e): ").strip().lower()
        if opcion == "a":
            return funcion_a, "f(x) = sqrt(34 * e^2) / (cos(23.7) + 12)"
        elif opcion == "b":
            return funcion_b, "f(x) = 7 * e^(-x) + 3.54"
        elif opcion == "c":
            return funcion_c, "f(x) = 20 * log((25.4/pi))"
        elif opcion == "d":
            return funcion_d, "f(x) = ((3+5i)^3 - 1) / sqrt(0.5 - 3i)"
        elif opcion == "e":
            print("Saliendo del programa...")
            return None, None
        else:
            print("Opción no válida. Intenta de nuevo.")

def solicitar_rango():
    while True:
        try:
            inicio = float(input("Introduce el valor inicial del rango: "))
            fin = float(input("Introduce el valor final del rango: "))
            if inicio < fin:
                return inicio, fin
            else:
                print("El valor inicial debe ser menor que el valor final. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce valores numéricos válidos.")

def graficar_funcion():
    print("Bienvenido al graficador de funciones")

    while True:
        # Seleccionar la función
        funcion, descripcion = seleccionar_funcion()

        # Solicitar el rango al usuario
        inicio, fin = solicitar_rango()

        # Generar los valores de x en el rango especificado
        x = np.linspace(inicio, fin, 500)

        try:
            # Calcular los valores de y utilizando la función
            y = funcion(x)

            # Graficar la función
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, label=descripcion, color="blue")
            plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
            plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
            plt.title("Gráfica de la función")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.grid(True, linestyle="--", alpha=0.7)
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error al calcular o graficar la función: {e}")

# Ejecutar el programa
graficar_funcion()
