# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3,4,5]
# corresponding y axis values
y = [0,2,3,9,14]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Eeshaans threat level')
# naming the y axis
plt.ylabel('Mihirs pun level')

# giving a title to my graph
plt.title('Threats vs puns')

# function to show the plot
plt.show()
