from pathlib import Path
from zipfile import ZipFile


# with ZipFile("01-intro/10_archivos/comprimidos.zip", "w") as zip:
#     for path in Path("01-intro/10_archivos").rglob("*.*"):
#         if str(path) != "01-intro\\10_archivos\\comprimidos.zip":
#             print(path)
#             zip.write(path)

with ZipFile("01-intro/10_archivos/comprimidos.zip", "r") as zip:
    print(zip.namelist())
    info = zip.getinfo("01-intro/10_archivos/productos.json")
    print(info)
    zip.extractall("01-intro/10_archivos/descomprimido")
