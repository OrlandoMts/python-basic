from pathlib import Path

path = Path(r"01-intro/09_rutas")
# path.mkdir()
# path.exists()
# path.rmdir()  # Debe estar vacio el folder
# path.rename()  # Cambia el nombre al directorio

print(path.iterdir())
for p in path.iterdir():
    print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos_2 = [p for p in path.glob("01-*.py")]
archivos_3 = [p for p in path.rglob("*.py")]  # Recursive
print("***")
print(archivos_3)
