import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity
"""
inverse CDF of exponential distribution with mean m is:
-ln(1-x)
"""
bin_num = 30
width = 0.3
N = 1000

def plot_inverse_cdf(N, bin_num=bin_num, width=width):
    x_data = np.random.uniform(0,1,N)
    y_data = -np.log(1-x_data)
    mu, sigma = 0,0 
    for y in y_data:
        mu += y
    mu = mu / N
    print(f"Sample Mean = {mu}, theoretical mean = 1")
    for y in y_data:
        sigma += y**2 - mu**2
    var = sigma / N
    print(f"Sample Variance = {var}, theoretical variance = 1")

    idx = np.linspace(0,5,1000)
    exp_theoretical = np.e**(-idx)

    ks_density = ksdensity(y_data, width=width)



    fig, axs = plt.subplots(1,2,figsize = (15,6))

    axs[0].hist(y_data, bins = bin_num, density = "True", label = 'Random Generated Data')
    axs[0].plot(idx, exp_theoretical, '--', label = 'Theoretical Distribution')   
    axs[0].set_title('Histogram of random generated data from y = -ln(1-x)')
    axs[0].set_xlabel('random value')
    axs[0].set_ylabel('Density')
    axs[0].legend()

    axs[1].plot(idx, ks_density(idx), color = 'blue', label = 'Kernel Density Estimate')
    axs[1].plot(idx, exp_theoretical, '--', color = 'orange', label = 'Theoretical Distribution')
    axs[1].set_title(f'Kernel Density Estimate of random generated data with width = {width}')
    axs[1].set_xlabel('random value')
    axs[1].set_ylabel('Density')
    axs[1].legend()

    plt.legend()
    #plt.show()





