#Ejercicio: Escribir un for para buscar el máximo de la lista e imprimirlo
lista=[44,11,15,29,53,12,30]
maximo=0
# IMPLEMENTAR




#otrasolucion
maximo=0
for i in lista:
    if i>maximo:
        maximo=i

print('el maximo es',maximo)


#otra solucion
print('el maximo es:',max(lista))


# una solucion
lista.sort()
print(lista)
print(lista[-1])

# debe imprimir 53
print("- El maximo es:", lista[-1])
print(maximo)
