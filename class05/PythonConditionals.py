#Condicionales

# language = input('Cuál es tu lenguaje favorito:')

# if language =='R'or 'r'or 'Erre':
#     print('Te gusta la estadistica')
# elif language == 'Python':
#     print('Eres un viejo lobo de mar')
# elif language == 'Ruby':
#     print('Eres un hacker')
# else: 
#     print('No conozco ese lenguaje')
    

language = input('Cuál es tu lenguaje favorito?:')
language = language.lower() #Transforma el input en lowercase 

if language =='r':
    print('Te gusta la estadistica')
elif language == 'python':
    print('Eres un viejo lobo de mar')
elif language == 'ruby':
    print('Eres un hacker')
else: 
    print('No conozco ese lenguaje')