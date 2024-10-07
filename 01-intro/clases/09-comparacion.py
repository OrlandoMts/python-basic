class Coordenadas:

    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    # Verifica si dos objetos son iguales
    def __eq__(self, value: object) -> bool:
        return self.lat == value.lat and self.lon == value.lon

    # Not Equal
    def __ne__(self, value: object) -> bool:
        return self.lat != value.lat or self.lon != value.lon

    # Mayor  que
    def __lt__(self, value) -> bool:
        return self.lat + self.lon < value.lat + value.lon

    # Menor o igual que
    def __le__(self, value: object) -> bool:
        return self.lat + self.lon <= value.lat + value.lon


cord_1 = Coordenadas(20, 147)
cord_2 = Coordenadas(20, 145)

print(cord_1, cord_2)

# Al utilizar el metodo magico python ya lo reconoce, incluso si borro __ne__,
# al tener declarado __eq__ ya lo detecta
print(cord_1 == cord_2)
print("¿Es mayor? ", cord_1 <= cord_2)


# print(cord_1.__eq__(cord_2))
# print(cord_1.__ne__(cord_2))
