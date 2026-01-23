import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

nlist = [100,1000,10000]
bin_num = 30

def cdf(x):
    return scipy.stats.norm.cdf(x, 0, 1)

def plot_hist(nlist, bin_num = bin_num):
    fig, axs = plt.subplots(1, 3, figsize=(20,6))
    for N in nlist:
        ax = axs[np.where(np.array(nlist)==N)[0][0]]
        gauss_data = np.random.normal(0, 1, N)
        counts, bin_edges = np.histogram(gauss_data, bins=bin_num, density=False)
        bin_width = np.diff(bin_edges)
        for idx in range(len(counts)):
            #print(f'Bin {idx+1}: [{bin_edges[idx]:.2f}, {bin_edges[idx+1]:.2f}) - Count: {counts[idx]}')
            p_j = cdf(bin_edges[idx+1]) - cdf(bin_edges[idx])
            mu = N * p_j
            sigma = np.sqrt(N * p_j * (1 - p_j))
            mu_label = '$\mu$' if idx == 0 else None
            plussigma_label = '$\mu + 3\sigma$' if idx == 0 else None
            minussigma_label = '$\mu - 3\sigma$' if idx == 0 else None
            ax.bar(x = bin_edges[idx], 
                height = mu,
                width = bin_width[idx],
                alpha = 0.5,
                color = 'orange',
                zorder = 3,
                label = mu_label
                )
            ax.bar(x = bin_edges[idx], 
                height = mu+3*sigma,
                width = bin_width[idx],
                alpha = 0.5,
                color = 'green',
                zorder = 2,
                label = plussigma_label
                )
            ax.bar(x = bin_edges[idx], 
                height = mu-3*sigma,
                width = bin_width[idx],
                alpha = 0.5,
                color = 'grey',
                zorder = 4,
                label = minussigma_label
                )
        ax.set_title(f'N={N}')
        ax.set_xlabel('Random Value')
        ax.set_ylabel('Frequency')
        ax.hist(gauss_data, bins=bin_num, density=False, label='Gaussian RVs', zorder=1)
        ax.legend()
    fig.suptitle('Histogram of Gaussian random numbers with different N')
    plt.show()

def plot_var(N, bin_num = bin_num):
    gauss_data = np.random.normal(0, 1, N)
    counts, bin_edges = np.histogram(gauss_data, bins=bin_num, density=False)
    bin_width = np.diff(bin_edges)
    vars = []
    probs = []
    for idx in range(len(counts)):
        #print(f'Bin {idx+1}: [{bin_edges[idx]:.2f}, {bin_edges[idx+1]:.2f}) - Count: {counts[idx]}')
        p_j = cdf(bin_edges[idx+1]) - cdf(bin_edges[idx])
        probs.append(p_j)
        var = N * p_j * (1 - p_j)
        vars.append(var)
    fig, [ax0, ax1] = plt.subplots(1,2, figsize=(15,6))
    ax0.bar(x = bin_edges[:-1],
            height = vars,
            label = 'Variance')
    ax1.plot(probs, vars, color = 'red',
             label = 'Variance vs Probability')
    ax0.set_title(f'Variance of histogram height for N={N}')
    ax0.set_xlabel('Random Value')
    ax0.set_ylabel('Variance')
    ax1.set_title(f'Variance vs Probability for N={N}')
    ax1.set_xlabel('$p_j$')
    ax0.legend()
    ax1.legend()
    plt.show()




plot_var(10000)