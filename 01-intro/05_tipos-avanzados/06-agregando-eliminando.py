mascotas = ["pelusa", "oliver", "dogy", "lila", "pulga", "lila"]
mascotas.insert(1, "melvin")
mascotas.append("chanchito feliz")  # lo agrega al final
print(mascotas)

# va el elemento, NO el indice. Elimina la primer referencia
mascotas.remove("lila")
mascotas.pop()  # elimina el ultimo elemento
mascotas.pop(2)  # elimina el elemento de la posicion
# del mascotas[0] # otra opcion
print(mascotas)

mascotas.clear()
print(mascotas)
