#Suponga que un hospital abre la atención de pacientes muy temprano. Uno a uno personas van llegando al hospital.

#Llega la primer persona y la secretaria apunta sus datos personas y la razón de la consulta.

# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
# agregamos una persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')]
# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'), ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')]
# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]
# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'), ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta'), ('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta'), ('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor'), ('Felipe', 'Perez', 12243151, 42, 65151111, 'documento'), ('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor'), ('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')]
# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)
('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')
('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')
('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta')
('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor')
('Felipe', 'Perez', 12243151, 42, 65151111, 'documento')
('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor')
('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')


#Primera pregunta
#Cuantos pacientes llegaron en total?
cantidad=len(agenda_hospital)
#print(cantidad)
print('Los pacientes que llegaron en total son:',cantidad)

#Segunda pregunta
#Cuantas personas llegaron por dolor?
matching = [s for s in agenda_hospital if "dolor" in s]
print('las personas que entraron por dolor fueron:',matching)
#esto me indica quienes entraron por dolor
print('la cantidad de personas que entraron por dolor fueron:',len(matching))

#Tercera pregunta
#Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven

sorted_by_fourth = sorted(agenda_hospital, key=lambda tup: tup[3])
print('Ordenados de menor a mayor',sorted_by_fourth)

sorted_by_fourth = sorted(agenda_hospital, key=lambda tup: tup[3], reverse=True)
print('Ordenados de mayor a menor',sorted_by_fourth)

#Cuarta Pregunta
#Cuantos pacientes son mayores de edad? cuantos menores?
i=0
#for b in agenda_hospital:
#  if agenda_hospital[3] in agenda_hospital >18:
#     i=i+1
#print(i)

x=zip(*agenda_hospital)[3]
print(x)
#if edad < 18:  # el if termina con : para indicar donde acaba la condición
    # el print va indentado con 4 espacios para indicar que está dentro del
    # cuerpo del if
#    print("Menor")
#else:
    # Lo mismo con este print
#   print("Mayor")

#Ejemplo en linea
#a = (1, 2, 3)
#b = (1, 4, 3)

#for idx, (i, j) in enumerate(zip(a, b)):
#    if i == j:
#        print(f'Index {idx} match: {i}')
#    else:
#        print(f'Index {idx} no match: {i} vs {j}')
#        break

#Quinta Pregunta
#Suponga que se atienden con orden de prioridad por gravedad de consulta, empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor. Ordene la lista empenzando por los que tienen mayor prioridad.



#Sexta pregunta
#Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.