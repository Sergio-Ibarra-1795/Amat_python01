#ClASES EN PYTHON. 
#Creando clase en python 
from car import Car
from car import MovieCar

doc_brown = Car('Dlorian',1983)
print(type(doc_brown))
print((doc_brown.year))
print((doc_brown.brand))

Toreto_Car =Car('Dodge Carger',1970)
print(Toreto_Car.year)

Christine =Car('Furry',1985)
print(Christine.brand)

# hasta este momento nuestro coche no puede encencer. . Se definió un mpetodo strat_egine()

Christine.start_engine()
print(Toreto_Car.status)
Toreto_Car.start_engine()
print(Toreto_Car.status)

doc_brown.show_engine_status()

print(Toreto_Car.color)
Toreto_Car.color = 'black'
print(Toreto_Car.color)


print(doc_brown.odometer)
doc_brown.change_odometer(90)
print(doc_brown.odometer)


#Creando un auto de pelicula

doc_brown_movie = MovieCar('Delorian', 1983)
print(type(doc_brown_movie))
doc_brown_movie.show_engine_status()
doc_brown_movie.start_engine()
doc_brown_movie.show_engine_status()

print(doc_brown_movie.odometer)
#doc_brown_movie.change_odometer(500)
print(doc_brown_movie.odometer)

print(doc_brown_movie.show_movie())
doc_brown_movie.set_movie('La PELICULA')
print(doc_brown_movie.show_movie())
doc_brown_movie.start_engine()

print(doc_brown_movie.prueba)

print(doc_brown_movie.odometer)




