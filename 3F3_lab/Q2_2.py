import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N = 1000
x_data = np.random.uniform(0, 2*np.pi, N)
y_data = np.sin(x_data)
y1_data = np.minimum(np.sin(x_data), 0.7)

idx = np.linspace(-1, 0.7, N)
theoretical = 1/(np.pi * np.sqrt(1 - idx**2))

plt.hist(y1_data, bins=50, density=True, 
         label='histogram of $y= min(sin(x),0.7)$')
plt.plot(idx, theoretical, linestyle='--', label='Theoretical PDF')
#plt.axvline(x = 0.7, ymin = 0, ymax = 0.184,
  #          color = 'orange', linestyle = '--')
#plt.scatter(x = 0.7, y = 0.184)
plt.xlabel('y = sin(x)')
plt.ylabel('Density')
plt.title('Histogram of y=min(sin(x),0.7) and Theoretical PDF')
plt.legend()
plt.show()