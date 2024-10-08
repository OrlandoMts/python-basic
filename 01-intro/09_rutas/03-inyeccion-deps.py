import usuario  # NO existe, es de ejemplo


class Perro:
    def __init__(self, Correa) -> None:
        self.correa = Correa()


# Sin DI
def guardar():
    usuario.guardar()


# Con DI
def guardar_2(entidad):
    entidad.guardar()
