# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton
#
# Outro módulo, import as classes e contém algumas funções:
# Uma para criar os agentes e as lojas, a partir de um número n e controla o id específico i
# Criam-se listas
# Faz-se um loop utilizando n, i, append às listas, retorna
# Outra função, acessa as contas dos agentes e deposita recursos, por exemplo:
#   a[i].account.deposit(random.randrange(10, 50))
# Por fim, talvez a função ao mais difícil, a interação entre agentes e lojas.
# Por exemplo, para todos os agentes, escolhe-se uma loja aleatória:
#   random.choice(listalojas)
# então, verifica-se a capacidade da loja, os recursos do agente, faz-se a visita, computa-se o gasto e adquire-se
# satisfação! Por exemplo:
#   s1.account.deposit(a[i].account.pay(s1.cost))
#   a[i].get fun(s1.fun)
# Por fim, escreva uma função que tire a média da satisfação do agente, do custo das lojas e das contas.

from Accounts import Agent, Shop
import random


def creation(f, n, d):
    # essa função pode ser utilizada por agentes e lojas pois o primeiro argumento é a classe
    x = list()
    for i in range(n):
        x.append(f(i, d))
        i += 1
    return x


def salaries(a):
    # acessa a conta dos agentes e deposita recursos
    for i in range(len(a)):
        a[i].account.deposit(random.randrange(10, 50))


def interact(a, s):
    # verifica-se a capacidade da loja, os recursos do agente, faz-se a visita, computa-se o gasto e adquire-se
    # satisfação
    for i in range(len(a)):
        s1 = random.choice(s)
        if a[i].check_funds(s1) and s1.check_capacity():
            s1.visit()
            s1.account.deposit(a[i].account.pay(s1.cost))
            a[i].get_fun(s1.fun)


def averaging(a, s):
    # essa função calcula a média da satisfação do agente, do custo das lojas e das contas das lojas e dos agentes.
    avg_fun = sum([i.fun for i in a]) / len(a)
    avg_cost = sum([i.cost for i in s]) / len(s)
    avg_shop = sum([i.account.balance for i in s]) / len(s)
    avg_agent = sum([i.account.balance for i in a]) / len(a)
    print('A média da satisfação é {:.2f}\nA média do custo das lojas é {:.2f}\nA média das contas das lojas e dos '
          'agentes são {:.2f} e {:.2f}\n'.format(avg_fun, avg_cost, avg_shop, avg_agent))


def main(a, s):
    # cria listas
    list_a = creation(Agent, a, 1)
    list_s = creation(Shop, a, s + 1)
    # mistura as listas
    random.shuffle(list_a)
    random.shuffle(list_s)
    salaries(list_a)
    interact(list_a, list_s)
    return list_a, list_s


if __name__ == '__main__':
    ag = 10
    sh = 10
    agents, shops = main(ag, sh)
    print(averaging(agents, shops))
