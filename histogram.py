# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 17:58:41 2016

@author: Zachery McKinnon
"""

import pandas as pd
import matplotlib.pyplot as plt

def histogram(pandas_df, column_name, bins):
    """Creates a histogram of the column_name of a pandas_df 
    with a specified number of bins."""
    
    #sets minimum and maximum x values rounded to 10 for the plot
    x_min = int(pandas_df[column_name].min()) - int(pandas_df[column_name].min())%10
    x_max = int(pandas_df[column_name].max()) + 10 - int(pandas_df[column_name].max())%10
    
    #plots histogram
    plt.figure(figsize=(12, 9))
    n, _, _ = plt.hist(pandas_df[column_name], alpha = 0.5, bins = bins)
    
    #determines max y value rounded to 10 for the plot
    y_max = int(n.max() + 10 - n.max()%10)
    
    #formats the plot
    ax = plt.subplot()
    ax.spines["top"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False) 
    ax.set_ylim([0, y_max])
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    if y_max <50:
        for y in range(0, y_max+1, 5):    
            plt.plot(range(x_min,x_max+1), [y] * len(range(x_min,x_max+1)),
                     "--", lw=0.5, color="black", alpha=0.3)
    else:
         for y in range(0, y_max+1, 10):    
            plt.plot(range(x_min,x_max+1), [y] * len(range(x_min,x_max+1)),
                     "--", lw=0.5, color="black", alpha=0.3)
    plt.xlabel(column_name, fontsize=16)
    plt.ylabel("Count", fontsize=16)
