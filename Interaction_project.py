# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton

import random
import Class_project


def creation(y, n, d):
    x = list()
    for i in range(n):
        x.append(y(i, d))
    return x


def estrategia_investidor(r, p, b, amount):
    for s in range(len(p)):
        b1 = random.choice(b)
        r1 = random.choice(r)
        amount1 = random.choice(amount)
        if r1 >= 5.76:
            if p[s].check_funds(amount1):
                p[s].investor.deposit(b1[s].add_balance(amount1))
            return
        if r1 > 11.52:
            if b1[s].check_funds(amount1):
                b1[s].withdraw(p[s].withdraw(amount1))
        return


def estrategia_firmas(t, e, a, value):
    for d in range(len(e)):
        a1 = random.choice(a)
        value1 = random.choice(value)
        while t <= 11.52:
            if a1[d].check_funds(value1):
                a1[d].lending(e[d].get_loan(value1))
    return


def main(list_investors, list_banks, list_firms):
    random.shuffle(list_investors)
    random.shuffle(list_banks)
    random.shuffle(list_firms)
    return list_investors, list_banks, list_firms


if __name__ == '__main__':
    inv = [10]
    ban = [13]
    fir = [10]
    poup, banc, emp = main(inv, ban, fir)
    tax = [10, 3, 5, 9, 11, 6]
    am = [1000, 100, 300, 400, 10, 0]
    rem = [10, 3, 5, 9, 11, 6]
    valor = [1000, 100, 300, 400, 10, 0]
    print(estrategia_investidor(rem, ban, fir, valor))
    print(estrategia_firmas(tax, ban, fir, am))
