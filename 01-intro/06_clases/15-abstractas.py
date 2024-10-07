from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    # Propiedad abstracta
    def table(self):
        pass

    @abstractmethod
    def guardar(self) -> None:
        pass
        # print(f"Guardando {self.table} en BBDD")

    @classmethod
    def buscar_por_id(cls, _id):
        print(f"Buscando por id {_id} en la {cls.table}")


class Usuario(Model):
    table = "Usuario"

    def guardar(self) -> None:
        print(f"Guardando {self.table} en BBDD")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(24)
