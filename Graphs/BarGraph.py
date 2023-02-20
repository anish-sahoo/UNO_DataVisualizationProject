import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]

# labels for bars
tick_label = ['Hershey', 'M&M', 'Toblerone', 'Lindt', 'Yorks']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
		width = 0.8, color = ['brown', 'blue'])

# naming the x-axis
plt.xlabel('Chocolate Name')
# naming the y-axis
plt.ylabel('Chocolate Rating')
# plot title
plt.title('Chocolate Name vs Chocolate Rating')

# function to show the plot
plt.show()
