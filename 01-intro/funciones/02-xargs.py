# * convert params in iterable
def suma(*numeros):
    xd = 0
    for i in numeros:
        xd += i
    return xd


print(suma(3, 2, 1, 4, 5))
print(suma(3, 2))
