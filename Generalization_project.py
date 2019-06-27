import random
import Interaction_project
import os
import matplotlib.pyplot as plt

# print([i.balance for i in inv])
# print([i.balance for i in b])
# print([i.balance for i in firm])


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
        for i in inv:
            inv, ban, fir, = Interaction_project.main(inv[i], ban[i], fir[i])
            if (rem > 11.52) in range(len(rem)):
                if i.check_funds(amount):
                    i.withdraw(i.withdraw(amount))
            elif rem > 5.76:
                if i.check_funds(amount):
                    i.deposit(i.add_balance(amount))
            f.write('{};{};{};'.format(amount, -amount, rem))
            f.write('\n')
            retlist.append(amount)
            deplist.append(-amount)
            taxlist.append(rem)
    # cria o gráfico
    plt.plot(deplist, taxlist, color='#17a589', label='depósitos')
    plt.plot(retlist, taxlist, color='red', label='retiradas')
    plt.legend(loc='right', shadow=True)
    plt.xlabel('taxa de juros')
    plt.show()


if __name__ == '__main__':
    po = [20, 40, 60, 80, 120, 250, 350, 400, 600, 800, 900, 1000]
    ba = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
    fi = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
    re = list(range(1, 19 + 1))
    am = list(range(100, 1000 + 1))
    grafic(po, ba, fi, re, am)
