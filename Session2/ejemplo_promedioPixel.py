#Ejercicio
# Pasar a escala de grises el color codificado en los elementos de la lista `pixel`

pixel= [0.6,0.3,0.4] # intensidades de cada canal.
#El elemento 0 es el R, el 1 el G y el 2 el B

# la intensidad en escala de grises es el promedio de la intensidad de cada canal R, G y B
intensidad=0 # IMPLEMENTAR

total=pixel[0]+pixel[1]+pixel[2]
print('esta es la suma de pixeles:',total)
intensidad=total/len(pixel)


print("La intensidad es:")
print(intensidad)

#una debilidad de ese metodo es que no esta flexible a la cantidad de elementos


#otra manera
#mediante ciclos
p=0
for numero in pixel: #numero es una variable que corresponde al valor adentro de la lista. por eso nos deja acumular. en este ejemplo NO es un indice de for
   p+= numero # vaya acumulando en ciclo la suma de todos los numeros
p=p/len(pixel)
print('el promedio es:',p)


#tercera solucion
suma=sum(pixel)
mi_promedio=suma/len(pixel)
print(mi_promedio)

#cuarta opcion
mi_promedio=sum(pixel)/len(pixel)
print(mi_promedio)