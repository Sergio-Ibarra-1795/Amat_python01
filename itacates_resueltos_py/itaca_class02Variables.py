#language = "Python"
#author = "Guido Van R"
#role = "Dictador de por vida"
#end_date = "Julio 2018"

#print ("Mi lengiaje favorito es {} y su creador es {} quien tuvo el puesto de {} hasta {}" .format(language,author,role,end_date))

# 1. Escribe un programa que le pida su nombre al usuario y como salida
# le diga cuantos caracteres tiene su nombre.
#message1 = input("Escribe tu nomnbre: ")
#print(message1)
#len_name = len(message1)
#len_name_str = str(len_name)
#print("Tu nombre tiene" + " "+ len_name_str + " " + "letras")

# 2. Escribe un programa que le pida primero su nombre al usuario, posteriormente
# su apellido, crea una variable de nombre completo concatenando el nombre y el
# apellido y muestra en pantalla un mensaje de bienvenida utilizando la variabla
# con el nombre completo.
#message2 = input("Escribe tu nombre:")
#message2_1 = input ("Escribe tu apellido:")
#print("Hola" + " " + message2 + "_" + message2_1 + " " + "bienvenido a python")


# 3. Escribe un programa que le pida primero el nombre de su deporte favorito, posteriormente
# se le pide al usuario su edad. Muestra en pantalla el nombre del deporte el número
# de veces igual a la edad del usuario.
#print ("Python " *3)
#message3 = input("Escribe el nombre de tu deporte favorito:")
#message3_1 = input("¿Cuantos años tienes?: ")
#edad_multiplicador = int(message3_1)
#print (message3 * edad_multiplicador)


# 4. Escribe un programa que al proporcionarle la siguiente clave HomeroSimpson1970SpringfieldUSA
# nos guarde el nombre, apellido, año, estado y país en variables independientes y
# porteriormente muestra en pantalla un mensaje de bienvenida utilizando las variables.
#message4 = input ("Escribe la clave de Homero: ")
#message_split = message4.split()
#print(message_split)

# NO PUDE HACER EL EJERCIO 4, VOY A PREGUNTARLE A GOZ

# 5. Escribe un programa que te permita ingresar dos numeros enteros y como salida
# de el resultado de la suma.
#message5 = input("Escribe un múmero del 1 al 100: ")
#message5_1 = input("Escribe un múmero del 100 al 200: ")
#primer_numero = int(message5)
#segundo_numero = int(message5_1)
#suma = primer_numero + segundo_numero
#suma_string = str(suma)
#print ("La suma de los números que elegiste es:" + suma_string)


# 6. Escribe un programa que te permita ingresar dos numeros enteros y como salida
# de el resultado de concatenar los dos números.
#message6 = input("Escribe un número: ")
#message6_1 = input("Escribe otro número: ")
#print("Los número que elegiste fueron {0} y {1}".format(message6, message6_1)) 
#print("Los números que elegiste fueron" +" " + message6 + " " + "y" + " " + message6_1)

# 7. Escribe un programa que te permita ingresar una cadena de texto y el resultado
# sea esa misma cadena pero en orden totalmente invertido.

#message7 = input("Escribe tu color favorito: ")
#stringlenght = len(message7)
#sliceString = message7 [:: -1]
#print(sliceString)

#message7 = input("Escribe tu color favorito: ")
#reversed_message ='' .join(reversed(message7))
#print(reversed_message)

# 8. Escribe un programa que te permita ingresar una cadena de texto, porteriormente
# el programa solicita una cadena a reemplazar, y luego solicita el valor por el
# cual se reemplazara, como resultado el programa presenta la cadena original pero
# con el reemplazo indicado.
# NO ENTENDÍ LA INDICACIÓN


# 9. Escribe un programa que te permita ingresar una cadena de texto y la salida
# sea la misma cadena pero con todas las letras en mayúsculas.
#message9 = input("Quién es tu artista favorito?: ")
#print("Tú artista favorito es" + " " +  message9.upper())


# 10. Escribe un programa que te permita ingresar una cadena de texto y el programa
# indique si la cadena tiene esta formada por caracteres numéricos.
# NO PUDE HACERLO






# 14. Generador de cuentos
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente comenzará a
# preguntarle al usuario lo siguiente: el nombre del usuario, edad, lugar, animal, país,
# comida, color, profesión, parte del cuerpo.
# La salida del programa debe ser un cuento con la siguiente estructura:
#print("Hola, cosntruyamos juntos una pequeña historia")
#nombre = input("¿Cómo te llamas?: ")
#edad = input("¿Cúantos años tienes?: ")
#animal = input("¿Cuál es tu animal favorito?: ")
#pais = input("¿Qué país te gustaría visitar?: ")
#comida = input("¿Cuál es tu comida favorita?: ")
#color = input("Escribe un color que te guste: ")
#profesion = input ("¿Cuál es tu profesión?: ")
#parte_cuerpo = input ("Escribe una parte del cuerpo: ")
#print("A los {0} años {1} se fue de viaja a {2}. Su trabajo de {3} le permitió visitar este lejano lugart en el pudo comer {4}. Lamentablemente terminó visitando al doctor ya que su {5} se hinchó y se puso de color {6} por estar jugando con un {7} que casualmente se encontró en el lugar" .format(edad, nombre, pais, profesion, comida, parte_cuerpo, color, animal))



#HomeroSimpson1970SpringfieldUSA

print("Bienvenido a nuestro programa")
print("Porfavor ingrese su clave: ")
key = input()

name = key[0:6]
lastname = key[6:13]
#Aquí se puede observar el intervalo cerrado al inicio y abierto al final 
year = key[13:17]
state = key[17:28]
country = key[28:]

print ("Bienvenido" + " " + name + " " + lastname + " " + "Nacido en" + " " + year + "en" + state + country)


