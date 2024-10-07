usuarios = [["omontes", 4], ["oliver", 1], ["dogy", 3]]
nombres = list(map(lambda usuario: usuario[0], usuarios))
mayores = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)
print(mayores[1])
