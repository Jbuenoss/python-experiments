import numpy as np
from numpy import random
import matplotlib.pyplot as plt


list0 = [1, 2, 3, 4, 5]
nArray = np.array(list0, dtype=np.uint8) #ui = unsigned integer
print(nArray)
print(nArray.dtype)

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(type(x))

print("functions")
print(np.arange(1,10,2))
y = np.linspace(1, 5, 10)
print(x) #para float
print(y.dtype)
print(np.zeros((2,3)))
print(y.size)

a = np.random.randint(101, size=(2,3))
b = np.random.randint(2, 100, 10)
print(a)
print(b)

x[0][0] = 10.0
x.itemset((0,1), 30.0)
print(x)
print(x.size)
print(x.shape)
print("\n")
print(np.take(x, [0,3,5]))