import numpy as np

"""A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(A)
C = np.concatenate((A,B,B,A))
print(C)"""
A=np.arange(24).reshape((4,6))
print(A)
print(np.split(A,2,axis=1))

