# Python4ABMIpea  - Exercício 3
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton

# Cria-se o gráfico que demonstra o efeito sobre os depósitos e saques de investidores, a partir da simulação da
# alteração dos parâmetros da taxa de juros.

import random
import Interaction_project
import os
import matplotlib.pyplot as plt


def grafic(inv, ban, fir, rem, amount):
    file = 'results.csv'
    # cria listas para os resultados
    retlist = []
    deplist = []
    taxlist1 = []
    taxlist2 = []
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        f.write('depósitos; retiradas; remuneração\n')
        for i in range(len(inv)):
            invlist, banklist, firmlist = Interaction_project.main(inv[i], ban[i], fir[i])
            ban1 = random.choice(banklist)
            rem1 = random.choice(rem)
            amount1 = random.choice(amount)
            if rem1 > 11.52:
                if ban1.check_funds(amount1) > 0:
                    ban1.withdraw(invlist[i].withdraw(amount1))
                    retlist.append(amount1)
                    taxlist1.append(rem1)
            elif rem1 > 5.76:
                if invlist[i].check_funds(amount1) > 0:
                    invlist[i].deposit(ban1.add_balance(amount1))
                    deplist.append(amount1)
                    taxlist2.append(rem1)
            f.write('{};{};{};'.format(invlist[i].deposit, invlist[i].withdraw, rem1))
            f.write('\n')
    # cria o gráfico
    plt.plot(taxlist2, deplist, color='#17a589', label='depósitos')
    plt.plot(taxlist1, retlist, color='red', label='retiradas')
    plt.legend(loc='center', shadow=True)
    plt.xlabel('taxa de juros')
    plt.show()
    return deplist, retlist


if __name__ == '__main__':
    po = [20, 40, 60, 80, 120, 250, 350, 400, 600, 800, 900, 1000]
    ba = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
    fi = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
    re = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    am = [1100, 2200, 3300, 4400, 6000, 8500, 10000, 13000, 15000, 16500, 19000, 21000]
    dl, rl = grafic(po, ba, fi, re, am)
