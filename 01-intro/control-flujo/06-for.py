for numero in range(0, 10):
    print(numero, numero * "*")


# for numero in range(10, 0, -1):
#     print(numero, numero * "*")

buscar = 30

for numero in range(10):
    print(numero)

    if numero == buscar:
        print("Encontrado", buscar)
        break

else:
    print("No Encontrado", buscar)
