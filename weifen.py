from sympy import *
u=Function('u')
#x=Symbol('x')
z, omega0, gamma ,E ,L ,G ,M= sympy.symbols("z, omega_0, gamma ,E ,L ,G ,M", positive=True)
eq = (1-2*u(z))*(1+2*gamma*u(z))*(u(z).diff(z,1))**2 -(E**2/L**2) + ((u(z)**2)*(1-2*u(z))/(G**2 * M**2)) + (1-2*u(z))/L**2
result = dsolve(eq,u(x))
print(result)