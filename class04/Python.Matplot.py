# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points 
#plt.plot(x, y)
#plt.show()

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
#plt.show() comentando para poder ejecutar otros comandos 




# x axis values
x2 = [1,2,3,4,5,6]
# corresponding y axis values
y2 = [2,4,1,5,2,6]
  
# plotting the points 
#plt.plot(x2, y2, color='green', linestyle='dashed', linewidth = 3,
 #        marker='o', markerfacecolor='blue', markersize=12)
  
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
  
# naming the x axis
plt.xlabel('x2 - axis')
# naming the y axis
plt.ylabel('y2 - axis')
  
# giving a title to my graph
plt.title('Some cool customizations!')
  
# function to show the plot
#plt.show()



# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5]
  
# heights of bars
height = [10, 24, 36, 40, 5]
  
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']
  
# plotting a bar chart
#plt.bar(left, height, tick_label = tick_label,
 #       width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My first bar chart!')
  
# function to show the plot
#plt.show()



#SCATERED- POINT GRAPHS 

# x-axis values
x3 = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y3 = [2,4,5,7,6,8,9,11,12,12]
  
# plotting points as a scatter plot
#plt.scatter(x3, y3, label= "stars", color= "green", 
 #           marker= "*", s=30)

# setting x and y axis range
plt.ylim(1,15)
plt.xlim(1,15)


# x-axis label
plt.xlabel('x3 - axis')
# frequency label
plt.ylabel('y3 - axis')
# plot title
plt.title('My first scatter plot!')
# showing legend
plt.legend()
  
# function to show the plot
#plt.show()




# HISTOGRAMA frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,
        60,7,13,57,18,90,77,32,21,20,40]
  
# setting the ranges and no. of intervals
range = (0, 100)
bins = 10  

# plotting a histogram
plt.hist(ages, bins, range, color = 'green',
        histtype = 'bar', rwidth = 0.8)

# setting x and y axis range
plt.ylim(1,10)
plt.xlim(1,100)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')
  
# function to show the plot
plt.show()


