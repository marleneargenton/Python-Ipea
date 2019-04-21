# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 13 - Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’ por ‘,’ em uma string. Exemplo: 1,000.54 por
# 1.000,54.


def subs_caracteres(x):
    y = list(x)
    for i in range(len(y)):
        if y[i] == ',':
            y[i] = '.'
        elif y[i] == '.':
                y[i] = ','
    return ''.join(y)


if __name__ == '__main__':
    n = input('digite um número com vírgulas e pontos: ')
    print('Os caracteres vírgulas e pontos de {} foram substituídos e resultaram em {}'.format(n, subs_caracteres(n)))
