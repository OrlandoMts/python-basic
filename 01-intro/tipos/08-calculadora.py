num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

num_1 = int(num_1)
num_2 = int(num_2)

sum = num_1 + num_2
res = num_1 - num_2
div = num_1 / num_2
mul = num_1 * num_2

response = f"""
        Para los numeros {num_1} y {num_2}:
        La suma es: {sum}, La resta es: {res}, La division es: {div}, La multiplicacion es: {mul}
"""


# print(response.format(num_1=num_1, num_2=num_2))
print(response)
