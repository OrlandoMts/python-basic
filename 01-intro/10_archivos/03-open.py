from io import open

# Ejemplo: escritura
# texto = "Hola mundo, esto es una prueba de escritura de archivos en Python"
# archivo = open("01-intro/10_archivos/archivo-open.txt", "w")
# archivo.write(texto)
# archivo.close()


# Ejemplo: lectura
# archivo = open("01-intro/10_archivos/archivo-open.txt", "r")
# texto = archivo.read()  # readlines()
# archivo.close()
# print(texto)

# with cierra los archivos de manera automatica
# with open("01-intro/10_archivos/archivo-open.txt", "r") as archivo:
#     print(archivo.readlines())

# Ejemplo: agregar contenido a un archivo
archivo = open("01-intro/10_archivos/archivo-open.txt", "a+", encoding="utf-8")
archivo.write("\nAgregando una nueva linea al archivo")
archivo.close()
