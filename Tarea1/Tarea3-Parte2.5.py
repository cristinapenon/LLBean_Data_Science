cantidad=input("Dígame cuántas palabras tiene la lista:")
stringcantidad=str(cantidad)
cantidad=int(cantidad)
nombres=[]
if cantidad == 0:
    print("Imposible!")
else:
    for x in range(cantidad):
        nom=input("Dígame la palabra  :")
        nombres.append(nom)

list=[]
for x in range(cantidad):
   # print(nombres[x])
    list.append(nombres[x])

print(list)

z=input("Diga cuantas palabras tiene la lista de palabras a eliminar:")
cantidadeliminar=int(z)


nombreseliminar=[]
if cantidadeliminar == 0:
    print("Se acabo el ejercicio")
else:
    for x in range(cantidadeliminar):
        nom=input("Dígame la palabra por eliminar :")
        nombreseliminar.append(nom)

listeliminar=[]
for x in range(cantidadeliminar):
   # print(nombres[x])
    listeliminar.append(nombreseliminar[x])

print("Esta es la lista por eliminar:",listeliminar)

#y = input("Diga cual palabra quiere eliminar :")
for i in list:
    for t in listeliminar:
        if i == t:
        #list = [item.replace(i, z) for item in list]
           b = list.index(i)
           list.pop(b)
       #list.insert(i,z)
      #words = [list.replace(i) for z in list]

print("Esta es la lista despues de eliminar la otra lista:",list)