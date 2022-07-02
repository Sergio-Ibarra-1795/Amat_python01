antizombie_weapons = ['ballesta','escopeta','pistola']
another_list = ['yo soy string',True,'pistola', 2, 5.5]
another_list2 = ['yo soy string',[1,2,3]]

print(type(antizombie_weapons))
print(type(another_list))
print(type(another_list2))


print(antizombie_weapons)
print(another_list)
print(another_list2)

#Accediendo a elementos 
print(antizombie_weapons[0])
print(antizombie_weapons[1])
print(antizombie_weapons[-3])
print(len(antizombie_weapons))


#Utilizando valores de una lista
print('Puedes acabar con un zombie si utilizas una:'+ antizombie_weapons[2])

#Camios en una lista  lista
antizombie_weapons [0] = 'katana'
print(antizombie_weapons)

# antizombie_weapons [0,1] = 'katana', 'granada'
# print(antizombie_weapons)

#Agregando valor al final de la lista
antizombie_weapons.append('snifer de rifle')
print(antizombie_weapons)

antizombie_weapons.append(0.2)
print(antizombie_weapons)

#Agregando elementos de una lista al final de otra lista
antizombie_weapons2 = ['magnum','berreta']

antizombie_weapons.extend(antizombie_weapons2)
print(antizombie_weapons)


#Agregando valor en alguna posición de la lista
antizombie_weapons.insert(1, 'javelin')
print(antizombie_weapons)

#Eliminando elemento en alguna posición de la lista
del antizombie_weapons [3]
print(antizombie_weapons)

#Eliminando de elementos con pop (último elemento) 
erased_element = antizombie_weapons.pop()
print(antizombie_weapons)
print(erased_element)

#Eliminando cualquier elemento con pop (definiendo la posición dentro de pop) 
erased_element2 = antizombie_weapons.pop(0)
print(antizombie_weapons)
print(erased_element2)

erased_element3 = antizombie_weapons.pop(3)
print(antizombie_weapons)
print(erased_element3)

#Eliminando elemento por valor
antizombie_weapons.remove('snifer de rifle')
print(antizombie_weapons)

antizombie_weapons.insert(3, 'snifer de rifle')
print(antizombie_weapons)


antizombie_weapons.insert(3, 'snifer de rifle')
print(antizombie_weapons)

antizombie_weapons.remove('snifer de rifle')
print(antizombie_weapons)

#Ordenando una lista por valores  (orden alfabético)

antizombie_weapons.sort()
print(antizombie_weapons)

antizombie_weapons3 = ['ballesta','Rifle de medio alcanze' ,'escopeta','pistola']
antizombie_weapons3.sort()
print(antizombie_weapons3)

#Ordenando una lista por valores  (orden alfabético a la inversa)
antizombie_weapons.sort(reverse=True)
print(antizombie_weapons)

#Ordenando una lista por valores  (orden alfabético sin modifixar los indices de la lista original)
print(sorted(antizombie_weapons))
print(antizombie_weapons)


#Ordenando una lista por valores  (orden alfabético a la inversa)
antizombie_weapons.reverse()
print(antizombie_weapons)


#Conocer si un elemento está en una lista 
answer = 'escopeta' in antizombie_weapons
print(answer)

#Concatenación de listas 
new_weapons = antizombie_weapons + antizombie_weapons2
print(new_weapons)


#Inicialización de listas 
new_weapons = antizombie_weapons + antizombie_weapons2
print(new_weapons)


#Minimo de una lista
money = [200, 201, 205, 207]
print(min(money))

#Máximo de una lista
print(max(money))

#Obtener indice de un elemento
money = [200, 201, 205, 207, 201]

print((money.index(201)))


# money2 = [208, 209, 210, 211, 211]
# money3 = money * money2 
# print(money3)


#Recorrer los elementos de listas.  For cada elemento al que yo llamé arbotrariaomente armas en la lista pedí que me l imprimiera. 
print(antizombie_weapons)
for armas in antizombie_weapons: 
    print(armas)

print('Estoy fuera del for')
print(armas)


#RANGE  para generar listas numericas 
numbers = list(range(1,12))
print(numbers)


#Uso de slides en listas
print(antizombie_weapons)
print(antizombie_weapons[1:3])
print(antizombie_weapons[:4])

print(len(antizombie_weapons))

antizombie_weapons[4:] = ['fugoneta', 'navaja']
print(antizombie_weapons)

antizombie_weapons[2:4] = []
print(antizombie_weapons)

counter = 1 
print(antizombie_weapons)
for armas in antizombie_weapons: 
    print(armas)
    print(f'estamos en {counter}')
    counter += 1 

print('Estoy fuera del for')
print(armas)



