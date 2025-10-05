# archivo: trabajo_archivos_texto.py
# Tema: Lectura y escritura de archivos de texto en Python
# Instrucciones cumplidas:
# - Crear my_notes.txt y escribir al menos 3 líneas (write)
# - Leer línea por línea con readline()
# - Mostrar cada línea en consola
# - Cerrar los archivos al finalizar

RUTA_ARCHIVO = "my_notes.txt"

# ---------------------------
# 1) ESCRITURA DEL ARCHIVO
# ---------------------------
try:
    # Abrimos en modo escritura ("w") — si no existe, lo crea; si existe, sobrescribe
    f_out = open(RUTA_ARCHIVO, "w", encoding="utf-8")
    # Escribimos 3+ líneas de notas personales (puede editar el contenido si desea)
    f_out.write("Nota 1: Repasar lectura y escritura de archivos en Python.\n")
    f_out.write("Nota 2: Practicar readline() y diferenciarlo de read().\n")
    f_out.write("Nota 3: Subir el código al repositorio de GitHub de la asignatura.\n")
    # Puede añadir más líneas si lo desea:
    f_out.write("Nota 4 (opcional): Usar encoding='utf-8' para tildes y eñes.\n")
finally:
    # Cerrar el archivo de salida
    f_out.close()

# ---------------------------
# 2) LECTURA LÍNEA POR LÍNEA
# ---------------------------
try:
    # Abrimos en modo lectura ("r")
    f_in = open(RUTA_ARCHIVO, "r", encoding="utf-8")

    print("Contenido de", RUTA_ARCHIVO, "(lectura línea por línea):\n")

    while True:
        linea = f_in.readline()   # lee una línea (incluye el salto de línea)
        if not linea:             # cuando no hay más líneas, readline() devuelve ''
            break
        print(linea.rstrip("\n")) # mostramos la línea sin salto de línea final
finally:
    # Cerrar el archivo de entrada
    f_in.close()

# ---------------------------
# 3) VERIFICACIÓN (opcional)
# ---------------------------
# Confirmamos que los archivos quedaron cerrados
print("\nArchivo de escritura cerrado:", f_out.closed)
print("Archivo de lectura cerrado:", f_in.closed)
