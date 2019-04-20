# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 7 -  Escreva um programa que, dada uma lista de números [2, 34, 5, 6, 5, 4, 32] qualquer, retorne: o
# primeiro valor, o número de valores, o último valor, a soma, a média e a mediana. Obs. Para listas com tamanho
# ímpar, a mediana é o # valor do meio, quando ordenada (sorted()). Para listas pares, os dois valores do meio.


def first_value(x):
    # retorna o primeiro número.
    return x[0]


def num_value(y):
    # retorna o número de valores da lista.
    return len(y)


def last_value(z):
    # retorna o último valor da lista.
    return z[-1]


def sum_value(w):
    # soma os valores da lista.
    return sum(w)


def media(a):
    # calcula a média dos valores da lista.
    return sum(a)/len(a)


def mediana(b):
    # calcula a mediana dos valores da lista.
    b = sorted(b)
    y = len(b)
    centro = y//2
    if y % 2 == 1:
        return b[centro]
    else:
        return (b[centro - 1] + b[centro])/2


if __name__ == '__main__':
    n = [2, 34, 5, 6, 5, 4, 32]
    print('O primeiro valor da lista é: {}'.format(first_value(n)))
    print('A lista é composta por {} valores'. format(num_value(n)))
    print('O último valor da lista é: {}'.format(last_value(n)))
    print('A soma dos valores da lista é: {}'.format(sum_value(n)))
    print("A média dos valores da lista é: {:.2f}".format(media(n)))
    print('A mediana dos valores da lista é: {}'.format(mediana(n)))
