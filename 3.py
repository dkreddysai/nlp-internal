import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
data=np.random.randn(50)
plt.style.use('ggplot')
plt.style.use('dark_background')
plt.plot(data,linestyle="dotted",linewidth=2)
plt.show()
