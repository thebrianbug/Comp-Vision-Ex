#In this example, we use SciPy's interpolate2d function. Check the following webpage for its usage:
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp2d.html

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy import interpolate

sigma = 1.5

xyRange = np.arange(-4, 4.01, 0.2)      # dense

xyRange2 = np.arange(-4, 4.01, 0.8)     #coarse

xx, yy = np.meshgrid(xyRange, xyRange)
xx2, yy2 = np.meshgrid(xyRange2, xyRange2)

z = np.exp((-xx**2 - yy**2)/(2.0*(sigma**2)))
z2 = np.exp((-xx2**2 - yy2**2)/(2.0*(sigma**2)))

f_lin = interpolate.interp2d(xyRange2, xyRange2, z2, kind='linear')
f_cub = interpolate.interp2d(xyRange2, xyRange2, z2, kind='cubic')

z_lin = f_lin(xyRange, xyRange)
z_cub = f_cub(xyRange, xyRange)


fig1 = plt.figure(1)
ax = Axes3D(fig1)
ax.plot_surface(xx, yy, z, rstride=1, cstride=1, cmap='hot')


fig2 = plt.figure(2)
ax = Axes3D(fig2)
ax.plot_surface(xx, yy, z_lin, rstride=1, cstride=1, cmap='hot')

fig3 = plt.figure(3)
ax = Axes3D(fig3)
ax.plot_surface(xx, yy, z_cub, rstride=1, cstride=1, cmap='hot')


plt.show()  

