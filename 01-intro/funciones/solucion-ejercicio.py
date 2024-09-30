def no_space(text):
    new_text = ""

    for chart in text:
        if chart != " ":
            new_text += chart

    return new_text


def reverse(text):
    texto_al_reves = ""

    for chart in text:
        texto_al_reves = chart + texto_al_reves

    return texto_al_reves


def isPalindromo(text):
    texto = no_space(text)
    texto_al_reves = reverse(texto)
    return texto == texto_al_reves


print(isPalindromo("amo la paloma"))
