cantidad=input("Dígame cuántas palabras tiene la lista:")
cantidad=int(cantidad)
nombres=[]
if cantidad == 0:
    print("Imposible!")
else:
    for x in range(cantidad):
        nom=input("Dígame la palabra {}".format(x+1))
        nombres.append(nom)

list=[]
for x in range(cantidad):
   # print(nombres[x])
    list.append(nombres[x])

print("Esta es la lista original:",list)

#sort = sorted(list, key=lambda tup: tup[3], reverse=True)
sort = sorted(list, key=lambda tup: tup[1], reverse=False)

print("Esta es la lista inversa:",sort)