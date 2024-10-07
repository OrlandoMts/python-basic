# Es lo mismo que una lista pero no se pueden modificar
# Puedo crear mas tuplas a partir de una pero no puedes modificar las existentes
# Se define con corchetes

puntp = tuple([1, 2])  # Recibe cualquier cosa que sea iterable


def define_tuple():
    # Define un tuple con 3 elementos
    my_tuple = (1, 2, 3)

    # Imprime el tuple
    print(my_tuple)

    # Imprime el tipo de dato del tuple
    print(type(my_tuple))

    # Imprime la longitud del tuple
    print(len(my_tuple))

    # Imprime el elemento en la posición 0
    print(my_tuple[0])

    # Imprime el elemento en la posición 1
    print(my_tuple[1])

    # Imprime el elemento en la posición 2
    print(my_tuple[2])

    # Intenta modificar un elemento del tuple (dará error)
    try:
        my_tuple[0] = 10
    except TypeError:
        print("No se pueden modificar los elementos de un tuple")


# Llamar a la función
define_tuple()
