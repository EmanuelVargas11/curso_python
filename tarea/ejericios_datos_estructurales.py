# ********** EJERCICIO_1 **********
# Pedir tres números enteros al usuario y guardarlos en
# una lista, luego mostrar la lista completa

# numeros_enteros = input('ingrese tres numeros enteros, separados con , : ')
# lista_num_enteros = []
# lista_completa_num_enteros = lista_num_enteros.append(numeros_enteros)

# # print(f'Ingresaste estos Números: {lista_num_enteros}')

# ********** EJERCICIO_2 **********
# Solicitar al usuario su nombre y edad, guardarlos en una tupla y mostrarla.

# ingrese_nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# nombre = ingrese_nombre.capitalize()

# datos_usuario = (f'Bienvenido/a {nombre}, su edad es: {edad} años')

# print(datos_usuario)

# ********** EJERCICIO_3 **********
# Pedir tres palabras y guardarlas en un set; luego mostrar el conjunto.

# ingrese_palabras_1 = input('Ingrese la primer palabra: ')
# ingrese_palabras_2 = input('Ingrese la segunda palabra: ')
# ingrese_palabras_3 = input('E ingrese la ultima palabra: ')

# primer_palabra = ingrese_palabras_1
# segunda_palabra = ingrese_palabras_2
# ultima_palabra = ingrese_palabras_3

# set_datos = set()

# datos = set_datos.union({primer_palabra, 
#                         segunda_palabra,
#                         ultima_palabra})

# print(datos)

# ********** EJERCICIO_4 **********
# Solicitar el nombre y el precio de un producto, guardarlos en un
# diccionario y mostrarlo.

# solicitar_producto = input('ingrese el producto solicitado: ')
# solicitar_precio = int(input('ingrese el precio del producto: $'))

# producto_ingresado = solicitar_producto
# precio_dado = solicitar_precio

# product_dicc = {
#     "producto:" : producto_ingresado,
#     "precio" : precio_dado
# }

# datos_dicc = product_dicc.items()
# print(datos_dicc)

# ********** EJERCICIO_4 **********
# Ingresar dos valores (0 o 1), convertirlos a booleanos,
# guardarlos en una lista y mostrarla.

ingrese_valor_1 = int(input('ingrese un valor (0 o 1): '))
ingrese_valor_2 = int(input('ingrese un valor (0 o 1): '))

valor_1_bool = bool(ingrese_valor_1)
valor_2_bool = bool(ingrese_valor_2)

lista = list()
datos_bool_lista = lista.append(valor_2_bool)
