from pathlib import Path

archivo = Path("01-intro/10_archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")

print(texto)

texto.insert(0, "hola mundo")
# write_text sustituye todo lo que hay en el archivo por lo que se le pasa en la funcion
archivo.write_text("\n".join(texto), "utf-8")
