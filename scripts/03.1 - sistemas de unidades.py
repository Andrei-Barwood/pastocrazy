def explicar_ventajas_sistema_metrico():
    """
    Esta función imprime una explicación sobre las ventajas del sistema métrico
    en comparación con el sistema imperial para longitud, masa, fuerza y temperatura.
    """

    print("--- Ventajas del Sistema Métrico vs. el Sistema Imperial ---")

    # Explicación general
    print("\nEl sistema métrico (Sistema Internacional de Unidades o SI) es el estándar mundial")
    print("para la ciencia, la industria y el comercio. Su principal ventaja es su simplicidad")
    print("y coherencia, ya que se basa en múltiplos de 10.")
    print("----------------------------------------------------------------------")

    # Longitud (Metro vs. Pulgada/Pie/Yarda/Milla)
    print("\n## Longitud 📏")
    print("El sistema métrico utiliza el 'metro' como unidad base.")
    print("Las conversiones son sencillas: 1 kilómetro = 1,000 metros; 1 metro = 100 centímetros.")
    print("En el sistema imperial, las relaciones son irregulares y más difíciles de memorizar:")
    print("  - 1 pie = 12 pulgadas")
    print("  - 1 yarda = 3 pies")
    print("  - 1 milla = 1,760 yardas")
    print("\n**Ventaja métrica:** La estructura decimal simplifica enormemente los cálculos y las conversiones.")
    print("----------------------------------------------------------------------")

    # Masa (Kilogramo vs. Onza/Libra/Tonelada)
    print("\n## Masa ⚖️")
    print("El sistema métrico utiliza el 'kilogramo' (y el gramo).")
    print("La relación es directa y decimal: 1 kilogramo = 1,000 gramos; 1 tonelada métrica = 1,000 kilogramos.")
    print("El sistema imperial usa onzas, libras y toneladas, con conversiones menos intuitivas:")
    print("  - 1 libra = 16 onzas")
    print("  - 1 tonelada corta = 2,000 libras")
    print("\n**Ventaja métrica:** La consistencia decimal facilita los cálculos científicos y de ingeniería.")
    print("Además, hay una relación directa y simple entre volumen y masa para el agua (1 litro de agua ≈ 1 kilogramo).")
    print("----------------------------------------------------------------------")

    # Fuerza (Newton vs. Libra-fuerza)
    print("\n## Fuerza 💪")
    print("En el sistema métrico, la unidad de fuerza es el 'Newton' (N).")
    print("Se define directamente a partir de las unidades base de masa y aceleración (1 N = 1 kg * m/s²),")
    print("lo que sigue la Segunda Ley de Newton (F=ma) de una manera limpia.")
    print("El sistema imperial usa la 'libra-fuerza' (lbf). Esto puede generar confusión entre masa (libra-masa, lb) y fuerza (lbf),")
    print("ya que ambas se denominan 'libra'. Para que F=ma funcione, se debe introducir una constante gravitacional (g_c),")
    print("lo que complica los cálculos.")
    print("\n**Ventaja métrica:** La definición del Newton es coherente y no genera ambigüedad entre masa y fuerza,")
    print("simplificando las ecuaciones en física e ingeniería.")
    print("----------------------------------------------------------------------")

    # Temperatura (Celsius/Kelvin vs. Fahrenheit)
    print("\n## Temperatura 🌡️")
    print("El sistema métrico utiliza la escala 'Celsius' (°C) para el uso diario y 'Kelvin' (K) para la ciencia.")
    print("La escala Celsius se basa en los puntos de congelación (0 °C) y ebullición (100 °C) del agua,")
    print("lo cual es intuitivo. La escala Kelvin es una escala absoluta donde 0 K es el cero absoluto.")
    print("La escala Fahrenheit (°F) del sistema imperial tiene puntos de referencia menos intuitivos (congelación del agua a 32 °F y ebullición a 212 °F).")
    print("\n**Ventaja métrica:** La escala Celsius es más sencilla de usar en la vida cotidiana debido a sus puntos de referencia basados en el agua.")
    print("La escala Kelvin es el estándar para la ciencia porque se relaciona directamente con la energía térmica y no tiene valores negativos,")
    print("lo que simplifica las leyes termodinámicas.")

# --- Ejecutar el script ---
if __name__ == "__main__":
    explicar_ventajas_sistema_metrico()