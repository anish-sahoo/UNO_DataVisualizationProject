import os

try:
    import pandas as pd
    from matplotlib import pyplot as plt
except ImportError:
    os.system('pip install pandas')
    os.system('pip install matplotlib')
    import pandas as pd
    from matplotlib import pyplot as plt


def show_graph_2(fsize, color):
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = (10, 7)
    columns = ["minage_gen_age_12"]
    df = pd.read_csv("childlabour_6Feb2019CSVversion.csv", usecols=columns)
    cl = ['green', 'red', 'green', 'red', 'green', 'red', 'green']  # default

    if color == 1 or color == 2:
        cl = ['#004C83', '#A27A01', '#004C83', '#A27A01', '#004C83', '#A27A01', '#004C83']  # deuteranopia/protanopia
    elif color == 3:
        cl = ['#68CCEE', '#EE3168', '#68CCEE', '#EE3168', '#68CCEE', '#EE3168', '#68CCEE']  # tritanopia

    a = df.minage_gen_age_12.to_list()
    b = [0, 0, 0, 0, 0, 0, 0]  # counters for yes, no and unknown

    for i in range(len(a)):
        if a[i] == 12:
            b[0] += 1
        elif a[i] == 13:
            b[1] += 1
        if a[i] == 14:
            b[2] += 1
        elif a[i] == 15:
            b[3] += 1
        elif a[i] == 16:
            b[4] += 1
        elif a[i] == 17:
            b[5] += 1
        else: b[6] += 1

    c = ['12', '13', '14', '15', '16', '17', '18']
    plt.bar(c, b, color=cl)
    plt.autoscale(enable=True)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)
    plt.xlabel('Minimum Working Age enforced by Laws', fontsize=fsize + 2, color='gray')

    plt.show()