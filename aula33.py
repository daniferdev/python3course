# tipos built-in são imutáveis
# não podemos alterar o valor de uma string
# mas podemos criar uma nova string com base na original
# e atribuí-la a uma nova variável

# https://docs.python.org/pt-br/3/library/stdtypes.html

nome = 'daniel fernando'
nome_ID = nome + ' moraes'

print(nome)
print(nome_ID)

print(f'{nome.upper()}')

print(f'{(nome[:5])}ABC{(nome[5:])}')

print(nome_ID.zfill(20))  # preenche com zeros à esquerda
print(nome_ID.center(30, '*'))  # centraliza com asteriscos
print(nome_ID.ljust(30, '*'))  # alinha à esquerda com asteriscos
print(nome_ID.rjust(30, '*'))  # alinha à direita com aster
