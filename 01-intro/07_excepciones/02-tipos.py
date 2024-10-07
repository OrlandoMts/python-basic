try:
    n1 = int(input('Digite algo: '))
    sadada
except ValueError as e:
    print("Algo salio mal")
    print('Erro: {}'.format(e))
except NameError as e:
    print("Algo salio mal")
    print('Erro: {}'.format(e))
