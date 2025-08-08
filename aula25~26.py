# Interpolação de strings
# Formatação de strings com f-strings

# s - string
# d - inteiro
# f - float
# x e X - hexadecimal
# (caractere) < - alinhamento à esquerda
# (caractere) > - alinhamento à direita
# (caractere) ^ - alinhamento ao centro
# Sinal + ou - para indicar positivo ou negativo

# Exemplo de formatação de strings

objeto = 'Playstation 5'
preço = 4499.99
print('%s custa R$ %.2f' % (objeto, preço)) # Estilo C
print(f'{objeto} custa R$ {preço:.2f}') # Estilo Python

numero = 360
print(f'O hexadecimal de {numero} é representado por {numero:06x}')
print('O hexadecimal de %d é representado por %06x' % (numero, numero)) 
