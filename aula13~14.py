nome = 'Daniel Fernando'
idade = 22
peso = 80.2
altura = 1.80
imc = peso / (altura ** 2)

# F-STRINGS

linha_1 = f'{nome} tem:'
linha_2 = f'{idade} anos'
linha_3 = f'{peso} quilos'
linha_4 = f'{altura:.2f} de altura'
linha_5 = f'E seu IMC é: {imc:.3f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(linha_4)
print(linha_5)

# FORMAT

pais = 'Brasil'
estado = 'Paraná'
cidade = 'Curitiba'

texto = 'Eu moro no {}, estado do {} e cidade de {}'
print(texto.format(pais, estado, cidade))

# Chaves {} são substituídas pelos valores passados no método format.
# A ordem dos valores passados no método format() é a mesma que a ordem das chaves {}.

# Podemos passar valores nomeados para o método format() que serão substituídos nas chaves {}

texto2 = 'Eu moro nos {pais}, estado da {estado} e cidade de {cidade}'
print(texto2.format(pais='Estados Unidos', estado='Virginia', cidade='Richmond'))

# Podemos usar índices nas chaves {} para especificar a ordem dos valores passados no método format()
# Apenas com variáveis, não funciona com valores nomeados

texto3 = 'Eu moro em {2}, estado do {1} e país {0}'
print(texto3.format(pais, estado, cidade))