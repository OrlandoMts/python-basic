numeros_al_azar = [1, 3, 56, 8, 123, 42, 79, 46, 87, 56, 1, 3, 6, 9, 67, 23]

# numeros_al_azar.sort(reverse=True)

"""
	Devuelve una nueva lista, no afecta a la anterior
"""
numeros2 = sorted(numeros_al_azar, reverse=False)

print(numeros_al_azar)
print(numeros2)

# Ejemplo 2
usuarios = [[4, "omontes"], [1, "oliver"], [3, "dogy"]]
usuarios.sort()
print(usuarios)

# Ejemplo 3
nombres = ["omar", "dogy", "oliver"]
nombres.sort()
print(nombres)

# Ejemplo 4


def ordena(elemento):
    """Function return element."""
    return elemento[1]


usuarios2 = [["omontes", 4], ["oliver", 1], ["dogy", 3]]
# usuarios2.sort()
usuarios2.sort(key=ordena)
print(usuarios2)
