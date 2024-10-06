
class Perro:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __habla(self):
        print(f"{self.__nombre} dice Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 4)


mi_perro = Perro.factory()
mi_perro.__habla()
print(mi_perro.get_nombre())
