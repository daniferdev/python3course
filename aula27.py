# Fatiamento de strings e função Len

# Hello World
# 012345678910
# -0123456789
# Fatiamento [início:fim:passo] // [i:f:p]

yoda = 'O que você ta fazendo menor?'

print(yoda)

print(yoda[0:2])  # O
print(yoda[3:6])  # ue
print(yoda[7:9])  # oc
print(yoda[10:20]) # ta fazen

print(yoda[0:2:2])  # O
print(yoda[3:6:2])  # u
print(yoda[7:9:2])  # o
print(yoda[10:20:2])  # afzn

# Funçao len

print(len(yoda))  # 30
print(f'O tamanho da string yoda é de {len(yoda)} caracteres')

print(len(yoda[0:2]))  # 2
print(len(yoda[3:6]))  # 3