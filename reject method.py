import numpy as np
import matplotlib
import scipy.stats
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

X=[]
L=[]
M = 0.45
#print(M)
    #x = symbols('x')
    #m = M/integrate(M, (x, -5, 5))
for i in range(0,10000):
         Ｕ = np.random.random()
         U2 = np.random.random()
         T=10*U2-5
         L.append(T)
         y = (1 / (2 * math.pi) ** 0.5) * math.exp(-T**2)
         if M*U > y:
             continue
         else :
             X.append(T)
print(L)
print(X)
plt.figure(1)
plt.hist(X, bins=10, density=1, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("area")
# 显示纵轴标签
plt.ylabel("frequency")
# 显示图标题
plt.title("频数/频率分布直方图")

plt.figure(2)
plt.hist(L, bins=10, density=1, facecolor="blue", edgecolor="black", alpha=0.7)
plt.show()