import scipy
import pandas as pd
import plotly.figure_factory as ff

read = pd.read_csv('PRO-108_2.csv')

sr_no = read['Sr.No'].to_list()
brand = read['Mobile Brand'].to_list()
avg_rating = read['Avg Rating'].to_list()

graph = ff.create_distplot([avg_rating] , ['Brand'] , show_hist = False , show_rug = False)
graph.show()