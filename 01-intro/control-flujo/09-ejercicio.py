print("""
        Bienvenidos a la calculadora
        Para salir escribe exit
        Las operaciones disponibles son: sum, mul, div, res
""")

first_number = input("Ingrese un numero: ")

while (first_number.lower() != 'exit'):
    result = 0
    operation = input("Ingrese la operacion: ").lower()
    second_number = input("Ingrese otro numero: ")
    if (operation != 'sum' and operation != 'mul' and operation != 'div' and operation != 'res'):
        print("Operacion no valida")
        continue

    if operation == 'sum':
        result = (float(first_number) + float(second_number))
    elif operation == 'mul':
        result = (float(first_number) * float(second_number))
    elif operation == 'div':
        result = (float(first_number) / float(second_number))
    else:
        result = (float(first_number) - float(second_number))

    print(f"El resultado es: {result}")
    first_number = input("Ingrese un numero: ")
