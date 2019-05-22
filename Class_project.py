# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton
#
#
# 1. Objetivo: criar agentes e interações.


import random


class Investors:
    # cria classe: Investidores
    def __init__(self, inves):  # indicar um número único para cada investidor
        self.registration = inves
        self.balance = 0

    def deposit(self, amount):
        # depositar recursos
        self.balance += amount

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        # verificar recursos
        if self.balance - amount <= 0:
            return False
        else:
            return True

    def withdraw(self, amount):
        # retirar recursos
        self.balance -= amount
        return self.balance


class Banks:
    # cria a classe: Bancos
    def __init__(self, idbank, n):  # indicar um número único para cada banco
        self.bank = n
        self.id = idbank
        self.balance = 10.000
        self.deposit = random.randrange(1, 1000)
        self.loan = random.randrange(1, 1000)

    def check_funds(self, amount):
        # verificar recursos
        if self.balance <= 0:
            return False
        else:
            return amount

    def receive_deposit(self, amount):
        self.balance += amount

    def investor_pay(self, amount):
        self.balance -= amount

    def lending(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return False

    def receive_loan(self, amount):
        self.balance += amount


class Firms:
    # cria a classe Firmas
    def __init__(self, idfirms, num):  # indicar um número unico para cada empresa
        self.firms = idfirms
        self.registration = num
        self.balance = 0
        print('Agent has {} right now'.format(self.balance))

    def get_loan(self, amount):
        self.balance += amount

    def check_funds(self):
        if self.balance > 0:
            return True
        else:
            return False

    def pay_loan(self, amount):
        self.balance -= amount
        # print('Agent has {} fun right now'.format(self, amount))


if __name__ == '__main__':
    print()
