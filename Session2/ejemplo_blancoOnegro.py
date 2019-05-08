#Ejercicio
# Pasar a blanco y negro el valor de intensidad codificado en la variable intensidad


# podemos considerar que un pixel se convierte en blanco si su intensidad en escala de grises es mayor a 0.5
# y negro de lo contrario
bw = 0 # IMPLEMENTAR

pixel= [0.6,0.3,0.4] # intensidades de cada canal.
mi_promedio=sum(pixel)/len(pixel)
print(mi_promedio)
#decidir si es blanco o negro
if mi_promedio>0.5:
    print('es blanco')
else:
    print('es negro')

#print("En blanco y negro el pixel sería: (0 -> negro, 1 -> blanco)")
print(bw)