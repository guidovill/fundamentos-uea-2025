# =========================================
#  Registro de Temperaturas Diarias (3D)
#  Estructura: temperaturas[ciudad][semana][día]
# =========================================

# Lista de ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Días de la semana
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

# Número de semanas
num_semanas = 2   # puedes aumentar si deseas

# =========================================
# Datos de ejemplo: 3 ciudades × 2 semanas × 7 días
# Quito
quito_sem1 = [14, 16, 15, 17, 18, 17, 16]
quito_sem2 = [15, 16, 16, 18, 19, 18, 17]

# Guayaquil
guayaquil_sem1 = [26, 27, 28, 29, 30, 30, 29]
guayaquil_sem2 = [27, 28, 29, 30, 31, 31, 30]

# Cuenca
cuenca_sem1 = [12, 13, 14, 15, 15, 14, 13]
cuenca_sem2 = [13, 14, 14, 15, 16, 15, 14]

# =========================================
# Construcción de la matriz 3D
temperaturas = [
    [quito_sem1, quito_sem2],             # Quito
    [guayaquil_sem1, guayaquil_sem2],     # Guayaquil
    [cuenca_sem1, cuenca_sem2]            # Cuenca
]

# =========================================
# Cálculo de promedios semanales por ciudad
for i_ciudad in range(len(ciudades)):
    nombre_ciudad = ciudades[i_ciudad]
    for i_sem in range(num_semanas):
        suma = 0
        for i_dia in range(len(dias)):
            suma += temperaturas[i_ciudad][i_sem][i_dia]
        promedio = suma / len(dias)
        print(f"{nombre_ciudad:10s} | Semana {i_sem+1} | Promedio: {promedio:.2f} °C")
