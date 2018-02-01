"""import matplotlib.pyplot as plt
input_v=[1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_v,squares,linewidth=5)


plt.title("Square Numbers",fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=13)
plt.show()
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=10)
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=10)
plt.axis([0,1100,0,1100000])
plt.scatter(x_values,y_values,edgecolors='none',s=4)
plt.show()"""

"""
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=10)
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=10)
plt.axis([0,1100,0,1100000])
plt.scatter(x_values,y_values,c= (0,1,0.8),edgecolors='none',s=40)
plt.show()"""

import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none',s=40)
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=10)
plt.axis([0,1100,0,1100000])
plt.savefig('t.png',bbox_inches='tight')
plt.show()
