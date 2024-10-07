
class Perro:
    patas = 4

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 4)


Perro.habla()


mi_perro = Perro("Chanchito", 5)
# mi_perro.habla()

perro1 = Perro("Dogy", 2)
perro2 = Perro.factory()
print(perro2.nombre, perro2.edad, perro2.patas)
