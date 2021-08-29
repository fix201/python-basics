# pip install numpy

my_list = [1,2,3]

import numpy as np
arr = np.array(my_list)
print(arr)
arr.reshape(-1,-1)
print(arr)

# ones
print(np.ones(4))

# arange
print(np.arange(4,7))

# linspace
print(np.linspace(1, 2, 10))

# eye
print(np.eye(4,4, 1))

# random
print(np.random.randint(3))