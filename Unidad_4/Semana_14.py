"""
Calculo Descuento Python
Semana_14.py
Autor: Guido Eduardo Villarroel Ramos
Descripción: Calcula el descuento y el monto final a pagar usando funciones con
parámetros y valor predeterminado. Incluye dos llamadas de ejemplo.
"""

def calcular_descuento(monto_total: float, porcentaje: float = 0.10) -> float:
    """
    Calcula el descuento a partir de un monto_total y un porcentaje.
    :param monto_total: Total de la compra (>= 0).
    :param porcentaje: Porcentaje de descuento en formato decimal (0.10 = 10%).
                       Por defecto 0.10 (10%).
    :return: Monto de descuento (float).
    """
    if monto_total < 0:
        raise ValueError("El monto total no puede ser negativo.")
    if porcentaje < 0 or porcentaje > 1:
        raise ValueError("El porcentaje debe estar entre 0.0 y 1.0 (ej., 0.15 = 15%).")

    descuento = monto_total * porcentaje
    return round(descuento, 2)

def imprimir_resumen(monto_total: float, porcentaje: float = 0.10) -> None:
    descuento = calcular_descuento(monto_total, porcentaje)
    total_a_pagar = round(monto_total - descuento, 2)
    print("======================================")
    print(f"Monto total:       ${monto_total:,.2f}")
    print(f"Descuento ({porcentaje*100:.0f}%):  -${descuento:,.2f}")
    print("--------------------------------------")
    print(f"Total a pagar:     ${total_a_pagar:,.2f}")

if __name__ == "__main__":
    # Llamada 1: porcentaje por defecto (10%)
    imprimir_resumen(250.00)

    # Llamada 2: porcentaje específico (15%)
    imprimir_resumen(520.00, 0.15)
