from spent import tracker
from collections import Counter

import plotly.graph_objs as go

import plotly
import os
import sys

if __name__ == "__main__":

    input_dir = ""
    file_list = []
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
    else:
        input_dir = input("Enter a directory: ")
    for root, dirs, filenames in os.walk(input_dir):
        for f in filenames:
            if f.endswith(".txt"):
                file_list.append(str(os.path.join(root, f)))

    total_dic = Counter({})
    for file in file_list:
        print(file)
        x = tracker.ChaseTextToData(file)
        x.run()

        total_dic += Counter(x.item_dict)

    labels = list(total_dic.keys())
    values = list(total_dic.values())
    trace = go.Pie(labels=labels, values=values)
    plotly.offline.plot([trace], filename='basic_pie_chart.html')