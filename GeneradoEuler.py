from tqdm.auto import tqdm


def factorial(n=0):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    return resultado


def sumaEuler(limite=0):
    suma = 0
    for i in tqdm(range(limite)):
        suma += 1/factorial(i)
    return suma


print('\n\tGenerador de número Euler\n')
limite_superior = int(input('Ingrese múmero de veces a realizar la opreción: '))
print(sumaEuler(limite_superior))
