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

def inverse_cdf(N, bin_num=bin_num, width=width):
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
    return mu, var

def plot_mu_and_var():
    mus = []
    vars = []
    for i in range(100):
        mu, var = inverse_cdf(N)
        mus.append(mu)
        vars.append(var)
    idx = np.arange(1,101)
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(idx, mus, marker='o', linestyle='-', color='b', label='Sample Mean')
    plt.axhline(y=1, color='r', linestyle='--', label='Theoretical Mean')
    plt.title('Sample Mean vs Theoretical Mean')
    plt.xlabel('Trial')
    plt.ylabel('Mean')
    plt.ylim(0,2)
    plt.legend()
    plt.subplot(1,2,2)
    plt.plot(idx, vars, marker='o', linestyle='-', color='g', label='Sample Variance')
    plt.axhline(y=1, color='r', linestyle='--', label='Theoretical Variance')
    plt.title('Sample Variance vs Theoretical Variance')
    plt.xlabel('Trial')
    plt.ylabel('Variance')
    plt.ylim(0,2)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_mu_and_var()







