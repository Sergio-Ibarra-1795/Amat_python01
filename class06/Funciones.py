#FUNCIONES EN PYTHON
from cmath import pi
import math
from unittest import result


def say_hi():
    """Welcome message"""
    print('Hello')

say_hi() #Para mandar a llamar a una función 



#Pasando información a una función
def say_hi2(name):
    """"Custome welcome message"""
    print(f'Hi {name}')

say_hi2('Serg')


# radio = int(input('Cuál es el radio en cm'))
# def circle_area(radio):
#     """"Circle area function"""
#     area = pi*(radio**2)
#     print(f'El área del cirucolo es {area} cm')

# circle_area(radio)


# largo = int(input('Cuál es el largo en cm'))
# ancho = int(input('Cuál es el ancho en cm'))
# def rectangle_area(largo,ancho):
#     """"Recntangle area function"""
#     area = largo*ancho
#     print(f'El área del rectangulo es {area} cm')

# rectangle_area(largo,ancho)


#EJEMPLO DE ARGUMENTOS POR KEY-WORD
def hello (name, lastname):
    """"Hello message"""
    print(f'Hi {name} {lastname}')

hello(lastname='Ibarra',name='Sergio')


#EJEMPLO DE ARGUMENTOS DEFAULT
def hello2 (name, lastname='Clasificado'):
    """"Hello message"""
    print(f'Hi {name} {lastname}')

hello2 (name='Sergio')




#EJEMPLO DE ARGUMENTOS OPCIONALES
def hello3 (name, lastname='Clasificado2',job=''):#Se le está dicioendo que el argumento job es opcional
    """"Hello message"""
    print(f'Hi {name} {lastname} {job}')

hello3 (name='Sergio',job='Consultoria')


#EJEMPLO DE ARGUMENTOS ARBITRARIOS
def create_pizza(*toppings): 
    """"Create custom pizza for clients"""
    for topping in toppings:
        print(f'Su pizza tiene {topping}')
    
create_pizza('jamon','piña','extra queso')


print(math.sin(90))



#Retorno de valores 
def my_super_sum (value1, value2):
    result = value1 + value2
    return result



answer = my_super_sum(1.5,2.2)
print(answer)


def OP_Basica(a,b,operacion):
    Resultado=('a'+operacion+'b')
    Resultado=eval(Resultado)
    return Resultado 

OP_Basica(10,5,'*')
Objeto_P=OP_Basica(10,5,'*')
print(Objeto_P)
