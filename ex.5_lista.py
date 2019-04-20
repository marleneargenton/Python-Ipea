# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 5 - Escreva um programa que recebe uma letra e identifica se ela é vogal ou consoante.


def vogal(z):
    # a função verifica e imprime se a letra escolhida for uma vogal.
    vogais = ('a', 'e', 'i', 'o', 'u')
    if z.lower() in vogais:
        print('A letra {} é uma vogal.'.format(z))


def consoante(x):
    # a função verifica e imprime se a letra escolhida for uma consoante.
    consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z')
    if x.lower() in consoantes:
        print('A letra {} é uma consoante.'.format(x))


if __name__ == '__main__':
    l1 = input('\nInsira uma letra: ')
    vogal(l1)
    consoante(l1)
