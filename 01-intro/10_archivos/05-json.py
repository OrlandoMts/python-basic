import json
from pathlib import Path

productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 15.49},
    {"id": 3, "nombre": "Producto 3", "precio": 8.75},
    {"id": 4, "nombre": "Producto 4", "precio": 12.99},
    {"id": 5, "nombre": "Producto 5", "precio": 20.50}
]


data = json.dumps(productos)
archivo = Path("01-intro/10_archivos/productos.json")
# archivo.write_text(data)

# leer archivo json
data = archivo.read_text(encoding="utf-8")
print(data)

# Modificar json
productos = json.loads(data)
productos[1]["nombre"] = "chanchito feliz"
Path("01-intro/10_archivos/productos.json").write_text(json.dumps(productos))
