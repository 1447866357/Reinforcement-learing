import numpy as np
"""a = np.array([[1,1],
             [0,1]])
b = np.arange(4).reshape((2,2))
c= a*b
d=np.dot(a,b)
c_dot=a.dot(b)
print(c_dot)
print(d)
"""
"""a =np.random.random((2,4))
print(a)
print(np.sum(a,axis=1))
print(np.min(a,axis=0))
print(np.max(a,axis=1))
"""
#A = np.arange(14,2,-1).reshape((3,4))
"""print(np.argmax(A))
print(np.argmin(A))
print(np.mean(A))
print(A.mean())
print(np.median(A))
print(np.cumsum(A).reshape((3,4)))
print(np.diff(A))
print(np.nonzero(A))
print(np.sort(A))
print(A)
#print(np.clip(A,5,14))
print(np.mean(A,axis=0))
print(np.mean(A,axis=1))"""
A=np.arange(3,15).reshape((3,4))
print(A)
print(A.flatten())
for item in A.flat:
    print(item)
""""
#print(A[2,1:3])
for row in A:
    print((row))
print(A.T)
for column in A.T:
    print(column)"""