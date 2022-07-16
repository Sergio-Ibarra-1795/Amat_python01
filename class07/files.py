#Archivos en PYTHON 
file = open('paises.txt')
contents=file.read()
print(contents)
file.close()

with open('paises.txt') as file_object:
    content=file_object.read()
    print(content)
    