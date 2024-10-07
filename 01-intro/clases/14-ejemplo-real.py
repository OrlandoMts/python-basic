class Model:
    table = False

    def __init__(self) -> None:
        if not self.table:
            print("Debes definir una tabla")

    def guardar(self) -> None:
        print(f"Guardando {self.table} en BBDD")

    @classmethod
    def buscar_por_id(cls, _id):
        print(f"Buscando por id {_id} en la {cls.table}")


class Usuario(Model):
    table = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(24)
