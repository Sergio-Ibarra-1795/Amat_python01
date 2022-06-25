#PYTHON STRINGS 

from os import symlink


word = "alien" 
print(type(word))

symbol = '@@@@@'
print(type(symbol)) 

text = 'Los marcianos llegaaron ya'
print(type(text))

content_file = 'Los marcianos llegaron ya \n y llegaron bailando'
print(content_file) 

code ='print("esto es código, puede ser de otro lenguaje diferente a python")'
print(type(code))
bytes_content = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(type(bytes_content))
print(bytes_content.decode('utf-16'))

name_1 = 'Martha'
print(name_1)
print(name_1 [1])

name_2 = 'Martha Ramírez'
print(name_2)
print(name_2[7])

my_string1 = 'Con comillas simples'
my_string2 = "Con comillas dobles"
my_string3 = '''
Con comillas triples
se puede 
hacer salto de linea
muy fácil'''
print(my_string3)

my_string4 = """""
Con comillas triples
se puede 
hacer salto de linea
muy fácil
Se puede triple simple comilla o triple doble xD (suena a clavado)"""
print(my_string4)

print('\\')
print("\"")

print('esto es un textoF antes \f esto es un textoF') ; print (" \n")
print('esto es un textoN antes \n esto es un textoN')  ; print (" \n")
print('esto es un textoR antes \r esto es un textoR')  ; print (" \n")
print('esto es un textoT antes \t esto es un textoT')  ; print (" \n")


print('\x40') #Código exadecimal 

escape1 = "Hola, yo soy una \"estupenda\" cadena" #escapé el valor dentro de ""
escape2 = "Hola, yo soy una \"estupenda\" \n \U0001F412 cadena" #escapé el valor dentro de ""
print(escape1)
print(escape2)

# Unicode literales
# https://unicode-table.com/es/
print('\N{GREEK CAPITAL LETTER DELTA}') # unicode database id
print('\u0394') # unicode char 16 bit hex val
print('\U00000394') # unicode char 32 bit hex val

print('\N{Grinning Face with Smiling Eyes}') # unicode database id
print('\U0001F601') # unicode char 32 bit hex val
print('\U0001F412') # unicode char 32 bit hex val

print("hola yo soy una \"estupenda\" \n \U0001F412  cadena ")

my_class03Folder = r"C:\Users\llell\Documents\SIR_PERSONAL\Other_Courses\Python AMAT\ClassesPython01\class03"
print(my_class03Folder)

print(len("my heroe is Batman"))

#Concatenate characteres 
word1 = 'bat'
word2 = 'man'
heroe = word1 + word2 
print(heroe)

#Repeat strings
word3 = 'superman '
print(word3 *10)

#Indexing 
word4 = "Bruce is Batman"
print(word4 [6])

#SLICING
word5 = "Bruce is Batman"
print(word4 [-1]) 
#Empieza a contar deasde atrás con -1 SIN CONTAR EL CERO, que siempre es la primer letra de izquerda a derecha

word6 = "Wayne"
print(word6 [:3])
#0=W, 1=a, 3=y, por lo tanto es intervalo abierto, pues no toma el 3

word6 = "Wayne is batman"
print(word6 [:3])
#0=W, 1=a, 3=y, por lo tanto es intervalo abierto, pues no toma el 3
print(word6 [1:3])
print(word6 [4:])
#En el inicio es intervalo cerrado y en el final es abierto
print(word6 [-6:-3])

malcolm_phrase = "La vida se abre camino"
print(malcolm_phrase[::3]) #Imprtime un caracter si y unono, se puede expandir a 3, 4, etc 
print(malcolm_phrase[::-1]) #Te voltea toda la frase 


#REPLACE STRINGS 

message2 ="Luke I am your mother!!!"
message2 = message2.replace("mother","father")
print(message2)

message3 ="la vida se agre camino"
message3 = message3.capitalize()
print(message3)

print(message3.find("vida"))
print("vida" in message3) #True
print("vidas" in message3) #False

message4 = "La vida se abre camino 2"
print(message3.isnumeric())


#print("Bienvenido a nuestro programa")
print("Porfavor ingrese su clave: ")
key = input()

name = key[0:6]
lastname = key[6:13]
 #Aquí se puede observar el intervalo cerrado al inicio y abierto al final 
year = key[13:17]
state = key[17:28]
country = key[28:]

#print ("Bienvenido" + " " + name + " " + lastname + " " + "Nacido en" + " " + year + "en" + state + country)

print(f'Bienvenido {name} {lastname} nacido en {state}')

# Format strings
phrase_1 = 'power'
phrase_2 = 'responsability'
print('With great %s comes a great %s' % (phrase_1, phrase_2))
print('With great {0} comes a great {1}'.format(phrase_1, phrase_2))
print('With great {text_1} comes a great {text_2}'.format(text_1 = 'power', text_2 = 'responsability'))
print(f'With great {phrase_1} comes a great {phrase_2}')

