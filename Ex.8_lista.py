# Python4ABMIpea  - Lista 1

# Professor: Bernardo Furtado

# Autora: Marlene Aparecida Argenton


# Exercício 8 - Dicionários. Dado o dicionário: d = {‘a’: 0}:

# 8.1 faça programas que 8.1 acrescente um par (chave, valor) {‘b’: 1}, ao dicionário;

a = {'a': 0}
b = {'b': 1}
a.update(b)
print(a)


#  8.2 verifique se a key ‘c’ está presente?

a = {'a': 0, 'b': 1}
if 'c' in a:
    print(a['c'])
if 'c' not in a:
    print('A key "c" não está presente no dicionário "a"')


#  8.3 Concatene um dicionário a um outro dicionário: e = {'z' : 23}.
# Use o método ‘update’!

a = {'a': 0, 'b': 1}
e = {'z': 23}
a.update(e)
print(f'O dicionário concatenado é:{a}.')
