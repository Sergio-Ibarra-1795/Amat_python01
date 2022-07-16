from car import Car 

#Creación de clases hijos
class MovieCar (Car): #MovieCar tendrá todos los atributos y métodos de Car
    """Represents a movie Car (inhereted from Car)"""
    def __init__(self,brand,year):
        """Initialize attributes of the parent Car"""
        super().__init__(brand,year) #Con esto se herada los atributos y métodos del padre 
        self.movie ='Unknown'
        self.__price = 1000000
    def show_movie(self):
        """Shoe the movie where the car appears"""
        print(f'This car appear in {self.movie}')
    def set_movie (self,movie):
        """Change/Assing the movie to a car"""
        self.movie = movie
    def start_engine(self): #  Este método va a sobre esribir y anular al del padre
        print(f'El auto de película no se puede encender')