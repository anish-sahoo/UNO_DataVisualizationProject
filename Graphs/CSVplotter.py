import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [9.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.ylim((11, 17))

columns = ["country", "minage_gen_age_95"] # tell python which columns to read
df = pd.read_csv("C:\\Users\\anish\\Downloads\\childlabour_6Feb2019CSVversion.csv", usecols=columns)

a = df.country.to_list()[10:20]  # select elements of index 10-20
b = df.minage_gen_age_95.to_list()[10:20]  # select elements of index 10-20

fig = plt.scatter(a, b)
plt.xticks(fontsize=8)
plt.show()
