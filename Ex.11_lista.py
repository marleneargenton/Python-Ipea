# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 11 -  Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência de cada
# uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}.


def histogram(data):
    # transforma lista em um dicionário, em que os valores da lista são as 'keys' e a frequência os valores representam
    #  os 'values'.
    d = dict()
    for each in data:
        d[each] = d.get(each, 0) + 1
    return d


if __name__ == '__main__':
    num = [0, 0, 1, 1, 1, 2, 5]
    print(num)
    print(histogram(num))
