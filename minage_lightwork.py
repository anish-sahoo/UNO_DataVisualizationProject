import os

try:
    import pandas as pd
    from matplotlib import pyplot as plt
except ImportError:
    os.system('pip install pandas')
    os.system('pip install matplotlib')
    import pandas as pd
    from matplotlib import pyplot as plt


def show_graph_1(fsize, color):
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = (10, 7)
    columns = ["minage_light_leg_12"]
    df = pd.read_csv("childlabour_6Feb2019CSVversion.csv", usecols=columns)
    cl = ['green', 'red', 'gray']  # default

    if color == 1 or color == 2:
        cl = ['#004C83', '#A27A01', '#7D7D7D']  # deuteranopia/protanopia
    elif color == 3:
        cl = ['#68CCEE', '#EE3168', '#7D7D7D']  # tritanopia

    a = df.minage_light_leg_12.to_list()
    b = [0, 0, 0]  # counters for yes, no and unknown

    for i in range(len(a)):
        if a[i] == 'Yes':
            b[0] += 1
        elif a[i] == 'No':
            b[1] += 1
        else:
            b[2] += 1

    c = ['Yes', 'No', 'Unknown']
    plt.bar(c, b, color=cl)
    plt.autoscale(enable=True)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)
    plt.xlabel('Do laws restrict hours of light work for children?', fontsize=fsize - 4, color='gray')

    plt.show()