# Tarea: Trabajando con Diccionarios en Python
# Estudiante: Guido Villarroel
# Materia: Fundamentos de Programación
# Objetivo: Utilizar diccionarios en Python para representar información estructurada
# y realizar operaciones comunes.

# 1. Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Guido Villarroel",
    "edad": 22,
    "ciudad": "Puyo",
    "profesion": "Estudiante de Ingeniería"
}

# 2. Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"  # Cambio de ciudad

# 3. Agregar una nueva clave-valor (ejemplo: correo electrónico)
informacion_personal["email"] = "guido.villaroel@example.com"

# 4. Verificar si existe la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio agregado

# 5. Eliminar la clave "edad" porque no es necesaria
del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
