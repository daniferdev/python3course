"""
Tipo de tipagem = Dinamica / Forte
Tipos de dados primitivos:
- int (inteiro)
- float (ponto flutuante)
- bool (booleano)
- str (string)
- None (nulo)
"""

# STRING

# Aspas simples
print('Hello World')

# Aspas duplas
print("Hello World")

# Aspas triplas
print('''Hello World''')
print("""Hello World""")

# Escape de caracteres
print('Hello \'World\'')  # Escape de aspas simples
print("Hello \"World\"")  # Escape de aspas duplas

# r ou R (raw string)
print(r'Hello \'World\'')  # Raw string, não interpreta escape
print(R"Hello \"World\"")  # Raw string, não interpreta escape

# INT

print(10)  # Inteiro positivo
print(-10)  # Inteiro negativo
print(0)  # Zero

# FLOAT

print(10.5)  # Ponto flutuante positivo
print(-10.5)  # Ponto flutuante negativo
print(0.0)  # Zero ponto flutuante

# BOOL
print(True)  # Verdadeiro
print(False)  # Falso

# NONE
print(None)  # Nulo, ausência de valor

# TYPE
print(type('Hello World'))  # <class 'str'>
print(type(10))  # <class 'int'>
print(type(10.5))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
