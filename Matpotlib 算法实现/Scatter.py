import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)  # 平均数为0，方差为1
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

plt.scatter(X,Y,s = 75,c = T,alpha= 0.5)
#plt.xlim((-1.5,1.5))
#plt.xlim((-1.5,1.5))

plt.xticks(())
plt.yticks(())

plt.savefig('scatter1.png')
plt.show()