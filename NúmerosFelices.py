def convDigitos(num=0):
    lista_numero = []
    for digito in num:
        lista_numero.append(int(digito))
    return lista_numero


def sumCuadrados(lista_numero):
    suma = 0
    for i in lista_numero:
        suma += i**2
    return suma


print('\n\tEs su número feliz?\n')
num = input('Ingrese un número: ')

res_previos = []
digitos = convDigitos(num)
suma = 0

while True:
    suma = sumCuadrados(digitos)
    # print(suma)
    if suma == 1:
        print('\nSu número es Feliz :)')
        break
    elif suma in res_previos:
        print('\nSu número no es Feliz :(')
        break
    else:
        digitos = convDigitos(str(suma))
        res_previos.append(suma)
        # print(res_previos)
