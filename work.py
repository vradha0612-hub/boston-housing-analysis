# YOUR CODE HERE
import pandas as pd
df = pd.read_csv("BostonHousing.csv", header =0)
print (df.head)
print(df.describe())
print(df.isnull().sum())
column1 = df.iloc[2,5]
print(column1)
if df.any().any():
    print ("contains zeros")
else:
    print ("no zeros")
import numpy as np
import matplotlib.pyplot as plt
x = (1, 2, 3, 4)
y = (2, 4, 5, 6)
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('graph')
plt.show()