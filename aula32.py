"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
    
try:
    
    numero = int(input('Digite um número inteiro: '))
    
    if (numero % 2 == 0):
        print('O número é par.')
    else:
        print('O número é impar.')
        
except ValueError:
    print('O número digitado não é inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    
    horario = int(input('Digite o horário: '))
    
    if (0 <= horario <= 11):
        print('Bom dia!')
    elif (12 <= horario <= 17):
        print('Boa tarde!')
    elif (18 <= horario <= 23):
        print('Boa noite!')
        
except ValueError:
    print('Horário inválido. Digite novamente.')
    
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

    
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)    
    
if tamanho_nome > 1:
    
    if tamanho_nome <= 4:
            print('Seu nome é curto!')
    elif (5 <= tamanho_nome <= 6):
            print('Seu nome é normal!')
    else: 
            print('Seu nome é muito grande!')
else:
    print('Digite um nome maior')
        