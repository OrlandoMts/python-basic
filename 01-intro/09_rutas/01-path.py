from pathlib import Path

# r = row string
# Path(r"C:\Archivos de programa\mongo")
# # Para linux y mac
# Path("/usr/bin")  # Ruta absoulta
# Path()  # Crea ruta dependiendo en donde me encuntre
# Path.home()  # Obtiene la ruta del home
# Path("one/__init__.py")  # Ruta relativa


path = Path("hola-mundo/mi-archivo.py")
path.is_file()  # False
path.is_dir()  # False
path.exists()  # False

print(
    path.name,  # Nombre con extension
    path.stem,  # Nombre sin extension
    path.suffix,  # Extension
    path.parent,  # Directorio padre
    path.absolute()  # Ruta completa de donde se encuentra
)


path.with_name("chanchito.py")  # Cambia el nombre del archivo con su extension
path.with_suffix(".txt")  # Cambia la extension
path.with_stem("")  # Cambia el nombre sin extension
