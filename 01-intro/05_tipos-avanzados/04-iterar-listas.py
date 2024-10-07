mascotas = ["pelusa", "oliver", "dogy", "lila"]

# for masc in mascotas:
#     print(masc)


for masc in enumerate(mascotas):
    # print(masc)
    print(masc[1])


# Desempaquetado
for indice, masc in enumerate(mascotas):
    print(indice, masc)
