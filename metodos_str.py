# Script que aplica 3 métodos de str a un dato ingresado

# Ingresar texto
texto = input("Ingrese un texto: ")

# Aplicamos 3 métodos de string
# minuscula = texto.lower()       # todo en minúscula
# mayuscula = texto.upper()       # todo en mayúscula
# invertido = texto.swapcase()    # invierte mayúsculas y minúsculas

# Ejemplos:

# Mostramos resultados
# print("\nResultados:")
# print(f"Original:   {texto}")
# print(f"Minúsculas: {minuscula}")
# print(f"Mayúsculas: {mayuscula}")
# print(f"Invertido:  {invertido}")

# Ejercicios: 

texto_split = texto.split()
texto_primera_mayus = texto.capitalize()
texto_join = "*".join(texto)
longitud_texto = len(texto)


print(f'\nResultados: ')
print(f'\nOriginal: {texto}')
print(f'Metodo split: {texto_split}')
print(f'Metodo capitalize: {texto_primera_mayus} ')
print(f'Metodo join: {texto_join}')
print(f'Metodo length: Longitud: {longitud_texto}')

