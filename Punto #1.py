import numpy as np
import matplotlib.pyplot as plt

def graficar_seno_coseno():
    print("Programa para graficar las funciones seno y coseno.")

    # Solicitar el rango al usuario
    while True:
        try:
            rango_inicio = float(input("Introduce el inicio del rango (en radianes): "))
            rango_fin = float(input("Introduce el fin del rango (en radianes): "))
            if rango_inicio >= rango_fin:
                print("El inicio del rango debe ser menor que el fin. Intentalo de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor introduce valores validos.")

    # Generar puntos en el rango especificado
    x = np.linspace(rango_inicio, rango_fin, 500)
    seno = np.sin(x)
    coseno = np.cos(x)

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    plt.plot(x, seno, label='Seno', color='red')
    plt.plot(x, coseno, label='Coseno', color='blue')

    # Configurar título, etiquetas y leyenda
    plt.title("Funciones Seno y Coseno")
    plt.xlabel("x (radianes)")
    plt.ylabel("y")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend()

    # Mostrar la gráfica
    plt.show()

# Ejecutar el programa
graficar_seno_coseno()