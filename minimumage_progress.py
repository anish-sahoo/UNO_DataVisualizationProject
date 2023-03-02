import os

try:
    import pandas as pd
    from matplotlib import pyplot as plt
    import numpy as np
except ImportError:
    os.system('pip install pandas')
    os.system('pip install matplotlib')
    os.system('pip install numpy')
    import pandas as pd
    from matplotlib import pyplot as plt
    import numpy as np


def show_graph_6(fsize, color):
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = (14, 4)

    columns = ["minage_gen_age_95", "minage_gen_age_96", "minage_gen_age_97", "minage_gen_age_98",
               "minage_gen_age_99", "minage_gen_age_00", "minage_gen_age_01", "minage_gen_age_02",
               "minage_gen_age_03", "minage_gen_age_04", "minage_gen_age_05", "minage_gen_age_06",
               "minage_gen_age_07", "minage_gen_age_08", "minage_gen_age_09", "minage_gen_age_10",
               "minage_gen_age_11", "minage_gen_age_12"]

    df = pd.read_csv("../../Downloads/UNO_DataVisualizationProject-main/childlabour_6Feb2019CSVversion.csv", usecols=columns)
    list_of_columns = []

    list_of_columns.append(df.minage_gen_age_95.to_list())
    list_of_columns.append(df.minage_gen_age_96.to_list())
    list_of_columns.append(df.minage_gen_age_97.to_list())
    list_of_columns.append(df.minage_gen_age_98.to_list())
    list_of_columns.append(df.minage_gen_age_99.to_list())
    list_of_columns.append(df.minage_gen_age_00.to_list())
    list_of_columns.append(df.minage_gen_age_01.to_list())
    list_of_columns.append(df.minage_gen_age_02.to_list())
    list_of_columns.append(df.minage_gen_age_03.to_list())
    list_of_columns.append(df.minage_gen_age_04.to_list())
    list_of_columns.append(df.minage_gen_age_05.to_list())
    list_of_columns.append(df.minage_gen_age_06.to_list())
    list_of_columns.append(df.minage_gen_age_07.to_list())
    list_of_columns.append(df.minage_gen_age_08.to_list())
    list_of_columns.append(df.minage_gen_age_09.to_list())
    list_of_columns.append(df.minage_gen_age_10.to_list())
    list_of_columns.append(df.minage_gen_age_11.to_list())
    list_of_columns.append(df.minage_gen_age_12.to_list())

    averages = []
    for i in range(len(list_of_columns)):
        sum = 0
        count = 0
        for j in list_of_columns[i]:
            if j > 0:
                sum += j
                count += 1
        averages.append(sum / float(count))

    years = []
    for i in range(1995, 2013):
        years.append(i)

    cl = '#004C83'  # default

    if color == 1 or color == 2:
        cl = '#A27A01'  # deuteranopia/protanopia
    elif color == 3:
        cl = '#EE3168'  # tritanopia

    plt.scatter(years, averages, color=cl, s=100)
    plt.xlim(1995, 2012)
    plt.ylim(12, 18)
    plt.xticks(np.arange(min(years), max(years) + 1, 1.0))
    # plt.yticks(np.arange(14, 16, 0.5))
    plt.xticks(years, years, rotation=45)
    plt.autoscale(enable=True)
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)
    plt.xlabel('Change in average minimum working age\nfor children over the years', fontsize=fsize - 4, color='gray')

    plt.show()
