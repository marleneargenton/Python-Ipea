# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 9 - Escreva uma função que faz um loop as keys de um dicionário. Se as keys forem vogais, eleve o valor
# ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’.


def vogais_quadrado(d):
    for k in d.keys():

        # cria um loop para identificar as keys que são vogais.
        if k in 'aeiou':
            d.update({k: d[k] ** 2})

        # para as keys não vogais, o valor é alterado para zero.
        else:
            d.update({k: 0})
    return d


if __name__ == '__main__':
    d1 = {'a': 3, 'd': 5, 'u': 2}
    d2 = {'d': 6, 'f': 4}
    d3 = {'i': 3, 'c': 2, 'f': 1}
    print(vogais_quadrado(d1))
    print(vogais_quadrado(d2))
    print(vogais_quadrado(d3))
