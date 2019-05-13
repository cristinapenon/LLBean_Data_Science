cantidad=input("Dígame cuántas palabras tiene la lista:")
cantidad=int(cantidad)
nombres=[]
if cantidad == 0:
    print("Imposible!")
else:
    for x in range(cantidad):
        nom=input("Dígame la palabra {}".format(x+1))
        nombres.append(nom)

for x in range(cantidad):
    print(nombres[x])

duda = input("Dígame la palabra a buscar :")

matching = [s for s in nombres if duda in s]
if len(matching)==0:
    print("la palabra", duda," no existe en la lista")
else:
    y=len(matching)
    print("La palabra",duda," aparece", y," vez/veces en la lista.")