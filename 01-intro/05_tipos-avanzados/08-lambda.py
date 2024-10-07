def ordena(elemento):
    """Function return element."""
    return elemento[1]


"""
	No requeri usar ordena, se puede usar key=lambda elemento: elemento[1]
	La estructura es: key=lambda parametro: contenido de la funcion (valor de retorno)
"""

usuarios2 = [["omontes", 4], ["oliver", 1], ["dogy", 3]]
usuarios2.sort(key=lambda elemento: elemento[1])
print(usuarios2)
