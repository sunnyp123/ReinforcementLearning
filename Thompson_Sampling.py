# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:17:21 2018

@author: Sunny Parihar
"""
#Thompson Sampling.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
#Implementing the thompson sampling.
import random
N = 10000
d = 10
ads_selected = []
numbers_of_rewards_1 = [0]*d
numbers_of_rewards_0 = [0]*d
total_reward = 0
for n in range(0,N):
    ad = 0
    max_random = 0
    for i in range(0,d):
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1,numbers_of_rewards_0[i]+1)\
        if(random_beta>max_random):
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward + reward
    if(reward==0):
        numbers_of_rewards_0[ad]  = numbers_of_rewards_0[ad] + 1
    else:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1