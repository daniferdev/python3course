# Operações Aritméticas

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

concatenacao = 'Daniel' + ' ' + 'Fernando'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_Daniel = 3 * 'Daniel'
print(a_dez_vezes)
print(tres_vezes_Daniel)

# Ordem das operações
# 1. parenteses
# 2. exponenciação
# 3. multiplicação/divisão
# 4. adição/subtração

print(1 + 1 ** 5 + 5) # O resultado é 7
print((1 + 1) ** (5 + 5)) # O resultado é 1024
