# Debugando código Python
# Debugar é o processo de encontrar e corrigir erros em um programa.
# Neste exemplo, vamos usar condicionais para demonstrar o fluxo de execução.# Condicionais são estruturas que permitem executar diferentes blocos de código
# dependendo de condições específicas
# que são avaliadas como verdadeiras ou falsas.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')

