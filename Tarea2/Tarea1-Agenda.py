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


#dictpact={'identificación':114380418,'Nombre':Cristina,'Apellido':Penon,'Tel':1234,'Dirección':SantaAna,'listaenfermedades':[tunel,dolor de cabeza], 'listamed':[acetaminofen]}
dictpact1={'identificación':114380418,'Nombre':'Cristina','Apellido':'Penon','Tel':1234,'Dirección':'Santa Ana','listaenfermedades':['tunel','dolor de cabeza'], 'listamed':['acetaminofen']}
dictpact2={'identificación':112320312,'Nombre':'Monica','Apellido':'Penon','Tel':7896,'Dirección':'San Francsico','listaenfermedades':['dolor de estomago'], 'listamed':['jarabe']}
dictpact3={'identificación':113051813,'Nombre':'Margarita','Apellido':'Baudrit','Tel':8526,'Dirección':'San Jose','listaenfermedades':['diabetes','migrañas'], 'listamed':['insulina','']}

print(dictpact)
