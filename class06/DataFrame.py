import pandas as pd
import numpy as np

#Building a data frame drom a dictionary 
dictionary1 = {"col1": [1, 2], "col2": [3, 4]}
print(dictionary1)
print(type(dictionary1))

df1 = pd.DataFrame(dictionary1)
print(df1)
print(type(df1))


#Building a data frame drom a dictionary including series
dictionary2 = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
print(dictionary2)
print(type(dictionary2))

df2 = pd.DataFrame(data=dictionary2, index=[0, 1, 2, 3])
print(df2)
print(type(df2))



# Constructing DataFrame from numpy ndarray:


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
print(array)
print(type(array))

df3 = pd.DataFrame(array, columns=['a', 'b', 'c'])
print(df3)
print(type(df3))




