import random
from Class_project import Firms, Banks
from Interaction_project import creation_banks, creation_firms
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    taxalist = []
    valorlist = []
    file = 'results.csv'
    # cria listas para os resultados
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        f.write('n_banks; n_investors; taxas de juros; valores de empréstimos\n')
    banlist = creation_banks(Banks, 5)
    firlist = creation_firms(Firms, 100)
    taxalist = random.randrange(4, 19)
    valorlist = random.randrange(100, 1000)
    # cria o gráfico
    plt.plot(valorlist, color='#17a589', label='valores de empréstimos')
    plt.legend(loc='right', shadow=True)
    plt.xlabel('taxa de juros')
    plt.show()
