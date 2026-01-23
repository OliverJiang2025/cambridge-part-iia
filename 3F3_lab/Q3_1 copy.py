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
Nlist = np.arange(0,200,1,dtype = int) # number of samples
M = 100 # number of trials of each set of samples

def mu_est(N, bin_num=bin_num):
    x_data = np.random.uniform(0,1,N)
    y_data = -np.log(1-x_data)
    mu = 0
    for y in y_data:
        mu += y
    mu = mu / N
    return mu

def MC_MSE(Nlist,M):
    mses = []
    for n in Nlist:
        mus = []
        for i in range(M):
            mu = mu_est(n)
            mus.append(mu)
        mus = np.array(mus)
        mse = np.mean((mus - 1)**2)
        mses.append(mse)
    plt.plot(Nlist, mses, label = 'MSE')
    plt.plot(Nlist, 1/Nlist,'--',label = '1/N')
    plt.xlabel('Number of samples N')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.title('MSE of Sample Mean vs Number of Samples N')
    #plt.xscale('log')
    #plt.plot(idx, 1/np.sqrt(idx) ,'--')
    plt.legend()
    plt.show()
    



if __name__ == "__main__":
    MC_MSE(Nlist,M)







