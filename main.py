import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean of sample:- ",population_mean)
print("std_deviation of sample:- ",std_deviation)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["claps"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

dataset = []

for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)


print("Mean of sample:- ",mean)
print("std_deviation of sample:- ",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["claps"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean =  random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()
