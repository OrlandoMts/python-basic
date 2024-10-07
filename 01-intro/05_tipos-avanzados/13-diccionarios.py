punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
punto["z"] = 45
print(punto)
print(punto.get("x"))
# aunque no existe lo considera porque tiene el 97 como por defecto
print(punto.get("a", 97))
del punto["x"]
print(punto)
punto["x"] = 25
print(punto)
print(len(punto))
print(punto.keys())

if "a" in punto:
    print(punto["a"])
print(punto.values())
print("**********************")
for valor in punto.items():
    print(valor)

print("**********************")
print("Desempaquetado")
for llave, valor in punto.items():
    print(llave, valor)


print("**********************")
usuarios = [
    {"curp": 'MOMOA981038HNCX01', "nombre": "Daniel", "edad": 26},
    {"curp": 'MOMOA981038HNCX01', "nombre": "Aylin", "edad": 22},
    {"curp": 'MOMOA981038HNCX01', "nombre": "Sergio", "edad": 50},
]

print(usuarios)
