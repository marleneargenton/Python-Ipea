# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 6 - Escreva um programa que conte o número de letras de uma string.


def count_letters(txt):
    global i
    vogais = 0
    consoantes = 0

    # converte as letras para minúsculas
    txt = txt.lower()

    # removem espaços, linhas e símbolos de pontuação
    txt = txt.replace(' ', '')
    txt = txt.replace('\n', '')
    txt = txt.replace('.', '')
    txt = txt.replace('!', '')
    txt = txt.replace(',', '')
    txt = txt.replace(';', '')
    txt = txt.replace('á', 'a')
    txt = txt.replace('à', 'a')
    txt = txt.replace('ã', 'a')
    txt = txt.replace('é', 'e')
    txt = txt.replace('ê', 'e')
    txt = txt.replace('í', 'i')
    txt = txt.replace('ó', 'o')
    txt = txt.replace('ô', 'o')
    txt = txt.replace('ú', 'u')
    txt = txt.replace('ç', 'c')

    # conta o número de vogais e consoantes
    for i in txt:
        if i in 'aeiou':
            vogais = vogais + 1
        else:
            if i in 'bcdfghjklmnpqrstvwyxz':
                consoantes = consoantes + 1

    print('Vogais: {}'.format(vogais))
    print('Consoantes: {}'.format(consoantes))
    print('Total de letras: {} - {}'.format(len(txt), (vogais + consoantes)))


if __name__ == '__main__':
    t = str(input('digite uma string:'))
    count_letters(t)
