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
y = input("Diga cual palabra sustituir :")
z= input("por esta palabra :")

#txt = nombres.replace(y, z)

for i in list:
    if i == y:
       # i = z
        list.insert(i,z)
       #####words = [list.replace(i,z) for z in words]

print(list)