try:
    n1 = int(input('Digite algo: '))
except Exception as e:
    print("Algo salio mal")
    print('Erro: {}'.format(e))
