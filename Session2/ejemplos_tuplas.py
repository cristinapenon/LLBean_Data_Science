#esto es un ejemplo de tuplas
#crear una tupla de 5 elementos de tipos difernetes

mi_tupla=('a', 3, 16,'mitexto', True)

#imprimir la tupla
print(mi_tupla)

#como podria hacer para agregar mas elementos

mi_tupla=mi_tupla + (1,'b') # se puede agregar otra tupla con el +
print(mi_tupla)

#otra  forma de agregar
mi_tupla +=(0,'x') # += es para acumular
print(mi_tupla)

#subtupla
# del segundo hasta el penultimo
print(mi_tupla[1:-1]) # e; ] de al final es exluyente
#si quisiera todos hacia el final es no poner al final
print(mi_tupla[1:])

#subtupla con saltos
#los elementos pares
print('los elementos pares de acuerdo a la posicion son:',mi_tupla[::2]) #al final va la cantidad de saltos. la posicion 0 es par

#los elementos impares
print('los elementos impares de acuerdo a la posicion son:',mi_tupla[1::2]) #empieza en 1 pero misma manera de satos
#doble puntos son saltos


