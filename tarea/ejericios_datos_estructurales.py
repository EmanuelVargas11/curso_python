# ********** EJERCICIO_1 **********
# Pedir tres números enteros al usuario y guardarlos en
# una lista, luego mostrar la lista completa

# numeros_enteros_1 = input('ingrese un numeros enteros: ')
# numeros_enteros_2 = input('ingrese un numeros enteros: ')
# numeros_enteros_3 = input('ingrese un numeros enteros: ')

# lista_num_enteros = [numeros_enteros_1, numeros_enteros_2, numeros_enteros_3]

# print(f'Ingresaste estos Números: {lista_num_enteros}')

# ********** EJERCICIO_2 **********
# Solicitar al usuario su nombre y edad, guardarlos en una tupla y mostrarla.

# ingrese_nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# nombre = ingrese_nombre.capitalize()

# datos_usuario = (nombre, edad)

# print(datos_usuario)

# ********** EJERCICIO_3 **********
# Pedir tres palabras y guardarlas en un set; luego mostrar el conjunto.

# ingrese_palabras_1 = input('Ingrese la primer palabra: ')
# ingrese_palabras_2 = input('Ingrese la segunda palabra: ')
# ingrese_palabras_3 = input('E ingrese la ultima palabra: ')

# primer_palabra = ingrese_palabras_1
# segunda_palabra = ingrese_palabras_2
# ultima_palabra = ingrese_palabras_3

# # guardar valores en un set
# datos = {primer_palabra, segunda_palabra, ultima_palabra}

# # mostrar el conjunto
# print(datos)

# ********** EJERCICIO_4 **********
# Solicitar el nombre y el precio de un producto, guardarlos en un
# diccionario y mostrarlo.

# producto_ingresado = input('ingrese el producto solicitado: ')
# precio_dado = int(input('ingrese el precio del producto: $'))

# product_dicc = {
#     "producto:" : producto_ingresado,
#     "precio" : precio_dado
# }

# print(product_dicc)

# ********** EJERCICIO_5 **********
# Ingresar dos valores (0 o 1), convertirlos a booleanos,
# guardarlos en una lista y mostrarla.

# ingrese_valor_1 = int(input('ingrese un valor (0 o 1): '))
# ingrese_valor_2 = int(input('ingrese un valor (0 o 1): '))

# valor_1_bool = bool(ingrese_valor_1)
# valor_2_bool = bool(ingrese_valor_2)

# lista = [valor_1_bool, valor_2_bool]

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

# edad_1 = int(input('ingrese su edad: '))
# edad_2 = int(input('ingrese otra edad: '))

# set_edad = {edad_1, edad_2}

# print(set_edad)

# ********** EJERCICIO_8 **********
# Pedir el nombre de un alumno, su nota decimal y si está activo (0 o 1); guardarlos en un diccionario y mostrarlo.

# solicitar al usuario el nombre, la nota decimal y si aun esta activo
# ingrese_nombre = input('ingrese su nombre: ')
# nota_alumno = float(input('ingrese su nota decimal: '))
# alumno_activo = int(input('Alumno activo ingrese el 1, de lo contrario, 0: '))

# alumno = ingrese_nombre.capitalize()

# guardar en un diccionario los valores
# datos_alumno = {
#     'alumno' : alumno,
#     'nota' : nota_alumno,
#     'activo' : alumno_activo
# }

# mostrar el diccionario
# print(datos_alumno.items())

# ********** EJERCICIO_9 **********
# Ingresar tres colores y guardarlos en una lista; luego mostrar la lista.

# # solicitar al usuario que ingrese tres colores
# print('ingrese 3 colores a continuacion: ')
# ingrese_color_1 = input('ingrese el color 1: ')
# ingrese_color_2 = input('ingrese el color 2: ')
# ingrese_color_3 = input('ingrese el color 3: ')

# color_1 = ingrese_color_1.capitalize()
# color_2 = ingrese_color_2.capitalize()
# color_3 = ingrese_color_3.capitalize()

#  # guardar en una lista
# lista_colores = [color_1, color_2, color_3]
# print(lista_colores)

# ********** EJERCICIO_10 **********
# Pedir dos números enteros y guardarlos como un
# par ordenado en una tupla; luego mostrarla.

# solicitar al usuario dos números enteros
# dato_num_entero_1 = int(input('Ingrese el primer n° entero: '))
# dato_num_entero_2 = int(input('Ingrese el segundo n° entero: '))

# ordenar los valores
# lista_ordenada = [dato_num_entero_1, dato_num_entero_2]
# lista_ordenada.sort()

# guardarlo en una tupla
# mostrar_datos = tuple(lista_ordenada)

# mostrar el valor
# print(mostrar_datos)

# ********** EJERCICIO_11 **********
# Ingresar cuatro nombres de amigos y guardarlos en un set; luego
#  mostrar el conjunto.

# # Solicitar el nombre de cuatro amigos al usuario
# input_amigo_1 = input('Ingrese el 1er nombre: ')
# input_amigo_2 = input('Ingrese el 2do nombre: ')
# input_amigo_3 = input('Ingrese el 3er nombre: ')
# input_amigo_4 = input('Ingrese el 4to nombre: ')

# # a cada valor se le asigna la propiedad capitalize()
# amigo_1 = input_amigo_1.capitalize()
# amigo_2 = input_amigo_2.capitalize()
# amigo_3 = input_amigo_3.capitalize()
# amigo_4 = input_amigo_4.capitalize()

# # guardar los valores en un set
# set_amigos = (amigo_1, amigo_2, amigo_3, amigo_4)

# # mostrar el conjunto
# print('Tus amigos son:', set_amigos)


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

# mostar_datos = [numero_entero, numero_entero_decimal]

# print(mostrar_datos)

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_2 **********
# Solicitar un número decimal, convertirlo a int, guardarlo en una tupla
# junto con el valor original y mostrar la tupla.

# # solicitar un número decimal al usuario
# numero_decimal = float(input('Ingrese un n° decimal: '))

# # convertir el número a entero
# decimal_a_entero = int(numero_decimal)

# # guardar los datos en una tupla
# datos_tupla = (numero_decimal, decimal_a_entero)

# #mostrar la tupla
# print(datos_tupla)

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_3 **********
# Pedir al usuario un número entero, convertirlo a string, guardarlo en
# un set junto con el entero y mostrar el conjunto.

# ingresar_entero = int(input('Ingrese un n° entero: '))
# numero_ingresado = ingresar_entero
# numero_ingresado_str = str(numero_ingresado)

# set_datos = {numero_ingresado, numero_ingresado_str}

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

# ********** EJERCICIOS MATEMATICOS **********
# ********** EJERCICIO_5 **********

# Solicitar un número entero y convertirlo a string y a float;
# guardar los tres (int, str, float) en una lista y mostrarla.

# solicitar un numero entero al usuario
numero_entero = int(input('Ingrese un numero entero: '))

# convertir a string y decimal
str_entero = str(numero_entero)
decimal = float(numero_entero)

# guardar los 3 en una lista
datos = [numero_entero, str_entero, decimal]

# mostrar lista
print(datos)

