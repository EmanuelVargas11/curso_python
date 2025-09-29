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
# tupla_coordenadas = ('x:', coordenada_x, 'y:', coordenada_y)

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

# alumno = ingrese_nombre
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

print('ingrese 3 colores a continuacion: ')
ingrese_color_1 = input('ingrese el color 1: ')
ingrese_color_2 = input('ingrese el color 2: ')
ingrese_color_3 = input('ingrese el color 3: ')

color_1 = ingrese_color_1
color_2 = ingrese_color_2
color_3 = ingrese_color_3

lista_colores = list()
lista_colores.extend({color_1, color_2, color_3})

print(lista_colores)