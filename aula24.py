numero_um = input('Digite o primeiro número: ')
numero_dois = input('Digite o segundo número: ')

if numero_um > numero_dois:
    print(f'{numero_um} é maior que {numero_dois}')
elif numero_um < numero_dois:
    print(f'{numero_dois} é maior que {numero_um}')
else:
    print(f'{numero_um} é igual a {numero_dois}')
