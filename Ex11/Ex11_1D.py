#In this example, we use SciPy's interpolate1d function. Check the following webpage for its usage:
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x)

plt.xlabel('x [radius]')
plt.ylabel('y = sin(x)')
plt.plot(x,y,'y')  #yellow
#for matplotlib color usage, check :
#http://matplotlib.org/api/colors_api.html


n1 = 10
n2 = 30

delta1 = (2 * np.pi) / n1
delta2 = (2 * np.pi) / n2

x1 = np.arange(0, 2*np.pi + 0.001, delta1)
y1 = np.sin(x1)

f_nn = interpolate.interp1d(x1,y1, kind='nearest')
f_lin = interpolate.interp1d(x1,y1, kind='linear')
#f_quad = interpolate.interp1d(x1,y1, kind='quadratic')
f_cub = interpolate.interp1d(x1,y1, kind='cubic')


x2 = np.arange(0, 2*np.pi + 0.001, delta2)

y_nn = f_nn(x2)
y_lin = f_lin(x2)
#y_quad = f_quad(x2)
y_cub = f_cub(x2)


plt.plot(x2,y_nn,'r--')
plt.plot(x2,y_lin,'g--')
#plt.plot(x2,y_quad,'bs')
plt.plot(x2,y_cub,'b--')








