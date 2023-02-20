import matplotlib.pyplot as plt

# defining labels
activities = ['Mihir', 'Anish', 'Swayam', 'Eeshan']

# portion covered by each label
slices = [90, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
		startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
		radius = 1.2, autopct = '%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()
