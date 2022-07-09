# Uso de while-loop en listas 
from re import T
from timeit import repeat


in_race = ['Mercedes','McLaren','Ferrari','RedBull']
final_positions = []

while in_race:#va a recorrer todos los elementos en in_race, mientras haya elementos por recorrer (en este caso 4) 
    racing_car = in_race.pop(0) #Con esto saco el ultimo coche de la lista y lo asigno a la variable rasing car
    print(f'{racing_car} está cruzando la meta')
    final_positions.append(racing_car) #Para incluir el rasing car en la lista previamente creada
print(final_positions)
print(in_race)



#in_race_tupla = ('Mercedes','McLaren','Ferrari','RedBull')
#in_race_tupla = list(in_race_tupla) #Para convertir la tupla en lista y poder hacer .pop 
#final_positions2 = []
#while in_race_tupla:#va a recorrer todos los elementos en in_race, mientras haya elementos por recorrer (en este caso 4) 
#    racing_car2 = in_race_tupla.pop() #Con esto saco el ultimo coche de la lista y lo asigno a la variable rasing car
#    print(f'{racing_car2} está cruzando la meta')
#    final_positions2.append(racing_car2) #Para incluir el rasing car en la lista previamente creada

#print(final_positions2)
#print(in_race_tupla)


final_positions_Otro = ['Mercedes', 'McLaren', 'Ferrari', 'Renaul', 'Redbull']
while 'Mercedes' in final_positions_Otro:
    final_positions_Otro.remove('Mercedes')
    print('Mercedes fue descalificado')
print('Nueva tabla de lugares')
print(final_positions_Otro)


#USO DE LOOPS EN DICCIONARIOS. 

# teams = {} #Inicializa un diciconario 
# polling_active = True 
# while polling_active: #Indica mientras poling_active es igual a true 
#     team = input('Cuál es el nombre de la escuderia')
#     driver = input('Cuál es el nombre del piloto')
#     teams[team] = driver #Para llenar el diciconario con los inputs 
#     repeat = input('¿Quieres agregar otro? s/n')
#     if repeat =='n':
#         polling_active = False
# print(teams)




#USO DE CICLO FOR 
# teams_for = ['Mercedes','McLaren','Renault','Williams']
# favourite_teams = []
# for team in teams_for:
#     if team == 'Mercedes':
#         print('Me encanta Mercedes')
#         favourite_teams.append(team)
#     elif team == 'Williams':
#         print('Me encanta Wiliams')
#         favourite_teams.append(team)
#     else:
#         print(f'{team} no me gusta tanto')

# print(teams_for)
#print(favourite_teams)





#USO DE FOOR-LOOP CON DICCIONARIO 
teams_diccionarioFor = {'Mercedes':'Russel','Ferrari':'Saens','Redbull':'Checo'}

for team, driver in teams_diccionarioFor.items(): #.items te tomaba cada uno de los pares del dicionario 
    if team == 'Mercedes':
        continue
    print(f'La escuderia de {team}, tiene al piloto {driver}')

for team in teams_diccionarioFor.keys(): #.key te tomaba cada llave de los pares del dicionario 
    print(f'La escuderia es {team}')

for driver in teams_diccionarioFor.values(): #.key te tomaba cada llave de los pares del dicionario 
    print(f'El piloto es {driver}')


name ='Formula uno'
for letters in name:
    print(letters)




#USO DE LOOPS ANIDADOS
teams = {
    'Mercedes':
    {
        'drivers': ['Hugo','Paco','Juana'],
        'budget': 6000000,
        'country':'Alemania'
    },
    'McLaren':
    {
        'drivers': ['Marcela','Pedro','Juan'],
        'budget': 700000,
        'country': 'Inglaterra'
    }
}

for team, description in teams.items():
    print(f"La escudedía {team} tiene")
    print(f"Un presupuesto de {description['budget']}")
    print(f"Y es del país {description['country']}")
    for driver in description['drivers']: #aqui se anuda un for dentro de otro para que imprima los drivers en cada escuderia
        print(f"Tiene al piloto {driver}")


list1 = list(range(-4,8,2))
for i in list1:
    print (i)


race2 = 'formula1'
list(range(0,len(race2),2))
for i in range(0,len(race2),2):
    print(race2[i])


race3 ='formula1'
for i in race3[::2]:
    print(i)


status = 'Active '
offset = 0 
for item in status:
    print(f'{item} appears at offset' + str(offset))
    offset+=1
    







