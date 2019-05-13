#PARTE!
#Funcionamiento sugerido

#Dígame cuántas palabras tiene la lista: 3
#Dígame la palabra 1: Alberto
#Dígame la palabra 2: Benito
#Dígame la palabra 3: Carmen
#La lista creada es: ['Alberto', 'Benito', 'Carmen']
#Dígame cuántas palabras tiene la lista: 0
#¡Imposible!


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


