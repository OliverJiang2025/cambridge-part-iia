import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 6
b = 3
num_bin = 50
N = 1000

x_data = np.random.normal(0, 1, N)
y_data = a * x_data + b
g_data = x_data**2

x = np.linspace(-5,5,N)
x_theoretical = stats.norm.pdf(x, 0, 1)

y = np.linspace(b-5*a,b+5*a,N)
y_theoretical = stats.norm.pdf(y, b, a)

g = np.linspace(0,10,N)
g_theoretical = np.e**(-g/2)/(np.sqrt(2*np.pi*g))


"""
axs[0].hist(x_data, bins = num_bin, density = True)
axs[0].plot(x, x_theoretical, linestyle = '--', label = 'theoretical distribution')
axs[0].axvline(0, color = 'red', linestyle = '--', label = '$\mu$')
axs[0].set_title('Standard Gaussian Distribution, x')
axs[0].legend()


axs[1].hist(y_data, bins = num_bin, density = True)
axs[1].plot(y, y_theoretical, linestyle = '--', label = 'theoretical distribution')
axs[1].axvline(b, color = 'red', linestyle = '--', label = '$\mu$')
axs[1].set_title(f'Distribution of y=ax+b ($\sigma^2$ = a = {a}, $\mu$ = b = {b})')
axs[1].legend()
"""
plt.hist(g_data, bins = num_bin, density = True, label = 'histogram of $y=x^2$')
plt.plot(g, g_theoretical, linestyle = '--', label = 'theoretical distribution')
plt.ylim(0,2)
plt.title('Distribution of y=$x^2$')

plt.legend()


plt.show()