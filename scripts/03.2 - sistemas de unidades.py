# -*- coding: utf-8 -*-

def explicar_conversion_temperatura():
    """
    Esta función explica en detalle la conversión de 68°F a los sistemas
    MKS, CGS y SI, y luego imprime la explicación en la consola.
    """
    # 1. Definir la temperatura inicial en Fahrenheit
    temp_f = 68.0

    # 2. Convertir Fahrenheit a Celsius usando la fórmula C = (F - 32) * 5/9
    temp_c = (temp_f - 32) * 5/9

    # 3. Convertir Celsius a Kelvin usando la fórmula K = C + 273.15
    temp_k = temp_c + 273.15

    # 4. Construir el texto explicativo usando f-strings para insertar los valores
    explicacion = f"""
    ¡Hola! Aquí tienes la explicación detallada sobre la temperatura ambiente de 68°F
    y su equivalencia en los sistemas MKS, CGS y SI.

    ---
    ## ❓ La Pregunta Fundamental: Unidad de Temperatura

    Primero, es clave saber qué unidad de temperatura utiliza cada sistema para ser precisos.

    * **Sistema Internacional (SI):** Es el estándar global para la ciencia y la tecnología. Su unidad base para la temperatura es el **Kelvin (K)**.
    * **Sistema MKS (Metro-Kilogramo-Segundo):** Este es el sistema precursor del SI y, como tal, también utiliza el **Kelvin (K)** como su unidad fundamental de temperatura.
    * **Sistema CGS (Centímetro-Gramo-Segundo):** Aunque en la práctica a veces se usa el grado Celsius, la unidad fundamental para la temperatura termodinámica en el CGS es también el **Kelvin (K)**.

    ✅ **Conclusión clave:** Los tres sistemas (MKS, CGS y SI) utilizan el **Kelvin (K)** como su unidad de temperatura fundamental. Por lo tanto, el objetivo es convertir 68°F a Kelvin.

    ---
    ## ⚙️ Proceso de Conversión Paso a Paso

    La conversión se realiza en dos etapas: primero a Celsius y luego a Kelvin.

    **Paso 1: Convertir Fahrenheit (°F) a Celsius (°C)**
    - **Fórmula:** $C = (F - 32) * {5}÷{9}$
    - **Cálculo:**
        - $C = ({temp_f}°F - 32) * {5}÷{9}$
        - $C = {temp_f - 32} * {5}÷{9}$
        - **$C = {temp_c:.2f}°C$**

    **Paso 2: Convertir Celsius (°C) a Kelvin (K)**
    - **Fórmula:** $K = C + 273.15$
    - **Cálculo:**
        - $K = {temp_c:.2f}°C + 273.15$
        - **$K = {temp_k:.2f} K$**

    ---
    ## 🎯 Respuesta Final

    La temperatura ambiente de 68°F, expresada en las unidades fundamentales de los sistemas solicitados, es:

    * **Temperatura en el sistema MKS:** **{temp_k:.2f} K**
    * **Temperatura en el sistema CGS:** **{temp_k:.2f} K**
    * **Temperatura en el sistema SI:** **{temp_k:.2f} K**

    En resumen, **68°F es igual a 293.15 Kelvin**.
    """

    # 5. Imprimir la explicación completa
    print(explicacion)

# --- Ejecución del Script ---
# Esta línea asegura que la función se ejecute solo cuando corres este archivo directamente.
if __name__ == "__main__":
    explicar_conversion_temperatura()