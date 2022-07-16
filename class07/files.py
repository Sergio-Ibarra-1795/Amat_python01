#Archivos en PYTHON 
file = open(r'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\paises.txt')
contents=file.read()
print(contents)
file.close()

#with open('C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\paises.txt') as file_object:
#    content=file_object.read()
#    print(content)

with open ('paises2.txt', 'a') as file_object:
    file_object.write('España')

