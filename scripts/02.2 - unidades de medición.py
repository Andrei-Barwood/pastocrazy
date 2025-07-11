# -*- coding: utf-8 -*-

def calcular_tiempo_caminata():
    """
    Este programa resuelve cuántas horas toma caminar una distancia
    dada a un ritmo constante, explicando el proceso.
    """

    # --- Constantes y Variables del Problema ---
    MINUTOS_POR_HORA = 60
    distancia_millas = 12
    ritmo_minutos_por_milla = 15

    # --- Inicio del Programa ---
    print("*" * 65)
    print("🚶‍♂️  Calculadora de Tiempo de Caminata  🚶‍♀️")
    print("*" * 65)

    ##
    # SECCIÓN: SOLUCIÓN DEL EJERCICIO
    ##
    print("\n## Problema a Resolver ##")
    print("-----------------------------------------------------------------")
    print(f"¿Cuántas horas le tomaría a una persona caminar {distancia_millas} millas")
    print(f"si su ritmo promedio es de {ritmo_minutos_por_milla} minutos por milla?\n")

    print("### Explicación y Solución Paso a Paso ###\n")

    # Paso 1: Calcular el tiempo total en minutos
    print("➡️  Paso 1: Calcular el tiempo total del recorrido en minutos.")
    print("Para esto, multiplicamos la distancia total por el ritmo por milla.")

    tiempo_total_minutos = distancia_millas * ritmo_minutos_por_milla

    print(f"   Cálculo: {distancia_millas} millas * {ritmo_minutos_por_milla} minutos/milla = {tiempo_total_minutos} minutos.\n")

    # Paso 2: Convertir los minutos totales a horas
    print("➡️  Paso 2: Convertir el tiempo total de minutos a horas.")
    print(f"Sabemos que 1 hora tiene {MINUTOS_POR_HORA} minutos, por lo que dividimos el total de minutos por {MINUTOS_POR_HORA}.")

    tiempo_total_horas = tiempo_total_minutos / MINUTOS_POR_HORA

    print(f"   Cálculo: {tiempo_total_minutos} minutos / {MINUTOS_POR_HORA} minutos/hora = {int(tiempo_total_horas)} horas.\n")

    # --- Resultado Final ---
    print("### Resultado Final ###")
    print(f"✅ A una persona le tomaría {int(tiempo_total_horas)} horas caminar {distancia_millas} millas.")
    print("-----------------------------------------------------------------")

# --- Ejecutar la función principal ---
if __name__ == "__main__":
    calcular_tiempo_caminata()