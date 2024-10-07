try:
    n1 = int(input('Digite algo: '))
except Exception as e:
    print("Algo salio mal")
else:
    # Se ejecuta si no hay excepciones
    print("Todo salio bien")
finally:
    # Se ejecuta siempre, no importa si hay excepciones o no
    print("Fin del programa")
