# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 12 = Escreva uma função que liste todos os números primos até 200. Utilize a divisão modular (%).


def prime(x, y):
    lista = []
    primos = []
    aux = 0

    # cria a lista de números do intervalo selecionado.

    for n in range(x, y + 1):
        lista.append(n)

    # identifica os números não primos, ou seja, aqueles que são divisíveis por mais de dois números dentro do
    # intervalo escolhido selecionado.

    for n in lista:
        for d in range(2, n):
            if n % d == 0:
                aux = 0
                break

        # identifica os números primos e cria lista de números primos.

        if aux == 1:
            primos.append(n)
        aux = 1
    print('Os números primos até 200 são: {}'.format(primos))


if __name__ == '__main__':
    a = 1
    b = 200
    prime(a, b)
