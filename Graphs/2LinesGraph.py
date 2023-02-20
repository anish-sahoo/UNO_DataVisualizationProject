import matplotlib.pyplot as plt

# line 1 points
x1 = [1,2,3]
y1 = [3,7,14]
# plotting the line 1 points
plt.plot(x1, y1, label = "Mihir")

# line 2 points
x2 = [1,2,3]
y2 = [7,3,0]
# plotting the line 2 points
plt.plot(x2, y2, label = "Eeshaan")

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Pun Score')
# giving a title to my graph
plt.title('Best Puns')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
