import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import scipy.stats as st


T=[0]*1000
L=[0]*1000
"""
F(t)=(1/math.sqart(2*Pi))

"""
#print(l)#randint(low=1, high=100, size=10**3)
for i in range(0,10**3):
    l = np.random.random()
    L[i]=l
#print( random.uniform(0.0,1) )
    print(L[i])
    T[i] = st.norm.ppf(L[i])  #st.norm.ppf(0.975) 标准正态分布在 0.975 处的逆函数值
#print(T)

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
# 随机生成（10000,）服从正态分布的数据
data = T
print(data)
"""
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
plt.hist(data, bins=10, density=1, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("区间")
# 显示纵轴标签
plt.ylabel("频数/频率")
# 显示图标题
plt.title("频数/频率分布直方图")
plt.show()

