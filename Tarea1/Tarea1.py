
#Escribir un código en Python que imprima en pantalla lo siguiente:
#* 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14

#usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos.

pie="3.1415926"
listpie=list(pie)
print(listpie)
list3=listpie[:-1]
list3+='*'
print(list3)

i=len(listpie)

pie="3.1415926"
for i in listpie:
    x = listpie.replace(i, "*")
    print(x)
#    listpie += '*'
   #listpie[-1]
   #i= '*'
 #  print(listpie)


