# ********** EJERCICIO_1 **********
# Pedir tres números enteros al usuario y guardarlos en una lista, luego mostrar la lista completa

# numeros_enteros = input('ingrese tres numeros enteros, separados con , : ')
# lista_num_enteros = []
# lista_completa_num_enteros = lista_num_enteros.append(numeros_enteros)

# # print(f'Ingresaste estos Números: {lista_num_enteros}')

# ********** EJERCICIO_2 **********
# Solicitar al usuario su nombre y edad, guardarlos en una tupla y mostrarla.

ingrese_nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
nombre = ingrese_nombre.capitalize()

datos_usuario = (f'Bienvenido/a {nombre}, su edad es: {edad} años')

print(datos_usuario)
