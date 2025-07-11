def quiz_potencias_de_diez():
    """
    Un quiz interactivo para aprender a expresar números como potencias de diez.
    """

    # Lista de números, sus explicaciones y opciones de respuesta.
    # Cada elemento es una tupla: (número, explicación, [opciones], respuesta_correcta)
    preguntas = [
        (
            "10.000",
            "Para números enteros mayores que 1, cuenta cuántos ceros hay después del 1. Ese número será el exponente positivo.",
            ["10^3", "10^4", "10^-4"],
            "10^4"
        ),
        (
            "0.0001",
            "Para números decimales menores que 1, cuenta cuántas posiciones mueves el punto decimal hacia la derecha hasta llegar al primer número entero (en este caso, 1). El número de posiciones será el exponente, pero negativo.",
            ["10^-3", "10^4", "10^-4"],
            "10^-4"
        ),
        (
            "1000",
            "Recuerda, solo cuenta los ceros que siguen al 1.",
            ["10^3", "10^2", "10^-3"],
            "10^3"
        ),
        (
            "1.000.000",
            "Este es un número grande. La cantidad de ceros te dará directamente el exponente positivo.",
            ["10^5", "10^7", "10^6"],
            "10^6"
        ),
        (
            "0.0000001",
            "Mueve el punto decimal hacia la derecha y cuenta los espacios hasta pasar el 1. No olvides que el exponente será negativo.",
            ["10^-7", "10^-6", "10^-8"],
            "10^-7"
        ),
        (
            "0.00001",
            "Aplica la misma regla que para los otros decimales. ¿Cuántos lugares debes mover el punto?",
            ["10^5", "10^-5", "10^-4"],
            "10^-5"
        )
    ]

    print("--- Bienvenido al Quiz de Potencias de Diez ---")

    # Itera a través de cada pregunta
    for numero, explicacion, opciones, respuesta_correcta in preguntas:
        print("\n" + "="*40)
        print(f"\nNúmero a expresar como potencia de diez: {numero}")
        print(f"\nExplicación: {explicacion}")

        respuesta_usuario = ""
        while respuesta_usuario != respuesta_correcta:
            print("\nElige la opción correcta:")
            # Muestra las opciones
            for i, opcion in enumerate(opciones, 1):
                print(f"{i}. {opcion}")

            # Captura la entrada del usuario
            try:
                eleccion = int(input("Ingresa el número de tu elección: "))
                respuesta_usuario = opciones[eleccion - 1]

                if respuesta_usuario == respuesta_correcta:
                    print("\n¡Correcto! ¡Excelente trabajo! 👍 Pasemos al siguiente.")
                else:
                    print("\nIncorrecto. ¡Inténtalo de nuevo! 🧐")
            except (ValueError, IndexError):
                print("\nOpción no válida. Por favor, elige un número de la lista.")

    print("\n" + "="*40)
    print("\n¡Felicidades! Has completado todos los ejercicios. 🎉")

# Ejecuta el quiz
if __name__ == "__main__":
    quiz_potencias_de_diez()