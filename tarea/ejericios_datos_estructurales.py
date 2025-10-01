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

# datos = set()
# datos.update({primer_palabra, segunda_palabra, ultima_palabra})
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

# ********** EJERCICIO_5 **********
# Ingresar dos valores (0 o 1), convertirlos a booleanos,
# guardarlos en una lista y mostrarla.

# ingrese_valor_1 = int(input('ingrese un valor (0 o 1): '))
# ingrese_valor_2 = int(input('ingrese un valor (0 o 1): '))

# valor_1_bool = bool(ingrese_valor_1)
# valor_2_bool = bool(ingrese_valor_2)

# lista = list()
# lista.append(f'el primer valor es: {ingrese_valor_1} = {valor_1_bool}, el segundo valor es: {ingrese_valor_2} = {valor_2_bool}')
# print(lista)

# ********** EJERCICIO_6 **********
# Pedir dos números decimales y guardarlos como coordenadas (x, y) en una tupla; luego mostrarla.

# ingresar_decimal_x = float(input('ingrese un numero decimal: '))
# ingresar_decimal_y = float(input('ingrese un numero decimal: '))

# coordenada_x = ingresar_decimal_x
# coordenada_y = ingresar_decimal_y
# lista_cordenadas = ['x:', coordenada_x, 'y:', coordenada_y]

# tupla_coordenadas = tuple(lista_cordenadas)

# print(tupla_coordenadas)

# ********** EJERCICIO_7 **********
# Solicitar dos edades y guardarlas en un set; luego mostrar el conjunto.

# ingreso_edad_1 = int(input('ingrese su edad: '))
# ingreso_edad_2 = int(input('ingrese otra edad: '))
# edad_1 = ingreso_edad_1
# edad_2 = ingreso_edad_2

# set_edad = set()
# set_edad.update({f'edad 1: {edad_1}, edad 2: {edad_2}'})
# print(set_edad)

# ********** EJERCICIO_8 **********
# Pedir el nombre de un alumno, su nota decimal y si está activo (0 o 1); guardarlos en un diccionario y mostrarlo.

# ingrese_nombre = input('ingrese su nombre: ')
# ingrese_nota = float(input('ingrese su nota decimal: '))
# ingresar_alumno_activo = int(input('Alumno activo ingrese el 1, de lo contrario, 0: '))

# alumno = ingrese_nombre.capitalize()
# nota_alumno = ingrese_nota
# alumno_activo = ingresar_alumno_activo

# datos_alumno = {
#     'alumno' : ingrese_nombre,
#     'nota' : nota_alumno,
#     'activo' : alumno_activo
# }

# print(datos_alumno.items())

# ********** EJERCICIO_9 **********
# Ingresar tres colores y guardarlos en una lista; luego mostrar la lista.

# print('ingrese 3 colores a continuacion: ')
# ingrese_color_1 = input('ingrese el color 1: ')
# ingrese_color_2 = input('ingrese el color 2: ')
# ingrese_color_3 = input('ingrese el color 3: ')

# color_1 = ingrese_color_1.capitalize()
# color_2 = ingrese_color_2.capitalize()
# color_3 = ingrese_color_3.capitalize()

# lista_colores = list()
# lista_colores.extend({color_1, color_2, color_3})

# print(lista_colores)

# ********** EJERCICIO_10 **********
# Pedir dos números enteros y guardarlos como un 
# par ordenado en una tupla; luego mostrarla.

# ingresar_num_entero_1 = int(input('Ingrese el primer n° entero: '))
# ingresar_num_entero_2 = int(input('Ingrese el segundo n° entero: '))

# dato_num_entero_1 = ingresar_num_entero_1
# dato_num_entero_2 = ingresar_num_entero_2

# lista_ordenada = list()
# lista_ordenada.extend({dato_num_entero_1, dato_num_entero_2})
# lista_ordenada.sort()

# mostrar_datos = tuple(lista_ordenada)
# print(mostrar_datos)

# ********** EJERCICIO_11 **********
# Ingresar cuatro nombres de amigos y guardarlos en un set; luego
#  mostrar el conjunto.

print('\nIngrese por cada input el nombre de un Amigo:\n')
input_amigo_1 = input('Ingrese el 1er nombre: ')
input_amigo_2 = input('Ingrese el 2do nombre: ')
input_amigo_3 = input('Ingrese el 3er nombre: ')
input_amigo_4 = input('Ingrese el 4to nombre: ')

amigo_1 = input_amigo_1.capitalize()
amigo_2 = input_amigo_2.capitalize()
amigo_3 = input_amigo_3.capitalize()
amigo_4 = input_amigo_4.capitalize()

set_amigos = set()
set_amigos.update({amigo_1, amigo_2, amigo_3, amigo_4})
print(f'\nTus amigos son: {set_amigos}')

# ********** EJERCICIO_12 **********
# Solicitar el título y autor de un libro, guardarlos en un diccionario y mostrarlo.

# ingrese_titulo_libro = input('Ingrese el titulo del libro: ')
# ingrese_autor_libro = input('Ingrese el autor del libro: ')

# titulo_libro = ingrese_titulo_libro.title()
# autor_libro = ingrese_autor_libro.title()

# dicc_libros = {
#     'Titulo' : titulo_libro,
#     'Autor' : autor_libro
# }
# print(dicc_libros)

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_1 **********
# Pedir un número entero con input(), convertirlo a float y guardarlo en una
# lista junto con el valor original; luego mostrar la lista.

# ingrese_numero_entero = input('Ingrese un n° entero: ')
# numero_entero_decimal = float(ingrese_numero_entero)
# numero_entero = int(ingrese_numero_entero)

# mostrar_datos = ['Original', numero_entero]
# mostrar_datos.append(f'Decimal: {numero_entero_decimal}')
# print(mostrar_datos)

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_2 **********
# Solicitar un número decimal, convertirlo a int, guardarlo en una tupla
# junto con el valor original y mostrar la tupla.

# input_decimal = float(input('Ingrese un n° decimal: '))
# dato_decimal = input_decimal
# decimal_a_entero = int(input_decimal)
# datos = ['Original:', dato_decimal, 'Entero:', decimal_a_entero]

# datos_tupla = tuple(datos)
# print(datos_tupla)

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_3 **********
# Pedir al usuario un número entero, convertirlo a string, guardarlo en
# un set junto con el entero y mostrar el conjunto.

# ingresar_entero = int(input('Ingrese un n° entero: '))
# numero_ingresado = ingresar_entero
# numero_ingresado_str = str(numero_ingresado)

# set_datos = set()
# set_datos.update({numero_ingresado, numero_ingresado_str})
# print(set_datos)

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_4 **********
# Ingresar la palabra "True" o "False", convertirla a bool, guardarla
# en un diccionario junto con la palabra original y mostrar el diccionario.

# ingrese_palabra = input("ingrese la palabra 'True' o 'false': ") 
# palabra = ingrese_palabra

# palabra_bool = bool(ingrese_palabra)

# dicc_palabra = {
#     'original' : palabra,
#     'booleano' : palabra_bool
# }

# print(dicc_palabra)