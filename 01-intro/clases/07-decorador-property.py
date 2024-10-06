class Perro:
    def __init__(self, nombre):
        self.nombres = nombre

    @property
    def nombres(self):
        print("Pasando por getter")
        return self.__nombre

    @nombres.setter
    def nombres(self, nombre):
        print("Pasando por setter")

        if nombre.strip():
            self.__nombre = nombre

        return


mi_perro = Perro("Chanchito")
print(mi_perro.nombres)
