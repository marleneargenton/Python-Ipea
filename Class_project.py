# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton
#
#
# 1. Objetivo: criar agentes e interações.

import random


class investors:
    # cria classe: Investidores
    def __init__(self, idinves):  # indicar um número único para cada investidor
        self.id = idinves
        self.balance = random.randrange(1, 20000)

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        # verificar recursos
        if self.balance <= amount:
            return False
        else:
            return True

    def deposit(self, amount):
        # depositar recursos
        self.balance -= amount
        return amount

    def withdraw(self, amount):
        # retirar recursos
        self.balance += amount
        return self.balance


class banks:
    # cria a classe: Bancos
    def __init__(self, idbank):  # indicar um número único para cada banco
        self.id = idbank
        self.balance = random.randrange(1, 100000)
        self.debt = 0
        self.credit = 0

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def check_funds(self, amount):
        # verificar recursos
        if self.balance <= amount:
            return False
        else:
            return amount

    def provisionar_credit(self, amount):
        self.credit += amount
        return

    def provisionar_debt(self, amount):
        self.debt += amount
        return

    def lending(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.credit += amount

    def receives_loan(self, amount):
        self.balance += amount
        self.balance -= self.debt
        return


class firms:
    # cria a classe Firmas
    def __init__(self, idfirms):  # indicar um número unico para cada empresa
        self.firms = idfirms
        self.balance = random.randrange(1, 10000)
        self.loanf = 0
        print('Agent has {} right now'.format(self.balance))

    def get_balance(self):
        return self.balance

    def check_funds(self):
        # verificar recursos
        if self.balance <= 0:
            return True
        else:
            return False

    def get_loan(self, amount):
        if self.balance <= 0:
            self.loanf -= amount
            self.balance += amount
        print('O valor do empréstimo é {} e seu saldo é {}'.format(amount, self.balance))

    def payment_loan(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.loanf += amount
        return self.loanf
        # print('Agent has {} fun right now'.format(self, amount))


if __name__ == '__main__':
    i = Investors(0)
    b = Banks(0)
    valor_investir = 10
    if i.check_funds(valor_investir):
        b.receive_deposit(i.deposit(valor_investir))
    print(i.balance)
    print(b.balance)
    f1 = Firms(0)
    f1.get_loan(100)
    print(f1.check_funds())
    f1.payment_loan(110)
    print(f1.check_funds())
    b1 = Banks(0)
    b1.receives_loan(f1.payment_loan(110))
    # self.balance += amount * .7
    # self.investor_pay(amount, investor)
