import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import statsmodels
import wrangle
from sklearn.model_selection import train_test_split
from matplotlib.pyplot import figure

#create pairplot 
def create_pairplots(df):
    cats = df.fips
    sns.pairplot(df, kind='reg')
    conts = df['bedroomcnt','bathroomcnt','calculatedfinishedsquarefeet','taxvaluedollarcnt','yearbuilt']
    print(plt.show())
    

#create a new feature bathroom to bedroom count
def bathroom_to_bedroom(df):
    bath_bed_ratio = df['bath_bed_ratio'] = df['bathroomcnt']/ df['bedroomcnt']
    return bath_bed_ratio

#create three different plots to visualize categoric and numeric variables in the dataset
def plot_categorical_and_continuous_vars(cats, vars, df):
    cats = ['fips']
    conts = ['bedroomcnt','bathroomcnt','calculatedfinishedsquarefeet','taxvaluedollarcnt','yearbuilt']
    # return a heatmap
    correlation_table = df.corr()
    # sns.heatmap(correlation_table,annot=True, vmin=-1, vmax=1)
    sns.heatmap(correlation_table, cmap='Blues', annot=True,vmin=-1, vmax=1)
    plt.show()
    #make plot 2
    df.bathroomcnt.plot.hist()
    plt.show()
    #make plot 3
    df.bedroomcnt.plot.hist()
    plt.show()