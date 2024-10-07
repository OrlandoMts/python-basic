class Animal:
    def comer(self) -> None:
        print("comiendo")


class Perro(Animal):
    def pasear(self) -> None:
        print("Paseando")


class Chanchito(Perro):
    def programar(self) -> None:
        print("programando")


chan = Chanchito()
chan.comer()
