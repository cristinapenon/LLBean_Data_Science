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

def Remove(list):
    final_list = []
    for num in list:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
#duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print("Esta es la lista sin duplicados:",Remove(list))

#print("Esta es la lista sin duplicados:", list)