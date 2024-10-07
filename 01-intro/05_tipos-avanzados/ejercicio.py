from pprint import pprint

# 1. Eliminar los espacios en blanco de una cadena y devolver una lista con los caracteres restantes


def cleanEmpty(text):
    result = [ch for ch in text if ch != " "]
    return result


# print(cleanEmpty("ho la xd  "))

# 2
def countItems(text):
    lista = [*text]
    result = {ch: lista.count(ch) for ch in lista}

    if " " in result:
        result.pop(" ")

    return result


# print(countItems("Hola mundooooo"))

# 3
dicA = {"a": 3, "b": 3, "c": 5, "d": 4}


def orderKeys(data):
    map_list = list(tuple(data.items()))
    map_list.sort(key=lambda item: item[1])
    return map_list


# print(orderKeys(dicA))

# 4
# tupA = [("a", 1), ("b", 2), ("f", 6), ("c", 6), ("d", 3), ("e", 5), ("f", 6)]
tupA = [("a", 1), ("b", 2), ("f", 6)]


def countItemRepeated(data):
    data.sort(key=lambda item: item[1])
    last_item = data[-1][1]
    result = []

    for item in data:
        if item[1] == last_item:
            result.append(item)

    return result


# print(countItemRepeated(tupA))
texto = "Este es un mensaje de prueba"

sin_espacios = cleanEmpty(texto)
contados = countItems(sin_espacios)
# pprint(contados, width=1)
ordenados = orderKeys(contados)
# print(ordenados)
repetidos = countItemRepeated(ordenados)
print(repetidos)
