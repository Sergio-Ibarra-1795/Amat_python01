# A government wanta to provide student loans to students in their contry. 
# But in-order for a student to be elegible to get a student loan, he/she must be in age range 17 to 21, and must have a minimum 0f 80% score in a cademics. 
# Write a program to accept the name, age and marks of students and display if he/she is elegible for the loan or not. 

#name = input ("Please write your name:")
#ge = int(input ("Please write your age: "))
#grade = int(input ("Please write your grade in a 1-100 scale: "))

#if (age>=17 and age<=21 and grade>=80):
#     print(f"{name}, CONTRTULATIONS! You are elegible for the loan")
#elif (age<17 or age>21):
#     print (f"{name}, You are out of age range to be elegible for the loan")
#elif (grade<80):
#     print (f"{name}, You are out of grade range to be elegible for the loan")




#Check if the nth power of a number is even or not. (Take the number. and the power as input) 

#base = int(input("Enter the base:"))
#power = int(input("Enter the power:"))
#result = base**power 

#if (result%2==0):  #If result divided by 2 give us a reminder of cero 
#    print(f"{result} is even")
#else:
#    print(f"{result} is odd")





#Check if a triangle is a right angle triangle or isoceles triangle 

#a = int(input("Enter the first side:"))
#b = int(input("Enter the second side:"))
#c = int(input("Enter the third side:"))

#if (a == (b**2 + c**2)**(1/2)):
#    print("This is a rectangle triangle" )
#elif (a==b or a==c or b==c):
#    print("This is an iscoceles triangle")
#elif (a==b and a==c and b==c):
#    print("This is an equilater triangle")
#else: 
#    print("This is a scalene triangle")



#Check if the character enter by the user is an uppetcase or lower case character

character = input("Enter your chacater")
ascii_value = ord(character)  #Ord is ised to convert a character in it´s ASCII value 
if (ascii_value>=65 and ascii_value<=90):
    print("Uppercase letter")
elif (ascii_value>=97 and ascii_value<=122):
    print("Lowercase letter")
else:
    print("Character is not an alphabet")







