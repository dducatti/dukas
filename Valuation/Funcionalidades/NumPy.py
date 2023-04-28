import numpy as np

dir(np)                                 #all functions contained in Numpy
x = np.array(dir(np))
len(x)                                  # generate an array containing all functions
help(np.std)                            # information about sdt()
x = np.array([[1, 2, 3], [3, 4, 6]])    # 2 by 3 matrix
np.size(x)                              # number of data items
np.size(x, 1)                           # show number of columns
np.std(x)                               # standard deviation
np.std(x, 1)
total = x.sum()
z = np.random.rand(50)                  # 50 random obs from [0.0, 1]
y = np.random.normal(size=100)          # from standard normal
r = np.array(range(0, 100), float) / 100# from 0, 0.1, to .99

np.array([100, 0.1, 2], float)          # specified array should contain the same data type

x1 = [1, 2, 3, 20]
y1 = np.array(x1, dtype=float)            # all items are float




