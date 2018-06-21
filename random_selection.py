# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:07:24 2018

@author: Sunny Parihar
"""
#Random Selection.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
#Implementing the random Selection.
import random
N = 10000
d = 10
ads_selected=[]
total_reward= 0
for n in range(0,N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward+reward
#Visualizing the histogram (Results).
plt.hist(ads_selected)
plt.title('Histogram of Selected Ads.')
plt.xlabel('Ads')
plt.ylabel('Number of times ad has been selected')
plt.show()