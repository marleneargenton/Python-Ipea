# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 3 - Altere o programa do exercício 2 para que o usuário possa entrar com o número máximo de estrelas.


def draw(x):
    # inicia o padrão com 1 asterisco até o máximo de asterisco escolhido pelo operador.
    for i in range(x + 1):
        print(' *' * i)
    # reduz o padrão do número máximo escolhido pelo operador até 1 asterisco, completando o padrão.
    for i in reversed(range(x)):
        print(' *' * i)


if __name__ == '__main__':
    num = int(input('digite o número máximo de asterisco: '))
    draw(num)
