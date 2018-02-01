import numpy as np

"""array=np.array([[1,2,3],
               [2,3,4],
                [1,2,5]])
print(array)
print('number of dim:',array.ndim)
print('shape:',array.shape)
print('size',array.size)"""
"""array = np.array([[1,2,3],
                 [2,3,4]])
print(array)
print('number of dim:',array.ndim)
print('shipe:',array.shape)
print('size:',array.size)"""
#array：创建数组
#dtype：指定数据类型
#zeros：创建数据全为0
#ones：创建数据全为1
#empty：创建数据接近0
#arrange：按指定范围创建数据
#linspace：创建线段
a = np.array([[2,23,4,5],
                [2,32,4,23] ])
print(a)

b = np.zeros((3,4))
print(b)

c= np.ones((22,3))
print(c)

d=np.empty((2,2))
print(d)

e=np.arange(10,30,3)
print(e)

f = np.arange(15).reshape((3,5))
print ( f )

g=np.linspace(1 , 10 , 10).reshape(2,5 )
print(g)