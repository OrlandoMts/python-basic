

class Perro:
    patas = 4

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice - Guau!")


mi_perro = Perro("Dogy", 5)
mi_perro.patas = 5
print(mi_perro.patas)
