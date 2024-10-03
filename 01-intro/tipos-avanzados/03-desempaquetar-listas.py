numeros = [1, 2, 3, 4, 5]
# primero, segundo, tercero, cuarto, quinto = numeros
primero, segundo, tercero, *otros = numeros
print(primero, segundo, tercero, otros)


numeros_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primero, *otros, penul, ultimo = numeros_2
print(primero, otros, penul, ultimo)
