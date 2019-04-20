# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton

# Exercício 2 - Escreva um programa que imprima o seguinte padrão.

#  *
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *


n = 10  # define o número de asterisco.

for i in range(n + 1):
    # inicia o padrão com 1 asterisco até o máximo de 5 asterisco.
    if i <= int(n / 2):
        print(' *' * i)
    # define o número de espaços em branco e reduz o padrão de 5 até 1 asterisco.
    if i > int(n / 2):
        espacos = n - i
        print(' *' * espacos)
