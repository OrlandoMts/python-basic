class Perro:
    # Constructor
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice - Guau!")


mi_perro = Perro("Dogy", 5)
mi_perro.habla()
