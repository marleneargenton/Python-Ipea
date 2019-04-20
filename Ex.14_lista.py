# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton

# Exercício 14 - Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma vez do
# parágrafo fornecido pelo usuário.


def check_alfabeto(txt):
    # verificar se todas as letras do alfabeto estão presentes no texto digitado pelo operador.
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for char in alfabeto:
        if char not in txt.lower():
            return False

    return True


if __name__ == '__main__':
    t = str(input('\ndigite um texto: '))
    if check_alfabeto(t) is True:
        print('O texto digitado apresenta todas as letras do alfabeto')
    else:
        print('O texto digitado não apresenta todas as letras do alfabeto')
