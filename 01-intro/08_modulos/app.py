
# Diferencias entre Módulo y Paquete
# El módulo apunta -> archivos
# El paquete apunta -> Carpetas (Se requiere crear un archivo __init__.py)


# from usuarios.acciones.utilidades import guardar, pagar_impuestos
# opcion 2: from usuarios import acciones
import usuarios.gestion
import usuarios.impuestos
from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios

pagar_impuestos()
# pagar_impuestos()

# Opcion 2
# acciones.guardar()

# print(dir(usuarios))
# print(usuarios.gestion.__name__)
# print(usuarios.__package__)
# print(usuarios.impuestos.__path__)
# print(usuarios.__file__)

print(__name__)
