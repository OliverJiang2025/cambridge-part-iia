import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity

N = 1000
num_bins = 50
width = 0.4 # width of ks density function 


def plot_data(N, num_bins, width):
    # plot gaussian data and uniform data with length N
    # in a histogram with bins number of num_bins
    gauss_data = np.random.normal(0, 1, N)
    unif_data = np.random.uniform(0, 1, N)

    gauss_x = np.linspace(-5, 5, N)
    gauss_pdf = stats.norm.pdf(gauss_x, 0, 1)

    unif_x = np.linspace(0, 1, N)
    unif_pdf = np.ones(N)
    
    ks_density = ksdensity(gauss_data, width=width)
    ks_density_unif = ksdensity(unif_data, width=width)

    fig, [[ax1,ax2],[ax3,ax4]] = plt.subplots(2,2,figsize = (12,6))
  
    ax1.plot(gauss_x, gauss_pdf, 
                     label = 'Theoretical Distribution')
    ax1.plot(gauss_x, ks_density(gauss_x),
                     label = 'KSD')
    ax1.set_title("KSD of Gaussian random numbers")
    ax1.set_xlabel('random value')
    ax1.set_ylabel('probability density')
    ax1.legend()    
    

    ax2.hist(gauss_data, bins = num_bins, density = True,
                     label = 'random Gaussian number')
    ax2.plot(gauss_x, gauss_pdf,
                     label = 'Gaussian curve')
    ax2.set_title("Histogram of Gaussian random numbers")
    ax2.set_xlabel('random value')
    ax2.set_ylabel('probability density')
    ax2.legend()



    mu = 0.5
    sigma = width
    x = np.linspace(-1,2,N)
    y = np.where((x >= 0) & (x <= 1), 1, 0)
    ax3.plot(x, stats.norm.pdf(x, mu, sigma**(1/2)),
                     label = 'Gaussian curve')
    ax3.plot(x, ks_density_unif(x),
                     label = 'KSD')
    ax3.plot(x,y,'--',
                     label = 'Uniform PDF')
    ax3.set_title('KSD of Uniform random numbers')
    ax3.set_xlabel('random value')
    ax3.set_ylabel('probability density')
    ax3.legend()




    ax4.hist(unif_data, bins = num_bins, density = True,
                     label = 'random uniform number')
    ax4.plot(unif_x, unif_pdf,
                     label = 'uniform curve')
    ax4.set_title('Histogram of Uniform random numbers')
    ax4.set_xlabel('random value')
    ax4.set_ylabel('probability density')
    ax4.legend()



    plt.tight_layout(rect = [0,0,1,0.92])
    plt.suptitle(f'Comparison of distributions (kernel width = {width})')
 
    plt.show()

widths = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]



def different_widths(widths):
    fig, axs = plt.subplots(2, 3, figsize=(15, 8)) 
    for ax, w in zip(axs.flatten(), widths):
        unif_data = np.random.uniform(0, 1, N)
        ks_density = ksdensity(unif_data, width=w)
        x = np.linspace(-1, 2, N)
        ax.plot(x, ks_density(x), label='KSD')
        ax.plot(x, np.where((x >= 0) & (x <= 1), 1, 0), linestyle = '--', label='Theoretical curve')
        ax.set_title(f'KSD with width = {w}')
        ax.set_xlabel('random value')
        ax.set_ylabel('probability density')
        ax.legend()
    plt.tight_layout()
    plt.suptitle('KSD with Different Kernel Widths', y=1.02)
    plt.show()


if __name__ == "__main__":
    #plot_data(N, num_bins, width)\
    different_widths(widths)

