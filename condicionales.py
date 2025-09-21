texto = input('ingrese una frase: ')

if texto.isalpha() == False:
    print(f'ingrese texto sin numeros: {texto}')
else:
    print(texto)