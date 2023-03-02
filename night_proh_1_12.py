import os

try:
    import pandas as pd
    from matplotlib import pyplot as plt
except ImportError:
    os.system('pip install pandas')
    os.system('pip install matplotlib')
    import pandas as pd
    from matplotlib import pyplot as plt


def show_graph_4(fsize, color):

    #plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = (15, 9)
    columns = ["night_proh_1_12"]
    df = pd.read_csv("../../Downloads/UNO_DataVisualizationProject-main/childlabour_6Feb2019CSVversion.csv", usecols=columns)
    cl = ['green', 'red', 'gray']  # default

    if color == 1 or color == 2:
        cl = ['#004C83', '#A27A01', '#7D7D7D']  # deuteranopia/protanopia
    elif color == 3:
        cl = ['#68CCEE', '#EE3168', '#7D7D7D']  # tritanopia

    a = df.night_proh_1_12.to_list()
    b = [0, 0, 0]  # counters for yes, no and unknown

    for i in range(len(a)):
        if a[i] == 'Yes':
            b[0] += 1
        elif a[i] == 'No':
            b[1] += 1
        else:
            b[2] += 1

    c = ['Yes', 'No', 'Unknown']
    plt.barh(c, b, color=cl)
    plt.autoscale(enable=True)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize, rotation=45)
    plt.xlabel('Do Countries restrict nightime work for children?', fontsize=fsize + 2, color='gray')

    plt.show()
