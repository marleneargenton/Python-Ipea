# Python4ABMIpea  - Exercício 3
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton

# No segundo módulo, são importadas as classes e definidas as funções para:
# 1. criação das listas para Bancos, Firmas e Investidores:
#    Faz-se um loop utilizando n, i, append às listas  e retorna
# 2. estratégias dos investidores, que depositam recursos nos Bancos, se a taxa de juros alcança um parâmetro
# pré-definido, ou
#  realizam retirada de seus recursos, caso identifiquem risco de liquidez das instituições financeiras, mediante o
#  oferecimento de uma remuneração maior, cujo parâmetro foi pré-definido, que a praticada pelo mercado financeiro.
# 3. estratégias de firmas, que contraem  empréstimos, a partir de um determinado patamar de taxa de juros.


import random
from Class_project import Banks, Investors, Firms


def creation(x, n):
    # essa função pode ser utilizada por investidores, bancos e firmas, pois o primeiro argumento é uma classe.
    ag = list()
    for i in range(n):
        ag.append(x(i))
        i += 1
    return ag


def estrategia_investidor(p, b):
    # define a estratégia dos investidores dados os parâmetros de taxas min 5.76% a.a e a partir de 11.52% a.a
    r = list(range(1, 20))
    amount = list(range(1, 1001))
    for s in p:
        b1 = random.choice(b)
        r1 = random.choice(r)
        amount1 = random.choice(amount)
        if r1 > 11.52:
            if b1.check_funds(amount1):
                b1.withdraw(s.withdraw(amount1))
                print('retirada', -amount1, 'remuneração', r1)
        elif r1 > 5.76:
            if s.check_funds(amount1):
                s.deposit(b1.add_balance(amount1))
                print('depósito', amount1, 'remuneração', r1)


def estrategia_firmas(e, a):
    # define a estratégia das empresas considerando o parâmetro de taxa de abaixo de 11.52% a.a
    t = list(range(5, 21))
    value = list(range(1, 1001))
    for d in e:
        a1 = random.choice(a)
        t1 = random.choice(t)
        value1 = random.choice(value)
        if t1 < 11.52:
            if a1.check_funds(value1):
                a1.lending(d.get_loan(value1))
                print('empréstimo', value1, 'taxa', t1)


def main(p, b, f):
    # cria lista
    ivlist = creation(Investors, p)
    banlist = creation(Banks, b)
    firlist = creation(Firms, f)
    estrategia_investidor(ivlist, banlist)
    estrategia_firmas(firlist, banlist)
    return ivlist, banlist, firlist


if __name__ == '__main__':
    iv = 300
    ban = 10
    fir = 200
    investor, bank, firms = main(iv, ban, fir)
