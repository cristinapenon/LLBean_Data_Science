cantidad=input("Dígame cuántas palabras tiene la lista 1:")
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

print(list)

z=input("Diga cuantas palabras tiene la lista 2:")
cantidad2=int(z)


nombres2=[]
if cantidad2 == 0:
    print("Se acabo el ejercicio porque no hay lista 2")
else:
    for x in range(cantidad2):
        nom=input("Dígame la palabra {}".format(x+1))
        nombres2.append(nom)

list2=[]
for x in range(cantidad2):
   # print(nombres[x])
    list2.append(nombres2[x])

print("Esta es la lista 2:",list2)


def Remove(list):
    final_list1 = []
    for num in list:
        if num not in final_list1:
            final_list1.append(num)
    return final_list1
final_list1=Remove(list)
print("Esta es la lista 1 despues de eliminar duplicados:", Remove(list))

def Remove(list2):
    final_list2 = []
    for num2 in list2:
        if num2 not in final_list2:
            final_list2.append(num2)
    return final_list2
final_list2=Remove(list2)
print("Esta es la lista 2 despues de eliminar duplicados:",Remove(list2))

#palabras en las 2 listas
listambas=[]
for i in final_list1:
    for x in final_list2:
        if i==x:
            listambas.append(i)

print("Estas son las que estan en ambas listas:", listambas)

# palabras que solo estan en la primera
listsoloprimera= Remove(list)
for i in listsoloprimera:
    for x in final_list2:
        if i==x:
            b = listsoloprimera.index(i)
            listsoloprimera.pop(b)
print("Estas son las que estan solo en la primera lista:", listsoloprimera)

#palabras que solo estan en la segunda

listsolosegunda=Remove(list2)
for y in listsolosegunda:
    for u in final_list1:
        if y==u:
            c = listsolosegunda.index(y)
            listsolosegunda.pop(c)
print("Estas son las que estan solo en la segunda lista:", listsolosegunda)

#todas las palabras
listcompleta=final_list1+final_list2

def Remove(listcompleta):
    listcompleta1 = []
    for num2 in listcompleta:
        if num2 not in listcompleta1:
            listcompleta1.append(num2)
    return listcompleta1
listcompleta1=Remove(listcompleta)
print("estas son todas las palabras:",listcompleta1)