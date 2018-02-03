import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
# X,Y value
X = np.arange(-5, 5, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
# Z value
Z = np.sin(R)
# 画3D，restride为3D图上每个行宽，cstride为列宽
ax.plot_surface(X, Y, Z, rstride=1, cstride=2, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')  # zdir为等高线图与Z轴垂直
ax.set_zlim(-2, 2)
plt.xlabel("X",fontsize =14)
plt.ylabel("Y",fontsize=14)

plt.savefig('3D半圆图z.jpg')
plt.show()