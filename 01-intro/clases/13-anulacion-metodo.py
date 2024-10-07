class Ave:

    def __init__(self) -> None:
        self.volador = True

    def vuela(self):
        print("Vuela ave")


class Pato(Ave):

    def __init__(self) -> None:
        super().__init__()
        super().volador = False
        self.nadador = True

    def vuela(self):
        super().vuela()
        print("vuela pato")


pato = Pato()
pato.vuela()
print(pato.volador, pato.volador)
