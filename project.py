from collections import namedtuple
import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("project_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
population_sd=statistics.stdev(data)
print("standard deviation of population",population_sd)
print("mean of population", population_mean)
fig=ff.create_distplot([data],["reading time"],show_hist=False)

fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1], mode="lines" ,name="mean"))
fig.show()

def random_set_ofmean(counter):
    data_set=[]
    for i in range(0, counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)

    mean=statistics.mean(data_set)
    return mean
def setup():
    mean_list=[]
    for i in range (0,100):
        set_of_means=random_set_ofmean(30)
        mean_list.append(set_of_means)
    sample_mean=statistics.mean(mean_list)
    sample_sd=statistics.stdev(mean_list)
    print("mean of sample",sample_mean)
    print("standard deviation of sample",sample_sd)

    fig=ff.create_distplot([mean_list],["temperature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,1], mode="lines" ,name="mean"))
   
    fig.show()
    z_score=(sample_mean-population_mean)/population_sd
    print("z score", z_score)

setup()