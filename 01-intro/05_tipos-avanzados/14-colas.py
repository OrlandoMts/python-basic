# LIFO Last In First Out

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo = pila.pop()
print(ultimo)

if not pila:
    print("pila vacia")
