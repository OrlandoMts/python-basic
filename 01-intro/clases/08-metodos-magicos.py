class Perro():
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Adios perro {self.nombre}")

    def __str__(self):
        return f"Clase Perro: Hola soy {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: guau")


mi_perro = Perro("Chanchito", 4)
# mi_perro.__
print(mi_perro.habla())
texto = str(mi_perro)
print(texto)
del mi_perro
