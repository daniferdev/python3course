"""
Introdução ao try/except
try: tente executar o código x
except: se der erro, execute o código y
"""

numero_str = input('Vou dobrar o seu número: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é: {numero_float * 2:.2f}')
except:
    print('Isso não é um número válido.')

if numero_str.isdigit():
   numero_float = float(numero_str)
   print(f'O dobro de {numero_str} é: {numero_float *2:.2f}')
else:
   print('Isso não é um número válido.')