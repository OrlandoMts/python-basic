from pathlib import Path
from time import ctime

archivo = Path("01-intro/10_archivos/archivo-prueba.txt")
# print(archivo.exists())
# print(archivo.stat())


print(archivo.stat().st_atime)
print("acceso: ", ctime(archivo.stat().st_atime))
print("modificado el: ", ctime(archivo.stat().st_mtime))
print("fecha de creacion: ", ctime(archivo.stat().st_birthtime))
