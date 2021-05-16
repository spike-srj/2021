import numpy as np
import matplotlib
import scipy.stats
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

x = np.linspace(0,8,10000)
color = ["blue","green","darkgrey","darkblue","orange"]
#print(x)
#n=4
data=[]
#data2=[[]]*3
for n in range(2,8,2):

    for i in range(0,10000):
        y=n*(1/((2**(n/2))*(math.gamma(n/2))))*((n*x[i])**((n/2)-1))*(math.exp(-n*x[i]/2))
        data.append(y)


    #data2.extend(data)

    print(data)
    #print(len(data2))

    plt.plot(x,data,c=color[int((n/2))-1])
    #因爲data.append 一直疊加，所以要在下一輪開始前清空data
    data=[]

plt.title('chi-square')
plt.show()


