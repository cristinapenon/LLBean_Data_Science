#asi se ingresan comentarios
#esto es un ejemplo de un comentario

'''
El texto
poniendo 3 comillas deja poner un bloque de texto completo en multiples lineas
'''

#ejercicio individual
#escribir un texto para que se muestre en pantalla
#que sea de 3 lineas
print('hola profe \ncomo esta? \nEste es mi ejemplo. :)')

# para correr una hace click derecho y le da run--- ojo que el run dice el nombre del archivo!! prestar atencion
#para correr solo 1 linea, se subraya la linea y le da right click y execute line in console---pero ahorita en mi compu no funciona

#id de variable es por dato y NO por el nombre de la variable

### Enteros ###

x = 3

print("- Tipo de x:")
print(type(x)) # Imprime el tipo (o `clase`) de x
print("- Valor de x:")
print(x)       # Imprimir un valor
print("- x+1:")
print(x + 1)   # Suma: imprime "4"
print("- x-1:")
print(x - 1)   # Resta; imprime "2"
print("- x*2:")
print(x * 2)   # Multiplicación; imprime "6"
print("- x^2:")
print(x ** 2)  # Exponenciación; imprime "9"
# Modificación de x
# cada vez que pasa por aqui aumenta X por valor de 1
x += 1

print("- x modificado:")
print(x)  # Imprime "4"

x *= 2 # aqui multiplica x2 cada vez que pasa
print("- x modificado:")
print(x)  # Imprime "8"

print("- Varias cosas en una línea:")
print(1,2,x,5*2) # imprime varias cosas a la vez


#ejemplos booleanos
v1= True #ojo que es sencible a las mayusculas entonces tener cuidado.
v2= False

#se puede hacer listas ocn tipo de datos mezclados


#listas
print("- Lista con 4 números:")
a=[57,45,7,13] # una lista con cuatro números
print(a)

print("- Lista con 3 strings:")
b=["hola","chau","buen día"] # una lista con tres strings
print(b)

# la función `len` me da la longitud de la lista
print("- Longitud de la lista:")
n=len(a)
print(n)
#- Lista con 4 números:
[57, 45, 7, 13]
#- Lista con 3 strings:
['hola', 'chau', 'buen día']
#- Longitud de la lista:
4


#Para acceder a sus elementos, se utiliza el [] Los índices comienzan en 0

print("- Elemento con índice 0 de la lista:")
print(b[0])
print("- Elemento con índice 1 de la lista:")
print(b[1])
print("- Elemento con índice 2 de la lista:")
print(b[2])
# ultima de la lista se saca con -1
print(b[-1])


#diferencia de tupla vs lista
#una tupla una vez creado no se puede cambiar- so contenido se queda congelado
#solo lo puede consultar, operar, pero NO cambiar. La lista si permite editar.