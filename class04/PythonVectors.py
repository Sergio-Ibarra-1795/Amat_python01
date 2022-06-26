import numpy as np
first_vector = np.array([1, 12, 14, 9, 5])
print(first_vector)
print(type(first_vector))

y = np.array([2, 3, 3, 4, 2])

z = first_vector + y
print(z)
print(type(z))

z2 = first_vector*y
print(z2)


#DOT product is the magnitude of one times the projection of the second onto the first.
# A · B = AB cos θ  
# A · B = 	(Ax î + Ay ĵ + Az k̂) · (Bx î + By ĵ + Bz k̂)	 
 
# A · B = 	Ax î	 · 	Bx î	 + 	Ax î	 · 	By ĵ	 + 	Ax î	 · 	Bz k̂	 
# + 	Ay ĵ	 · 	Bx î	 + 	Ay ĵ	 · 	By ĵ	 + 	Ay ĵ	 · 	Bz k̂	 
# + 	Az k̂	 · 	Bx î	 + 	Az k̂	 · 	By ĵ	 + 	Az k̂	 · 	Bz k̂	 
# A · B = 	AxBx + AyBy + AzBz, 

a = np.array([5, 10, 2])
b =np.array([2, 4, 3])
dotproduct = np.dot(a,b)
print('Dot product is:', dotproduct)


#Matrix multiplication
p = ([2,5],[3,2])
q = ([1,0],[4,1])
dotproductM = np.dot(p,q)
print(dotproductM)
print(len(p))
print(p)


#Cross product in vectors  To find the cross product of two vectors, we will use numpy cross() function.
r = [4, 2]
s = [5, 6]
productCross = np.cross(r,s)
print(productCross)


# Taking the inverse of a 3 * 3 matrix
OriginalA = np.array([[6, 1, 1],  [4, -2, 5], [2, 8, 7]])
print(OriginalA)

# Calculating the inverse of the matrix
print(np.linalg.inv(OriginalA))


# Inverses of several matrices can
# be computed at once
OriginalAyA = np.array([[[1, 2], [3, 4]],    [[1, 3], [3, 5]]])

print(np.linalg.inv(OriginalAyA))

input1 = ([2,5,4], [5,4,7],[5,6,9])
input2 = ([6,4,5],[5,4,7],[5,3,9])
print(type(input1))
print(type(input2))

input1 = np.array(([2,5,4], [5,4,7],[5,6,9]))
input2 = np.array(([6,4,5],[5,4,7],[5,3,9]))
print(type(input1))
print(type(input2))
print(input1.dot(input2)) #Matrix multiplication

#Recordar que mxn es renglones por columnas y para poderser multiplicar mxn *  kxp   n=k, es decir al número 
# de columnas de la primer matriz igual al de renglones de la segunda  
input3 = np.array(([2,5,4], [5,4,7]))
input4 = np.array(([6,4],[5,4],[5,3]))
print(type(input3))
print(type(input4))
print(input3.dot(input2)) #Matrix multiplication


input5 = np.array([2,5,4])
input6 = np.array(([6,4],[5,4],[5,3]))
print(type(input5))
print(type(input6))
print(input5.dot(input6)) #Matrix multiplication

#np matmul es equivalente e A.dot(B) 
print(np.matmul(input5,input6)) #Matrix multiplication

matrix_object = np.mat([[1, 2],
                        [1, 2],
                        [1, 2]])
print(matrix_object)
print(type(matrix_object))

input3 = np.array(([2,5,4], [5,7,7]))

print(np.matmul(matrix_object,input3))



OriginalB = np.array([[6, 1, 1],  [4, -2, 5], [4, -2, 4]])
print(OriginalB)

# Taking particular elements of a matrix or a vector
print(np.linalg.inv(OriginalB))

print(OriginalB[0])
print(OriginalB[1])
print(OriginalB[2])
print(OriginalB[0:2])


vector_velocidad = np.array([1, 13, 15, 9, 5])
velocidad_enY = vector_velocidad [1]
print(velocidad_enY)
print(type(velocidad_enY))




