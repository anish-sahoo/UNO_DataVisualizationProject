import csv
import matplotlib.pyplot as plt

labels = []  # list for storing labels (1st column)
values = []  # list for storing values (22nd column)

with open(r'C:\Users\mihir\Downloads\modified childlabour_6Feb2019CSVversion.csv') as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    for row in reader:
        if row[0] and row[21]:  # check if 1st and 22nd columns are not empty
            labels.append(row[0])
            values.append(int(row[21]))

plt.bar(labels, values)
plt.title('Child Labor Data')
plt.xlabel('Country')
plt.ylabel('minage_light_age_95')
plt.show()
