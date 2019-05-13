cantidad=input("Dígame cuántas palabras tiene la lista:")
cantidad=int(cantidad)
nombres=[]
if cantidad == 0:
    print("Imposible!")
else:
    for x in range(cantidad):
        nom=input("Dígame la palabra :")
        nombres.append(nom)

list=[]
for x in range(cantidad):
   # print(nombres[x])
    list.append(nombres[x])

print(list)

y = input("Diga cual palabra quiere eliminar :")
z=''
for i in list:
    if i == y:
        #list = [item.replace(i, z) for item in list]
        b = list.index(i)
        del list[b]
       #list.insert(i,z)
      #words = [list.replace(i) for z in list]

print(list)