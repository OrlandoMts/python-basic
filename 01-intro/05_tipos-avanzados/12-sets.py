# Set significa grupo o conjunto
# Puede ser manipulada como las listas con append, remove, etc
# No admite duplicados
# No es ordenado
# No se puede acceder a un elemento concreto
# Se puede recorrer con un for

# definicion = {"definicion", "definicion", "definicion",
#               "definicion", "definicion", "definicion"}
# print(definicion)

primer = {1, 1, 2, 2, 3, 4, 5}

segundo = [3, 4, 6]
segundo = set(segundo)

print(primer | segundo)  # Hace una union de los sets
print(primer & segundo)  # Hace una interseccion de los sets
# Hace una diferencia de los sets (los que estan en el de la derecha y que tambien estan en la izquierda los quita. Manteniendo los de la izquierda y quitando los de la derecha  )
print(primer - segundo)
# Hace una diferencia simetrica de los sets (Elimina los que estan en ambos sets. Los que estan en uno de los sets y no en el otro los mantiene)
print(primer ^ segundo)
