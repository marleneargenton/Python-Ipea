# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 4 - Escreva um programa que corre os números de 1 a 50 e imprime. Mas, quando for múltiplo de três,
# imprima ‘Oops’, quando for múltiplo de 5 imprima ‘Doo’, quando for de ambos imprima ‘OopsDoo’.


def divisivel(inicio, fim):
    for i in range(inicio, fim + 1):

        # imprime 'OopsDoo' para os números divisíveis por 3 e 5 para o intervalo.
        if (i % 3 == 0) and (i % 5 == 0):
            print('{} - {}'.format(i, 'OopsDoo'))

        # imprime 'Oops' para os números divisíveis por 3 para o intervalo.
        elif i % 3 == 0:
            print('{} - {}'.format(i, 'Oops'))

        # imprime 'Doo' para os números divisíveis por 5 para o intervalo.
        elif i % 5 == 0:
            print('{} - {}'.format(i, 'Doo'))

        # imprime os demais números do intervalo.
        else:
            print('{} -'.format(i))


if __name__ == '__main__':
    x = 1
    y = 50
    divisivel(x, y)
