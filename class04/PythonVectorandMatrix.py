import numpy as np 
matrizA = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrizA)
matrizB = np.array([[9],
                   [10],
                   [11]])
print(matrizB)

matrizC = matrizA.dot(matrizB)
print(matrizC)

matrizD = np.mat([[1,2,3],[4,5,6],[7,8,9], [11,12,13]])
print(matrizD)

matrizE = np.mat([[11,12],[14,15],[7,18]])
print(matrizE)

matrizF = np.dot(matrizD,matrizE)
print(matrizF)

# matrizG = matrizD + matrizE
# print(matrizG)
# No se pueden sumar o restar matrices que no tengan el mismo mxn 




