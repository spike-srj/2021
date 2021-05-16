from scipy import integrate
import numpy as np
import math
'''
def f(x, n):
    return x**2*np.exp(-x)#n*(1/((2**(n/2))*(math.gamma(n/2))))*((n*x)**((n/2)-1))*(math.exp(-n*x/2))
v, err = integrate.quad(f, 0, np.inf , args = 4)
print(v)
'''
def f(x):
    return x**2*np.exp(-x)#n*(1/((2**(n/2))*(math.gamma(n/2))))*((n*x)**((n/2)-1))*(math.exp(-n*x/2))
v, err = integrate.quad(f, 0, np.inf )
print(v)