animal = "chanchito feliz"
animal2 = "   chanchito feliz 2    "

print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())

print(animal2.strip().capitalize())
print(animal.find("fe"))  # devuelve la posicion del caracter
print(animal.find("z"))  # devuelve -1 si no encuentra el caracter

# print(animal.replace("chanchito", "gato"))
print(animal.replace("i", "x"))
print("fe" in animal)  # devuelve True/False si encuentra el caracter
print("fe" not in animal)
