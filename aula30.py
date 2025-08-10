"""
Constante -> "Variáveis" que não vão mudar o valor durante a execução do programa.
Boas práticas:
- Sempre usar letras maiúsculas.
- Usar underscore (_) para separar palavras.
- Usar nomes que façam sentido.

Não usar muitas condições no mesmo if, pois isso pode dificultar a leitura do código.
Quanto mais indentação, mais difícil fica de ler o código.
"""
RADAR_RANGE = 5

RADAR1_LOCATION = 100
RADAR1_SPEED_LIMIT = 60

CAR1_SPEED = 140

CAR1_LOCATION = 97

RADAR1_RANGE = RADAR1_LOCATION - RADAR_RANGE <= CAR1_LOCATION <= RADAR1_LOCATION + RADAR_RANGE

if CAR1_SPEED <= RADAR1_SPEED_LIMIT: 
    print('Carro está no limite de velocidade permitida')
    
else:
    if RADAR1_RANGE:
        print('Carro multado no radar 1 por excesso de velocidade')
    else:
        print('Carro fora do alcance do radar')
