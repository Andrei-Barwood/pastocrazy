#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Este script convierte un valor de energía de Julios a pies-libra
y explica el procedimiento.
"""

import textwrap

# --- Datos Iniciales ---
# Energía en Julios que queremos convertir.
julios = 1000

# Factor de conversión: 1 Julio equivale aproximadamente a 0.73756 pies-libra.
factor_conversion = 0.737562149

# --- Cálculo ---
# Multiplicamos los Julios por el factor de conversión para obtener los pies-libra.
pies_libra = julios * factor_conversion

# --- Explicación del Proceso ---
# Usamos textwrap para formatear la explicación en un párrafo justificado.

explicacion_texto = f"""\
Para convertir una cantidad de energía de Julios (J) a pies-libra (ft-lb), \
necesitamos usar un factor de conversión específico. La relación entre estas \
dos unidades de energía es la siguiente: 1 Julio es aproximadamente igual a \
0.73756 pies-libra.

El procedimiento es bastante directo: simplemente tomamos la cantidad de energía \
en Julios que deseamos convertir y la multiplicamos por este factor de conversión.

En este caso particular, el cálculo es: {julios} J * {factor_conversion} ≈ {pies_libra:.2f} ft-lb.

Por lo tanto, 1000 Julios de energía equivalen a aproximadamente {pies_libra:.2f} \
pies-libra.
"""

# Ancho deseado para el texto justificado.
ancho_linea = 80

# Usamos textwrap.fill() para justificar el texto.
explicacion_formateada = textwrap.fill(explicacion_texto, width=ancho_linea)

# --- Impresión del Resultado ---
print("--- Explicación de la Conversión de Julios a Pies-Libras ---")
print(explicacion_formateada)
print("\n" + "="*ancho_linea)
print(f"Resultado Final: {julios} Julios equivalen a {pies_libra:.4f} pies-libra.")
print("="*ancho_linea)