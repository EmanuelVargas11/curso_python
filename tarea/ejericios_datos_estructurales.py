# ********** EJERCICIO_1 **********
# Pedir tres números enteros al usuario y guardarlos en una lista, luego mostrar la lista completa

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
# ingrese_palabras_3 = input('E ingrese la tercer palabra: ')
# set_datos =set()
# datos = set_datos.union({ingrese_palabras_1, ingrese_palabras_2, ingrese_palabras_3})

# print(datos)


# ********** EJERCICIO_4 **********
# Solicitar el nombre y el precio de un producto, guardarlos en un diccionario y mostrarlo.

producto = input('ingrese el producto solicitado: ')
precio = int(input('ingrese el precio del producto: $ '))

datos_dicc = {
    "producto:" : producto,
    "precio $" : precio
}

for clave, valor in datos_dicc.items():
    print(clave, valor)

# print(datos_dicc.items())