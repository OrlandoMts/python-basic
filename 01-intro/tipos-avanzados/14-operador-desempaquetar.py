lista = [1, 2, 3, 4]
print(*lista)  # 1 2 3 4

tupla = (5, 6, 7, 8)
print(*tupla)  # 5 6 7 8


lista2 = [9, 10, 11, 12]
combinada = ["hola", *lista, 156, *lista2, "xd"]
print(combinada)

print("********")
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15, "z": "mundo"}
nuevoPunto = {**punto1, **punto2, "nuevo": "valor"}
print(nuevoPunto)
