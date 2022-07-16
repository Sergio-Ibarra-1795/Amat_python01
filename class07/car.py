class Car: #Estamos creando la clase Car
    """"A simple attemp to model a car"""
    def __init__(self,brand,year): #Estamos iniciando la clase car y diciendo que para definir un objeto de esa clase necesitaremos su marca y su año 
        """Initialize brand and year attributes"""
        self.brand = brand #La marca del coche será la que se indque al crear el objeto coche de la clase Car
        self.year = year
        self.status ="off" #No es necesario pedir todos los atributos para inicializar el objeto
        self.color ="" #Se inicializa el atributo sin color para despues pintarlo con un mpetodo
        self.odometer = 10
        self.prueba = True 
    def start_engine(self): #Se está definiendo el método para "encender el coche"
        """Simulates a car stasrting it´s engine"""
        self.status = "on" #Dentro de la misma clase puedo cambiart un atributo en un método
         #print(f'Your{self.brand} engine is on')
    def show_engine_status(self):
        """Show engine status"""
        print(f'Your {self.brand} engine is {self.status}')
    
    def change_odometer(self,value):
        """"Change odometer value"""
        self.odometer = value
        print(f'The odometer value was set at: {self.odometer}')



#Creación de clases hijos
class MovieCar (Car): #MovieCar tendrá todos los atributos y métodos de Car
    """Represents a movie Car (inhereted from Car)"""

    def __init__(self,brand,year):
        """Initialize attributes of the parent Car"""
        super().__init__(brand,year) #Con esto se herada los atributos y métodos del padre 
        self.movie ='Unknown'
    def show_movie(self):
        """Shoe the movie where the car appears"""
        print(f'This car appear in {self.movie}')
    def set_movie (self,movie):
        """Change/Assing the movie to a car"""
        self.movie = movie
    def start_engine(self): #  Este método va a sobre esribir y anular al del padre
        print(f'El auto de película no se puede encender')