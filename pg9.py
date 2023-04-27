
##https://realpython.com/linear-regression-in-python/

#Step 1: Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
#Step 2: Provide data
x = np.array([0,1,2,3,3,5,5,5,6,7,7,10]).reshape((-1, 1))
y = np.array([96,85,82,74,95,68,76,84,58,65,75,50])
print(x)
print(y)
# plot with various axes scales
plt.figure()

# linear plot
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.xlabel('hours')
plt.ylabel('score')
plt.grid(True)


# log plot
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.xlabel('hours')
plt.ylabel('score')
plt.grid(True)

# symmetric log plot
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog')
plt.title('symlog')
plt.xlabel('hours')
plt.ylabel('score')
plt.grid(True)

#scatter plot
plt.subplot(224)
plt.scatter(x, y )
plt.title('scatter')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

#Step 3: Create a model and fit it
model = LinearRegression()
model.fit(x, y)

