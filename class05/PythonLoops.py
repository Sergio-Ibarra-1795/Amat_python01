from random import * 

#Loops con while 

current_lap = 1 
while current_lap <= 14:
    print(f'Piloto de Mcclaren va en la vuelta {current_lap}')
    current_lap += 1



#Permitir al usuario salir del loop
car_status = 'Good'
current_lap = 1 
while current_lap <= 17 and car_status =='Good':
    print(f'Piloto de Mcclaren va en la vuelta {current_lap}')
    car_status = 'Bad'
    current_lap += 1

#Uso de bandera en un loop

flag = True 
while flag: 
    status = input('Está la bandera ondeando? s/n')
    if status =='s':
        print('Baje su velocidad, la carrera está en pausa')
    elif status =='n':
        print('Continue carrera')
        flag = False #Para salir del loop 



# #Uso de brak para salir de loop
# car = 'bueno'
# current_lap = 1
# while current_lap <= 26 and car == 'bueno':
#     print('Estamos en la vuelta ' + str(current_lap))
#     car = input('¿Cuál es el estado del auto?')
#     computer_failure = randrange(9)
#     if computer_failure == 7:
#         print('La computadora ha fallado')
#         break #Sale del loop si el randrange obtiene un número igual a 7 
#     current_lap += 1
# print('Termino la carrera!')



#Uso de brak para salir de loop
car = 'bueno'
current_lap = 1
while current_lap <= 26 and car == 'bueno':
    print('Estamos en la vuelta ' + str(current_lap))
    #car = input('¿Cuál es el estado del auto?')
    computer_failure = randrange(9)
    if computer_failure == 7:
        print('La computadora ha fallado')
        break #Sale del loop si el randrange obtiene un número igual a 7 
    current_lap += 1
print('Termino la carrera!')


# Uso del continue dentro loop
in_race = True
while in_race:
    print("Seguimos en la carrera")
    tires_status = input("Las llantas están bien?")

    if tires_status == 'no':
        print("Entrando a pits")
        print("Cambiando llantas")
        print("Saliendo de pits")
        continue
    else:
        print("No necesitas entrar a pits")

    computer_status = input("La computadora están bien?")    
    if computer_status == 'n':
        print("Entrando a pits")
        print("Arreglando")
        print("Saliendo de pits")
        continue
    else:
        print("No necesitas entrar a pits")


    print("Mantente hidratado y acepera campeon/a")
    keep_in_race = input("Quiéres seguir en la carrera? s/n")
    if keep_in_race == "n":
        in_race = False


