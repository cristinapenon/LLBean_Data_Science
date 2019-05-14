#Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona. La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco, la segunda columna la cantidad en crédito en miles de colones y la tercer columna en miles de colones en deuda.

hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]
print(hoja_calculo)
#Suponga que se dispone de una función que procesa la lista para obtener la transpuesta(cambiar las columnas por las filas)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]
b = transpuesta(hoja_calculo)
print(b)
#b #sea b la tabla resultante luego de aplicar transpuesta
#[['carlos', 'juan', 'luis'],
# [54.54, 5.54, 9.54],
# [6.57, 9.57, 7.57],
# [3.64, 4.64, 1.64]]
#Por otro lado, se puede aplicar matemática o cualquier otra operación a alguna fila en específico. Por ejemplo: dividir todos los números entre 10. Obteniendo:

b[1] = list(map(lambda x: x/10, b[1]))
print(b[1])
#b
#[['carlos', 'juan', 'luis'],
# [5.454, 0.554, 0.954],
# [6.57, 9.57, 7.57],
# [3.64, 4.64, 1.64]]

#Parte 1
#Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:
#Promedio
promedio=lambda sum(x)/len(x)
#La suma
sumar = lambda x,y: x+y
#La multiplicación
mult= lambda x,y: x*y
dict = {sumar,mult,promedio}

#Parte 2
#Obtenga utilizando el diccionario de funciones:

#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.

#2. La suma de todas las deudas

#3. la multiplicación de todos los crédito entre si



#Parte 3
#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20%
# (esto es multiplicar por 1.2) a toda la fila de créditos usando el diccionario de funciones.