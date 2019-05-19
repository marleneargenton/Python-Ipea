# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton
#
#
# 1. Objetivo: criar agentes e interações. Agentes vão às compras e ganham satisfação. Lojas, com capacidade limitada
# recebem os clientes. Vendem satisfação. Análise da interação (simples) na medida em que se aumentam clientes.
# 2. Três classes distintas: Account, Shop, Agent
# 3. Account is simple. Inicia-se com self.balance = 0 e um
# número de registro self.registration = i
# 4. Account também deverá ter dois métodos:
#    4.1 Um que recebe recursos amount e acrescenta ao balanço:
#        self.balance += amount
#    4.2 E outro que retira recursos (amount) do balanço (e retorna a quantia retirada)
#        self.balance -= amount
# 5. Tanto as classes Agent, quanto Shop terão uma account
# 6. E precisarão de um número de registro i
# 7. Portanto, o primeiro método init de Agent e Shop deverá constar como uma instância da class Account
#    Como precisa de um parâmetro, o registro,
#    fica self.account = Account(i)
#    Notem que, para acessar o método depósito da account, será necessário algo como:
#    bob.account.deposit(quantia)
#    Do mesmo modo, na Shop
#    loja.account.deposit(quantia)
# 8. A class Shop dever´a ter ainda no seu init , três variáveis: capacity, fun, cost.
# 9. Todas três podem ser geradas, no momento de criação da instância, por meio do random.randrange(início, fim)
# 10. Crie métodos, de forma que:
#     10.1 Sempre que ocorrer uma visita de um cliente, diminua a capacidade por 1: self.capacity -= 1
#     10.2 Se a capacidade chegar a zero, retorne False. Senão, retorne True
#     10.3 Antes de permitir a visita e a compra, check se a capacidade permite
#     10.4 Por fim, note que, dado o acesso `as accounts do cliente e da loja, a transação não ocorre na classe, mas
#     fora dela.
# 11. O Agent tem pelo menos um m´etodo para acumular a fun, satisfação que recebe ao visitar cada Shop
# 12. Adicionalmente, pode-se ter um método que verifica se os recursos do Agent são suficientes para bancar o Shop.cost


import random


class Account:
    # cria classe: Account
    def __init__(self, i):
        self.balance = 0
        self.registration = i

    def get_balance(self):
        return self.balance

    # recebe recursos
    def deposit(self, amount):
        self.balance += amount

    # retira recursos
    def check_funds(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True

    # paga
    def pay(self, amount):
        self.balance -= amount
        return amount


class Shop:
    # cria a classe: Shop
    def __init__(self, idshop, i):
        self.account = Account(i)  # indicar um número único para cada shop
        self.id = idshop
        self.cost = random.randrange(1, 10)
        self.fun = random.randrange(1, 10)
        self.capacity = random.randrange(1, 10)

    def check_capacity(self):
        if self.capacity <= 0:
            return False
        else:
            return True

    def visit(self):
        if self.capacity > 0:
            self.capacity -= 1

    def sell(self, amount):
        if self.fun >= amount:
            self.fun -= amount
            return amount
        else:
            return False


class Agent:
    # cria a classe Agent
    def __init__(self, idagent, i):
        self.account = Account(i)  # indicar um número unico para cada shop
        self.fun = 0
        self.id = idagent
        # print('Agent has {} fun right now'.format(sel, fun))

    def get_fun(self, amount):
        self.fun += amount
        # print('Agent has {} fun right now'.format(self, amount))

    def check_funds(self, shop):
        if self.account.balance > shop.cost:
            return True
        else:
            return False


if __name__ == '__main__':
    a1 = Agent(0, 0)
    s1 = Shop(1, 1)
    # bb = Account('023')
    # print(bb.balance)
    # print(a1.account.balance)
    # print(s1.account.balance)
    # print(a1.account)
    a1.account.deposit(10)
    s1.account.deposit(s1.cost)
    a1.account.pay(s1.cost)
    print('O custo da loja {} é R${:.2f} e a fun é {}'.format(s1.id, s1.cost, s1.fun))
    print('O balanço corrente da loja {} é R${:.2f}'.format(s1.id, s1.account.balance))
    print('O agente tem R$ {:.2f} em caixa'.format(a1.account.balance))
