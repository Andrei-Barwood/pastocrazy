import textwrap

def justificar_texto(texto, ancho):
    """
    Toma un bloque de texto, lo envuelve a un ancho específico y luego
    justifica cada línea añadiendo espacios entre las palabras.
    """
    # Primero, envolvemos el texto para obtener una lista de líneas
    lineas_envueltas = textwrap.wrap(texto, ancho)
    
    lineas_justificadas = []

    # Iteramos sobre todas las líneas excepto la última
    for i in range(len(lineas_envueltas) - 1):
        linea = lineas_envueltas[i]
        palabras = linea.split()

        # Si hay más de una palabra en la línea, la justificamos
        if len(palabras) > 1:
            espacios_a_añadir = ancho - len(''.join(palabras))
            huecos = len(palabras) - 1
            
            # Distribuir los espacios
            espacios_por_hueco = espacios_a_añadir // huecos
            espacios_extra = espacios_a_añadir % huecos
            
            linea_nueva = ""
            for j in range(len(palabras) - 1):
                linea_nueva += palabras[j]
                linea_nueva += ' ' * espacios_por_hueco
                if j < espacios_extra:
                    linea_nueva += ' '
            linea_nueva += palabras[-1]
            lineas_justificadas.append(linea_nueva)
        else:
            # Si solo hay una palabra, la dejamos como está
            lineas_justificadas.append(linea)

    # Añadimos la última línea sin justificarla
    if lineas_envueltas:
        lineas_justificadas.append(lineas_envueltas[-1])

    return "\n".join(lineas_justificadas)

def explicar_conversion_yarda_a_cm():
    """
    Explica la lógica para convertir media yarda a centímetros
    y formatea el texto de la explicación de manera justificada.
    """
    # Texto de la explicación
    explicacion = """\
    Para resolver este problema, primero necesitamos saber la equivalencia entre yardas y centímetros. Una yarda equivale a 91.44 centímetros. El problema nos pide calcular cuántos centímetros hay en MEDIA yarda. Por lo tanto, la lógica es bastante directa: 1. Tomamos el valor total de una yarda en centímetros (91.44 cm). 2. Dividimos ese valor por la mitad (es decir, entre 2) para encontrar el equivalente a media yarda. La operación matemática sería: 91.44 cm / 2 = 45.72 cm. Así, la respuesta es que en media yarda hay 45.72 centímetros.
    """
    
    ancho_deseado = 72

    # Usar nuestra nueva función para justificar el texto
    texto_final = justificar_texto(explicacion, ancho_deseado)

    # Imprimir la explicación justificada
    print("--- Lógica para convertir media yarda a centímetros ---")
    print(texto_final)

# Llamar a la función para que se ejecute la explicación
explicar_conversion_yarda_a_cm()