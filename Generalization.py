# Python4ABMIpea  - Exercício 2
#
# Professor: Bernardo Furtado
#
# Autora: Marlene Aparecida Argenton
#
# Simplesmente, crie uma rotina que testa números de agentes e de lojas, roda a interação e verificam-se os
# resultados:
# Average fun, average balance, average cost
# Salve em um arquivo.
# Possivelmente, depois, será possível realizar plots(gráficos)
# Um pouco mais detalhado:
#   Crie uma lista com vários números de Agents
#   Claro, com alguma relação óbvia. Por exemplo, aumentando linearmente de tamanho. Ou exponencialmente
#   Crie uma lista com vários números de Shops
#   Em um for loop, chame a função principal do  interactions (que recebe com parâmetros número de agentes e lojas).


import Interaction
import os
import matplotlib.pyplot as plt


def grafic_average(a, s):
    file = 'account_results.csv'
    # cria listas para os resultados
    ag_list = []
    sh_list = []
    fun_list = []
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        f.write('n_agentes; n_lojas; satisfacao media; custo medio das lojas, media das contas das lojas e a media'
                'das contas dos agentes\n')
        for i in range(len(a)) and range(len(s)):
            # cria lista de resultados para o gráfico
            agent, shop = Interaction.main(a[i], s[i])
            avg_fun = sum([i.fun for i in agent]) / len(agent)
            avg_cost = sum([i.cost for i in shop]) / len(shop)
            avg_shop = sum([i.account.balance for i in shop]) / len(shop)
            avg_agent = sum([i.account.balance for i in agent]) / len(agent)
            f.write('{}; {}; {:.2f}; {:.2f}; {:.2f}; {:.2f}'.format(a[i], s[i], avg_fun, avg_cost, avg_shop, avg_agent))
            f.write('\n')
            fun_list.append(avg_fun)
            ag_list.append(avg_agent)
            sh_list.append(avg_shop)
    # cria o gráfico
    plt.plot(a, fun_list, color='#17a589', label='satisfação média')
    plt.plot(a, ag_list, color='red', label='Saldo médio das contas dos agente')
    plt.plot(a, sh_list, color='#f4d03f', label='Saldo médio das contas das lojas')
    plt.legend(loc='right', shadow=True)
    plt.xlabel('número de agentes')
    plt.show()


if __name__ == '__main__':
    ag = [10, 50, 100, 200, 300, 600, 1000, 1200, 2300, 3000, 4500, 5300, 6000, 8200, 9500, 10000, 10400]
    #sh = [20, 100, 200, 400, 600, 1200, 2000, 2400, 4600, 6000, 9000, 10600, 12000, 16200, 19000, 20000, 20800]
    sh = ([15] * len(ag))
    grafic_average(ag, sh)
