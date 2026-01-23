import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity

"""
theoretical mean and sd for the histogram count
data as a function of N
"""

nlist = [100,1000,10000]
bin_num = 30


def paramater(N, bin_num):
    delta = N/bin_num
    return delta, np.sqrt(delta*(1-delta/N))

fig, axs = plt.subplots(1,3,figsize=(12,6))

for i in range(3):
    N = nlist[i]
    mu, sd = paramater(N, bin_num)
    unif_data = np.random.uniform(0,1,N)

    axs[i].hist(unif_data, bins = bin_num)
    axs[i].plot(unif_data, mu*np.ones(N), label = '$\mu$')
    axs[i].plot(unif_data, (mu+3*sd)*np.ones(N), label = '$\mu$ + 3$\sigma$')
    axs[i].plot(unif_data, (mu-3*sd)*np.ones(N), label = '$\mu$ - 3$\sigma$')
    axs[i].set_title(f'N = {N}')
    axs[i].legend(loc = 'lower right', fontsize = 8)

fig.suptitle('Histogram of Uniform random numbers with different N')
plt.show()
        




