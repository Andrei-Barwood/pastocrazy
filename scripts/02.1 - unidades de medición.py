# -*- coding: utf-8 -*-

def resolver_y_explicar_ejercicio():
    """
    Este programa resuelve un problema de conversión de unidades de velocidad a distancia,
    explica cada paso y compara unidades del sistema imperial con el sistema métrico.
    """

    # --- Constantes de Conversión ---
    # Es una buena práctica definir estos valores fijos al inicio.
    PIES_POR_MILLA = 5280
    MINUTOS_POR_HORA = 60
    KM_POR_MILLA = 1.60934
    METROS_POR_PIE = 0.3048

    # --- Inicio del Programa ---
    print("*" * 70)
    print("🔢  Programa para Calcular Distancia y Comparar Unidades de Medida  🔢")
    print("*" * 70)

    ##
    # SECCIÓN 1: SOLUCIÓN DEL EJERCICIO PRINCIPAL
    ##
    print("\n\n## Problema Principal 🚗💨 ##")
    print("----------------------------------------------------------------------")
    print("Determinar la distancia en pies, recorrida durante un minuto")
    print("por un automóvil que viaja a 50 millas por hora.\n")

    # --- Variables del problema ---
    velocidad_mph = 50
    tiempo_minutos = 1

    print("### Explicación y Solución Paso a Paso ###\n")

    # Paso 1: Calcular la distancia en millas por minuto
    print("➡️  Paso 1: Calcular cuántas millas recorre el auto en un minuto.")
    print(f"La velocidad es de {velocidad_mph} millas por hora. Sabemos que 1 hora tiene {MINUTOS_POR_HORA} minutos.")
    print(f"Para encontrar la distancia por minuto, dividimos la velocidad entre {MINUTOS_POR_HORA}.")

    distancia_millas_por_minuto = velocidad_mph / MINUTOS_POR_HORA

    print(f"   Cálculo: {velocidad_mph} millas/hora ÷ {MINUTOS_POR_HORA} min/hora = {distancia_millas_por_minuto:.4f} millas por minuto.\n")

    # Paso 2: Convertir la distancia de millas a pies
    print("➡️  Paso 2: Convertir esa distancia de millas a pies.")
    print(f"Sabemos que 1 milla equivale a {PIES_POR_MILLA} pies.")
    print("Multiplicamos la distancia en millas que calculamos por este factor de conversión.")

    distancia_total_pies = distancia_millas_por_minuto * PIES_POR_MILLA

    print(f"   Cálculo: {distancia_millas_por_minuto:.4f} millas * {PIES_POR_MILLA} pies/milla = {distancia_total_pies:.2f} pies.\n")

    # --- Resultado Final ---
    print("### Resultado Final del Problema ###")
    # Usamos int() para mostrar el número entero, ya que el resultado no tiene decimales.
    print(f"✅ Un automóvil que viaja a 50 mph recorre {int(distancia_total_pies)} pies en un minuto.")
    print("----------------------------------------------------------------------")


    ##
    # SECCIÓN 2: COMPARACIÓN DE UNIDADES
    ##
    print("\n\n## Comparación de Unidades (Imperial vs. Métrico) 🌍 ##")
    print("----------------------------------------------------------------------\n")

    # Comparación 1: Millas vs. Kilómetros
    print("📏 **Millas vs. Kilómetros (para distancias recorridas)**\n")
    print(f"Una milla es una unidad de longitud más grande que un kilómetro.")
    print(f"   - **1 milla equivale a {KM_POR_MILLA} kilómetros.**")
    print(f"Por ejemplo, la velocidad del auto de 50 mph es igual a ({velocidad_mph} * {KM_POR_MILLA}) = {velocidad_mph * KM_POR_MILLA:.2f} km/h.\n")

    # Comparación 2: Pies vs. Kilómetros en altura
    print("🏔️ **Pies vs. Kilómetros (para altura)**\n")
    print("Estas unidades también se usan para medir la altura de montañas o la altitud de vuelo.")
    print(f"Un pie es una unidad mucho más pequeña. **1 pie = {METROS_POR_PIE} metros** (o 0.0003048 km).")
    altura_aconcagua_metros = 6961 # Altura del Aconcagua, relevante para Chile/Sudamérica.
    altura_aconcagua_pies = altura_aconcagua_metros / METROS_POR_PIE
    print(f"Por ejemplo, el cerro Aconcagua mide {altura_aconcagua_metros} metros de altura, lo que equivale a:")
    print(f"   - **{altura_aconcagua_metros / 1000:.2f} kilómetros de altura.**")
    print(f"   - **{altura_aconcagua_pies:.2f} pies de altura.**\n")

    # Comparación 3: Pies vs. Kilómetros en superficie
    print("🏃 **Pies vs. Kilómetros (sobre la superficie)**\n")
    print("Esta es una comparación directa de longitud sobre una superficie plana.")
    pies_en_un_km = 1000 / METROS_POR_PIE
    print(f"Para recorrer 1 kilómetro sobre la superficie, necesitas dar muchos pasos.")
    print(f"   - **1 kilómetro equivale a {pies_en_un_km:.2f} pies.**")
    print("Esto muestra lo pequeña que es la unidad 'pie' en comparación con un 'kilómetro'.")
    print("----------------------------------------------------------------------")


# --- Ejecutar la función principal ---
if __name__ == "__main__":
    resolver_y_explicar_ejercicio()