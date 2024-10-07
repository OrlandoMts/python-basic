def isPalindromo(text):
    newStr = text.replace(" ", "").lower()
    reverseStr = newStr[::-1]

    return True if reverseStr == newStr else False


print(isPalindromo(" *   H ola como estas ?    "))
print(isPalindromo("Arroz"))
print(isPalindromo("oso"))
print(isPalindromo("Amo la paloma"))
