import os

try:
    import pandas as pd
    from matplotlib import pyplot as plt
except ImportError:
    os.system('pip install pandas')
    os.system('pip install matplotlib')
    import pandas as pd
    from matplotlib import pyplot as plt


def show_graph_5(fsize, color):
    # plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = (8, 6)
    plt.rcParams["figure.subplot.bottom"] = 0.2
    plt.rcParams["figure.subplot.right"] = 0.86
    columns = ["restweek_hrs_12"]
    df = pd.read_csv("../../Downloads/UNO_DataVisualizationProject-main/childlabour_6Feb2019CSVversion.csv", usecols=columns)

    cl = ['green', 'red', 'gray', 'black']  # default
    if color == 1 or color == 2:
        cl = ['#004C83', '#A27A01', '#7D7D7D', '#000000']  # deuteranopia/protanopia
    elif color == 3:
        cl = ['#68CCEE', '#EE3168', '#7D7D7D', '#000000']  # tritanopia

    a = df.restweek_hrs_12.to_list()
    l1 = [] # find all the unique values in this column
    for item in a:
        if item not in l1:
            l1.append(item)

    counts = [] # count how many times each of those unique values appear
    for item in l1:
        ct = 0
        for j in range(len(a)):
            if item == a[j]:
                ct += 1
        counts.append(ct)

    l1[l1.index(-7)] = "Undefined"

    str_list = []
    print(l1)
    for i in range(0, 4): # format the labels
        if l1[i] != 'Undefined':
            str_list.append(str(l1[i]) + " Hrs")
        else:
            str_list.append("Undefined")

    _, _, autotext = plt.pie(counts, labels=str_list, autopct='%1.1f%%', textprops={'fontsize': fsize}, colors=cl)
    for i in autotext:
        i.set_color('white')
    plt.autoscale(enable=True)
    plt.xlabel('How many hours per week \nof rest do governments guarantee?', fontsize=fsize, color='gray')
    plt.show()