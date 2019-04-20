# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton

# Exercício 1 - Escreva um programa que ache os números divisíveis por 7 e por 13, entre o seu ano de nascimento e 2701.


def print_anos(ano_nasc, ano_fim):
    div_7 = []
    div_13 = []
    div_7_13 = []



    for i in range(ano_nasc, ano_fim + 1):
        # inclui na lista os números divisíveis por 7 para o período.
        if i % 7 == 0:
            div_7.append(i)

        # inclui na lista os números divisíveis por 13 para o período.
        if i % 13 == 0:
            div_13.append(i)

        # inclui na lista os números divisíveis por 7 e por 13 para o período.
        if (i % 7 == 0) and (i % 13 == 0):
            div_7_13.append(i)

    print('Os números divisíveis por 7 são: {}'.format(div_7))
    print('Os números divisíveis por 13 são: {}'.format(div_13))
    print('Os números divisíveis por 7 e por 13 são: {}'.format(div_7_13))


if __name__ == '__main__':
    x = 1971
    y = 2701
    print_anos(x, y)
