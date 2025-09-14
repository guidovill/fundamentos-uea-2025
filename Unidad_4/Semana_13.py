def calcular_promedio_temperaturas(datos):
    """
    Calcula el promedio de temperaturas para cada ciudad.
    :param datos: Diccionario con nombre de ciudad como clave y lista de temperaturas como valor.
                  Ejemplo:
                  {
                      "Puyo": [28, 30, 27, 29],
                      "Tena": [26, 25, 27, 28],
                      "Macas": [24, 23, 25, 26]
                  }
    :return: Diccionario con los promedios por ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios


# Ejemplo de uso
datos_temperaturas = {
    "Puyo": [28, 30, 27, 29],
    "Tena": [26, 25, 27, 28],
    "Macas": [24, 23, 25, 26]
}

resultado = calcular_promedio_temperaturas(datos_temperaturas)
print("Promedio de temperaturas por ciudad:", resultado)
