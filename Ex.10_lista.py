# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 10 - Escreva uma função que retorna os máximos e mínimos de um dicionário.


def num_maximo(x):
    # calcula e retorna o valor máximo do dicionário.
    maximo = max(x, key=x.get)
    return x[maximo]


def num_minimo(y):
    # calcula e retorna o valor mínimo do dicionário.
    minimo = min(y, key=y.get)
    return y[minimo]


if __name__ == '__main__':
    d1 = {'a': 5, 'b': 78, 'c': 9}
    d2 = {'a': 27, 'f': 3, 'w': 13}
    print(d1)
    print(d2)
    print('O valor máximo do dicionário é: ', num_maximo(d1))
    print('O valor mínimo do dicionário é: ', num_minimo(d1))
    print('O valor máximo do dicionário é: ', num_maximo(d2))
    print('O valor mínimo do dicionário é: ', num_minimo(d2))
