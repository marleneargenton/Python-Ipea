# Python4ABMIpea  - Exercício 3
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton

# Outro módulo, import as classes e contém algumas funções:
# criam-se listas para bancos, firmas e invetidores:
# Faz-se um loop utilizando n, i, append às listas, retorna
# Outra função, define as estratégias dos investidores, que depositando recursos nos Bancos, quando a taxa de juros
# alcança um parâmetro pré-definido, ou realizam retirada de seus recursos, caso identifiquem risco de liquidez das
# instituições financeiras, ou oferecerem uma remuneração maior que a oferecida, normalmente, pelo mercado.
# Por fim, a interação entre bancos e firmas, definida pela estratégias de firmas na busca de empréstimos, que a partir
# de um determinado patamar de taxa optam por contrair o empréstimo.


import random
from Class_project import Banks, Investors, Firms


def creation_investors(p, n):
    #cria a lista de investidores
    invlist = list()
    for i in range(n):
        invlist.append(p(i))
        i += 1
    return invlist


def creation_banks(b, y):
    #cria a lista de bancos
    banklist = list()
    for i in range(y):
        banklist.append(b(i))
        i+=1
    return banklist


def creation_firms(f, w):
    # cria a lista de firmas
    firmlist = list()
    for i in range(w):
        firmlist.append(f(i))
        i += 1
    return firmlist


def estrategia_investidor(r, p, b, amount):
    # define a estratégia dos investidores dados os parâmetros de taxas min 5.76% a.a e máx de 11.52% a.a
    b1 = random.choice(b)
    r1 = random.choice(r)
    amount1 = random.choice(amount)
    for s in p:
        if r1 > 5.76:
            if s.check_funds(amount1):
                s.deposit(b1.add_balance(amount1))
            return
        if r1 > 11.52:
            if b1.bank.check_funds(amount1):
                b1.withdraw(s.withdraw(amount1))
            return


def estrategia_firmas(t, e, a, value):
    # define a estratégia das empresas considerando o parâmetro de taxa de abaixo de 11.52% a.a
    a1 = random.choice(a)
    t1 = random.choice(t)
    value1 = random.choice(value)
    for d in e:
        while t1 < 11.52:
            if a1.check_funds(value1):
                a1.lending(d.get_loan(value1))
        return


if __name__ == '__main__':
    ivlist = creation_investors(Investors, 200)
    banlist = creation_banks(Banks, 5)
    firlist = creation_firms(Firms, 16)
    tax = [10, 3, 5, 19]
    am = [1000, 100, 300, 400]
    rem = [10, 13, 5, 9]
    valor = [1000, 100, 300, 400]
    #print(estrategia_investidor(rem, ivlist, banlist, valor))
    print(estrategia_firmas(tax, firlist, banlist, am))
    #print(creation_banks(Banks, 5))
    #print(creation_firms(Firms, 20))
    #print(creation_investors(Investors, 30))