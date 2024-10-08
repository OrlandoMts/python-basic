from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]


def load(p):
    # Importa paquetes y modulos de manera dinamica
    paquete = __import__(str(p).replace("/", "."))
    paquete.start()


list(map(load, paths))
