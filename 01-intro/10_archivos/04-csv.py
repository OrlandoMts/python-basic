import csv
import os

# escribir
# with open("01-intro/10_archivos/archivo.csv", "w", encoding="utf-8") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["nombre", "apellido", "edad",])
#     writer.writerow(["Orlando", "Montes", 26,])
#     writer.writerow(["Matias", "Montes", 5,])
#     writer.writerow(["Clara", "Rios", 29,])


# leer
# with open("01-intro/10_archivos/archivo.csv", "r", encoding="utf-8") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for fila in reader:
#         print(fila)


# actualizar csv
with open("01-intro/10_archivos/archivo.csv", "r", encoding="utf-8", newline="") as r, open("01-intro/10_archivos/archivo_temporal.csv", "w", encoding="utf-8", newline="") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        print(linea)
        if linea[0] == "Orlando":
            writer.writerow(["Orlando", "Montes", 27])
        else:
            writer.writerow(linea)

os.remove("01-intro/10_archivos/archivo.csv")
os.rename("01-intro/10_archivos/archivo_temporal.csv",
          "01-intro/10_archivos/archivo.csv")
