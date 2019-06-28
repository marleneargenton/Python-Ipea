import random
import Interaction_project
import os
import matplotlib.pyplot as plt


def grafic(inv, ban, fir, rem, amount):
    file = 'results.csv'
    # cria listas para os resultados
    retlist = []
    deplist = []
    taxlist = []
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        f.write('depósitos; retiradas; remuneração\n')
        for i in range(len(inv)):
            inv, bank, firm = Interaction_project.main(inv[i], ban[i], fir[i])
            ban1 = random.choice(ban)
            rem1 = random.choice(rem)
            amount1 = random.choice(amount)
            if rem1 > 11.52:
                if ban1[i].check_funds(amount1):
                    ban1[i].withdraw(inv[i].withdraw(amount1))
            elif rem1 > 5.76:
                if inv[i].check_funds(amount1):
                    inv[i].deposit(ban1[i].add_balance(amount1))
            f.write('{};{};{};'.format(inv[i].balance, ban[i].balance, rem1))
            f.write('\n')
            retlist.append(inv[i].balance)
            deplist.append(ban[i].balance)
            taxlist.append(rem1)
    # cria o gráfico
    plt.plot(deplist, taxlist, color='#17a589', label='depósitos')
    plt.plot(retlist, taxlist, color='red', label='retiradas')
    plt.legend(loc='right', shadow=True)
    plt.xlabel('taxa de juros')
    plt.show()


if __name__ == '__main__':
    po = 20, 40, 60, 80, 120, 250, 350, 400, 600, 800, 900, 1000
    ba = 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
    fi = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200
    re = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20
    am = 100, 200, 300, 400, 1000, 1500, 2000, 3000, 5000, 6500, 9000, 10000
    grafic(po, ba, fi, re, am)
