# -*- coding: utf-8 -*-
import textwrap

def justificar_texto(texto, ancho):
    """
    Toma un bloque de texto y lo devuelve con formato justificado
    según el ancho de línea especificado.
    """
    # Usamos textwrap para dividir el texto en líneas del ancho correcto
    lineas_envueltas = textwrap.wrap(texto, ancho, break_long_words=False, replace_whitespace=False)
    
    # Si el texto original no tenía saltos de línea, lo tratamos como un solo bloque
    if not lineas_envueltas:
        return ""
        
    lineas_justificadas = []
    # Iteramos sobre todas las líneas excepto la última del bloque
    for i in range(len(lineas_envueltas) - 1):
        linea = lineas_envueltas[i]
        palabras = linea.split()

        if len(palabras) <= 1:
            lineas_justificadas.append(linea)
            continue

        espacios_a_anadir = ancho - len(''.join(palabras))
        num_huecos = len(palabras) - 1
        
        if num_huecos == 0:
             lineas_justificadas.append(linea)
             continue

        espacios_base = espacios_a_anadir // num_huecos
        espacios_extra = espacios_a_anadir % num_huecos

        linea_justificada = ""
        for j, palabra in enumerate(palabras[:-1]):
            linea_justificada += palabra
            linea_justificada += ' ' * espacios_base
            if j < espacios_extra:
                linea_justificada += ' '
        
        linea_justificada += palabras[-1]
        lineas_justificadas.append(linea_justificada)

    # Añadimos la última línea sin justificar
    lineas_justificadas.append(lineas_envueltas[-1])
    return "\n".join(lineas_justificadas)


def explicar_conversion_temperatura_justificada():
    """
    Versión mejorada del script que imprime la explicación con texto justificado.
    """
    temp_f = 68.0
    temp_c = (temp_f - 32) * 5/9
    temp_k = temp_c + 273.15
    ancho_linea = 80 # Ancho de la consola en caracteres

    # --- Construcción de la explicación (ahora separada en bloques) ---
    
    titulo = "Explicación Detallada de Conversión de Temperatura"
    
    intro_texto = f"""¡Hola! Aquí tienes la explicación detallada sobre la temperatura ambiente de {temp_f}°F y su equivalencia en los sistemas MKS, CGS y SI."""

    unidad_titulo = "1. La Unidad de Temperatura en Cada Sistema"
    unidad_texto = """Primero, es clave saber qué unidad de temperatura utiliza cada sistema para ser precisos. El Sistema Internacional (SI), su precursor MKS (Metro-Kilogramo-Segundo) y el sistema CGS (Centímetro-Gramo-Segundo) utilizan el Kelvin (K) como su unidad fundamental para la temperatura termodinámica. Por lo tanto, el objetivo es convertir 68°F a Kelvin."""

    proceso_titulo = "2. Proceso de Conversión Paso a Paso"
    proceso_texto_1 = f"""La conversión se realiza en dos etapas. Primero, pasamos de Fahrenheit a Celsius con la fórmula C = (F - 32) * 5/9. Para {temp_f}°F, el cálculo es ({temp_f} - 32) * 5/9, lo que resulta en {temp_c:.2f}°C."""
    proceso_texto_2 = f"""Luego, convertimos de Celsius a Kelvin con la fórmula K = C + 273.15. El cálculo es {temp_c:.2f}°C + 273.15, lo que nos da un resultado final de {temp_k:.2f} K."""

    final_titulo = "3. Respuesta Final"
    final_texto = f"""La temperatura ambiente de 68°F, expresada en las unidades fundamentales de los sistemas solicitados, es la misma para los tres: {temp_k:.2f} K."""

    # --- Impresión con formato ---
    print("\n" + titulo.center(ancho_linea))
    print("=" * ancho_linea)
    print(justificar_texto(intro_texto, ancho_linea))
    print("-" * ancho_linea)
    
    print(unidad_titulo)
    print(justificar_texto(unidad_texto, ancho_linea))
    print("-" * ancho_linea)

    print(proceso_titulo)
    print(justificar_texto(proceso_texto_1, ancho_linea))
    print(justificar_texto(proceso_texto_2, ancho_linea))
    print("-" * ancho_linea)

    print(final_titulo)
    print(justificar_texto(final_texto, ancho_linea))
    print("=" * ancho_linea)


# --- Ejecución del Script ---
if __name__ == "__main__":
    explicar_conversion_temperatura_justificada()