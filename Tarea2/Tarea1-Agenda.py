#Directorio de pacientes de una clínica.
#Se propone crear una aplicación escrita en Python que permita la gestión de pacientes de una clínica.

#identificación
#Nombre
#Apellido
#teléfono
#dirección
#lista de enfermedades tratadas
#lista de medicamentos que toma

#Operaciones:
#Ingreso de un paciente nuevo
#Borrado de un paciente
#Agregar más enfermedades en un paciente en particular
#Agregar más medicamentos en un paciente en particular
#Generar reporte de las enfermedades tratadas en la clínica
#Generar reporte de los medicamentos entregados en la clínica
#Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.

#Consideraciones:
#La lista inicial de pacientes puede estar escrito en el código asi como su información.
# La implementación puede ser abierta: puede ser que cada paciente sea creado por una clase o simplemente cada paciente sea un diccionario con toda la información solicitada.


#estructura de diccionario
#DictPacientes={"identificación":identificación,"Nombre":Nombre,"Apellido":Apellido,"Tel":Tel,"Dirección":Dirección,"listaenfermedades":listaenfermedades, "listamed":listamed}
#print(DictPacientes)

d={}
dictpact1={'identificación':114380418,'Nombre':'Cristina','Apellido':'Penon','Tel':1234,'Dirección':'Santa Ana','listaenfermedades':['tunel','dolor de cabeza'], 'listamed':['acetaminofen']}
dictpact2={'identificación':112320312,'Nombre':'Monica','Apellido':'Penon','Tel':7896,'Dirección':'San Francsico','listaenfermedades':['dolor de estomago'], 'listamed':['jarabe']}
dictpact3={'identificación':113051813,'Nombre':'Margarita','Apellido':'Baudrit','Tel':8526,'Dirección':'San Jose','listaenfermedades':['diabetes','migrañas'], 'listamed':['insulina','botox']}

print("Información de paciente 1:",dictpact1)
print("Información de paciente 2:",dictpact2)
print("Información de paciente 3:",dictpact3)

pacientes = {114380418: dictpact1, 112320312: dictpact2, 113051813:dictpact3}

print("Este es el dicionario de todos los pacientes:",pacientes)

#ingreso de un paciente nuevo
pacientes[214580418] = {'identificación':214580418,'Nombre':'Andres','Apellido':'Hernandez','Tel':1874,'Dirección':'Santa Ana','listaenfermedades':['dolor de estomago','dolor muscular'], 'listamed':['voltaren','jarabe']}

print("Este es el nuevo diccionario agregando 1 paciente mas:",pacientes)

#borrar 1 paciente
del pacientes[114380418]
print("Este es el nuevo diccionaio borranco 1 paciente:",pacientes)

#Agregar más enfermedades en un paciente en particular

#forma 1 de actualizar- ingresando toda la información
#    dictpact4={'identificación':113051813,'Nombre':'Margarita','Apellido':'Baudrit','Tel':8526,'Dirección':'San Jose','listaenfermedades':['diabetes','migrañas','embarazo'], 'listamed':['insulina','botox']}
#    pacientes[113051813].update(dictpact4)
#    print(pacientes)

#forma 2 de actualizar- agregando 1 condicion mas.
dictpact5='embarazo'
pacientes[113051813]['listaenfermedades'].append(dictpact5)
print("Esta es la lista de enfermedades de 1 paciente en particular actualizada:",pacientes)

#Agregar más medicamentos en un paciente en particular
#forma 1 de actualizar- ingresando toda la información
#    dictpact2={'identificación':112320312,'Nombre':'Monica','Apellido':'Penon','Tel':7896,'Dirección':'San Francsico','listaenfermedades':['dolor de estomago'], 'listamed':['jarabe','clorotrimeton','alergodex']}
#    pacientes[112320312].update(dictpact2)
#    print(pacientes)

#Forma 2 de actualizar-agregando 1 medicamente mas a la lista
dictpact2='clorotrimeton'
pacientes[112320312]['listamed'].append(dictpact2)
print("Esta es la lista de medicamentos de 1 paciente en particular actualizada:",pacientes)

#Generar reporte de las enfermedades tratadas en la clínica
p=[]
for person in pacientes:
    p= p+pacientes[person]['listaenfermedades']
    mylist=list(dict.fromkeys(p))
print("Esta es la lista de enfermedades:",mylist)

#Generar reporte de los medicamentos entregados en la clínica
m=[]
for person in pacientes:
    m= m+pacientes[person]['listamed']
    mylist=list(dict.fromkeys(m))
print("Esta es la lista de medicamentos entregados:",mylist)

#Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.

#comparar enfermedades
a = set(pacientes[112320312]['listaenfermedades'])
b = set(pacientes[113051813]['listaenfermedades'])
print("Esta es la comparación de enfermedades:")
# Letras en a pero no en b
print('en paciente 1 pero no en 2',a - b)
# letras en a o en b o en ambos
print('en paciente 1, paciente 2, o ambos', a | b)
# letras en a y en b
print('en paciente 1 y 2',a & b)
# Letras en a o en b pero no en ambos
print('en paciente 1 o en paciente 2 pero no en ambos', a ^ b)



#comparar medicamentos
a = set(pacientes[112320312]['listamed'])
b = set(pacientes[113051813]['listamed'])
print("Esta es la comparación de medicamentos:")
# Letras en a pero no en b
print('en paciente 1 pero no en 2',a - b)
# letras en a o en b o en ambos
print('en paciente 1, paciente 2, o ambos', a | b)
# letras en a y en b
print('en paciente 1 y 2',a & b)
# Letras en a o en b pero no en ambos
print('en paciente 1 o en paciente 2 pero no en ambos', a ^ b)



