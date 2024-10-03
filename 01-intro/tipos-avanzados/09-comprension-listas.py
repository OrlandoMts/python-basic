usuarios = [["omontes", 4], ["oliver", 1], ["dogy", 3]]
# nombres = [expresion for item in items]


# Tranformada
nombres = [use[0] for use in usuarios]
# Filtrado con if
usuario = [use for use in usuarios if use[1] > 2]
# Filtrada y transformada
usuario = [use[0] for use in usuarios if use[1] > 2]
print(nombres)
print(usuario)
