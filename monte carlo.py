import numpy as np
import matplotlib
import scipy.stats
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
a=5
n=10000
x=[0]*n
g=[]
for i in range(0,n):
    l = np.random.random()
    x[i]=l*5
    y=np.exp(-x[i]**2/2)
    g.append(y)
s=sum(g)
print(x)
L=a*(1 / n) * (1 / (2 * np.pi) ** 0.5)*s
print(L)