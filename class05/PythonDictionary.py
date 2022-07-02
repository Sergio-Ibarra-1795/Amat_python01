#Creando diccionarios 

videogame_boss = {'species':'alien', 'points':50}
english_spanish = {'dog':'perro','cat':'gato', 'duck':'pato', 'horse':'caballo'}
favourite_tacos = {'Pedro':'pastor', 'Daniel':'bisteck'}
print(videogame_boss)
print(type(videogame_boss))

#Accediendo a elementos por llave
print(videogame_boss['species'])
print(favourite_tacos['Pedro'])

#Accediendo a elementos por items (par) 
print(videogame_boss.items())

#Mostrando las llaves del diccionario 
print(videogame_boss.keys())

#Mostrando los valores diccionario 
print(videogame_boss.values())

#Agregando nuevos elementos al diciconario
videogame_boss['power'] = 'medium'
print(videogame_boss)

#Modificar elementos 
videogame_boss ['power'] = 'maximum'
print(videogame_boss)

#Eliminando elementos 
del videogame_boss ['species'] 
print(videogame_boss)


#Recorriendo por llave y valor 
for key, value in videogame_boss.items():
    print(f"La llave {key} tiene el valor {value}")

#Recorriendo por llaves 
for key in videogame_boss.keys():
    print(f"Tienes la llave {key}")

#Recorriendo por valores 
for values in videogame_boss.values():
    print(f"Tienes el valor {values}")

for values in english_spanish.values():
    print(f"Tienes el valor {values}")


#Recorriendo por valores 
for values in videogame_boss.values():
    if value =='maximum':
        print(f"Tienes el valor {values}")


#Lista de diccionarios
videogame_boss1 = {'species':'alien', 'points':50}
videogame_boss2 = {'species':'human', 'points':20}
videogame_boss3 = {'species':'reptilian', 'points':150}

bosses = [videogame_boss1, videogame_boss2, videogame_boss3]

for boss in bosses: 
    print(boss)


# Anidando listas en un diccionario 
baguette = {
    'carne':'jamon',
    'quesos':['manchego', 'cabra'],
    'fruta':'uva'
}

print(f"Usted ordenó una baguette de {baguette['carne']}")
print(f"Con {baguette['fruta']}")
print(f"Y con los siguientes quesos:")
for cheese in baguette['quesos']:
    print(cheese)



# Anidando diccionarios en diccionarioes

countries = {
    'Mexico':{
        'capital':'Ciudad de México',
        'comida_tipica':'Mole'
    },
    'USA': {
        'capital':'Washigton DC',
        'comida_tipica':'Hamburguesa'
    }

}

print(countries)
print(type(countries))

# for country, countri_info in countries.items():
#     print( "\n País:{country}")
#     print(f"Capital": {country_info ['capital']})
#     print(f"Comida tipica": {country_info ['comida tipica']})

for country, country_info in countries.items():
    print(f"\nPaís: {country}")
    print(f"Capital: {country_info['capital']}")
    print(f"Comida típica: {country_info['comida_tipica']}")



 # videogame_boss_copy = videogame_boss
 # print(videogame_boss)
 # print(videogame_boss_copy)

 # videogame_boss['videogame'] = 'Hello'
 # print(videogame_boss)
 # print(videogame_boss_copy)

 # videogame_boss['power'] =1.23
 # print(videogame_boss)
 # print(videogame_boss_copy)

 # videogame_boss_copy['power'] =False
 # print(videogame_boss)
 # print(videogame_boss_copy)

print(videogame_boss)
videogame_boss_copy = videogame_boss.copy()
print(videogame_boss_copy)

videogame_boss['videogame'] = 'Halo'
print(videogame_boss)
print(videogame_boss_copy)

videogame_boss['power'] = True
print(videogame_boss)
print(videogame_boss_copy)

videogame_boss_copy['power'] = False
print(videogame_boss)
print(videogame_boss_copy)


