numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)
punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)
# Desempaquetado
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)


# numeros[0] = 5 ERROR
listaNumeros = list(numeros)
listaNumeros[0] = 5
