# Ingresar productos dentro de una categoria
class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"El producto - { self.nombre } cuesta $ { self.precio }"


class Categoria:
    productos = []

    def __init__(self, nombre, productos) -> None:
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto) -> None:
        self.productos.append(producto)

    def imprimir(self) -> None:
        for item in self.productos:
            print(item)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("bicicleta", 500)
balon = Producto("balon", 900)
jersey = Producto("jersey", 2000)

deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(balon)
deportes.imprimir()
