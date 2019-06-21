# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton

import random
import Class_project

# criar lista
# calcular rentabilidade da aplicação financeira
# calcular rentabilidade dos emprestimos
# interação


import Class_project


def creation(f, n, d):
    x = list()
    for i in range(n):
        x.append(f(i, d))
    return x


def estrategia_investidor(rem, investidor, banco, amount):
    for i in range(investidor):
        if rem >= 5.76:
            (i).check_funds and (i).deposit(amount):
            (banco).receive_deposit(amount)
            (banco).check_funds and (banco).withdraw()
        return


def estrategia_firmas(taxa, firmas, bank, value):
    for i in range(firmas):
        if taxa <= 11.52:
            [firmas].get_loan().bank.check_funds and bank.lending(value)
        else:
            continue
    return


def main(list_i, list_b, list_f):
    random.shuffle(list_i)
    random.shuffle(list_b)
    random.shuffle(list_f)
    #renta(list_b)
    #interact(list_i, list_b, list_f)
    return list_i, list_b, list_f


if __name__ == '__main__':
    i = [10]
    b = [13]
    f = [10]
    Investors, Banks, Firms = main(i, b, f)
    remuneracao =[ 5, 8, 10, 3, 7]
    valor = [100, 200, 300, 400, 500]
    print(estrategia_investidor(remuneração,valor))