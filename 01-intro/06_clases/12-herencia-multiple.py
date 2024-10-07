class Animal:
    def comer(self) -> None:
        print("comiendo")

    def pasear(self) -> None:
        print("Paseando animales")


class Perro:
    def pasear(self) -> None:
        print("Paseando")


# Toma los metodos de la derecha hacia la izquierda
# Pero si existen dos metodos iguales, sustituira el
# de la derecha por el de la izquierda
class Chanchito(Perro, Animal):
    def programar(self) -> None:
        print("programando")


chan = Chanchito()
chan.pasear()
