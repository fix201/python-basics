from cProfile import label
import numpy as np
import pandas as pd
from numpy.random import randn

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(pd.Series(data=my_data, index=labels))

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df['new'] = df['W']+df['Z']
print(df)
df.drop('E',axis=0)
print(df.drop('Z',axis=1))

print(df.shape)
