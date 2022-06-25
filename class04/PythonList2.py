#List example
print('Bienvenido a Pizzas Serg') 
print ('Porfavor eliga sus ingredientes:')
ingredientes = """ 
1. peperoni
2. salami
3. piña
4. jamon
5. chorizo
"""
print(ingredientes)

# selected_ingredient = input('Escribe el ingrediente de tu pizaa:')

# pizza_oder = [None, None, None] #Para indicar que pizza order es una listya, por el momento sin elementos 
# pizza_oder.append(selected_ingredient)

selected_ingredient2 = input('Escribe el ingrediente de tu pizaa :):')

pizza_oder2 = [None] *5 #Para indicar que pizza order es una listya, por el momento sin elementos 
pizza_oder2 [1] = selected_ingredient2

print('Su pizza será de' + " "+ pizza_oder2[1])
print(pizza_oder2)


