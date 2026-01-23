import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity


alpha = 1.5 # alpha in (0,2)/{1}
beta = 0    # beta in [-1,1]
N = 10000

def generate_x(alpha, beta, N):
    def b(alpha, beta):
        temp1 = beta*np.tan(np.pi*alpha/2)
        temp2 = np.arctan(temp1)
        return temp2/alpha

    def s(alpha, beta):
        temp1 = beta*np.tan(np.pi*alpha/2)
        temp2 = 1 + temp1**2
        temp3 = 1/(2*alpha)
        return temp2**(temp3)

    u = np.random.uniform(-np.pi/2,np.pi/2,N)

    v = -np.log(1-np.random.uniform(0,1,N))

    b = b(alpha, beta)
    s = s(alpha, beta)

    def x(b,s,u,v):
        temp1 = np.sin(alpha*(u + b))
        temp2 = (np.cos(u))**(1/alpha)
        temp3 = np.cos(u - alpha*(u + b))/v
        temp4 = (1-alpha)/alpha
        return s*temp1/temp2*(temp3**temp4)
    return x(b,s,u,v)


def plot_data():

    fig, axs = plt.subplots(2,5,figsize = (12,8))
    fig.suptitle('Histograms of X for different alpha and beta')
    for i in range(2):
        for j in range(5):
            if i == 0:
                alpha = 0.5
            elif i == 1:
                alpha = 1.5
            elif i == 2:
                alpha = 2
            beta = -1 + j*0.5
            if i == 0 and j == 2:
                axs[i,j].set_xlim(-2e7,2e7)
            x = generate_x(alpha, beta, N)
            axs[i,j].set_yscale('log')
            axs[i,j].hist(x, bins = int(np.sqrt(N)), density = False)
            axs[i,j].set_title(f'alpha = {alpha}, beta = {beta}')
            axs[i,j].set_xlabel('random value')
            axs[i,j].set_ylabel('counts')

    plt.tight_layout()
    plt.show()


def tail_prob(alpha, beta, threshold, N):
    x = generate_x(alpha, beta, N)
    #print(len(x))
    #fig, ax = plt.subplots()
    #ax.hist(x, bins=100, density=True)
    count = np.sum(np.abs(x) > threshold)
    return count / N

def plot_tail_prob(thresholds, N, beta = 0):
    fig, axs = plt.subplots(2,1, figsize=(15, 12))
    
    for i in range(2):
        alpha = 0.5 if i == 0 else 1.5
        tail_probs = []
        for threshold in thresholds:
            prob = tail_prob(alpha, beta, threshold, N)
            tail_probs.append(prob)
        axs[i].hist(generate_x(alpha, beta, N), bins = int(np.sqrt(N)), density = False)
        axs[i].set_yscale('log')
        axs[i].set_title(f'Histogram for alpha={alpha}, beta={beta}')
        axs[i].set_xlabel('Random Value')
        axs[i].set_ylabel('Counts')
        #print(tail_probs)
        axs[i].annotate(f'Tail Probabilities:\n' + '\n'.join([f'P(|X| > {th}) = {tp:.5f}' for th, tp in zip(thresholds, tail_probs)]),
                        xy=(0.7, 0.7), xycoords='axes fraction',
                        bbox=dict(boxstyle="round,pad=1", fc="yellow", alpha=0.5))
    plt.tight_layout()
    plt.show()

def plot_ksd(alpha, beta, N):
    #fig, ax = plt.subplots(figsize=(10,6))
    x = generate_x(alpha, beta, N)
    counts, bin_edges = np.histogram(x, bins = 1000, density = True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    threshold = 7 if alpha > 1 else 3
    mask = (bin_centers > threshold) & (counts > 0)

    x_tail = bin_centers[mask]
    y_tail = counts[mask]  
    if len(x_tail) > 0 and len(y_tail) > 0: 
        log_x = np.log(x_tail)
        log_y = np.log(y_tail)
        #print(len(log_x), len(log_y))
        slope, intercept = np.polyfit(log_x, log_y, 1) 
        gamma_est = slope
        c_est = np.exp(intercept)
        #print(f'Estimated tail index (gamma) for alpha={alpha}, beta={beta}: {gamma_est}')
        return c_est, gamma_est
    else:
        return 0,0

def estimate_tail_index(alphas, N, num_it, beta = 0):
    clist = []
    gammalist = []
    for alpha in alphas:
        c_temp, gamma_temp = 0, 0
        for i in range(num_it):
            c, gamma = plot_ksd(alpha, beta, N)
            c_temp += c
            gamma_temp += gamma
        c_temp /= num_it
        gamma_temp /= num_it
        clist.append(c_temp)
        gammalist.append(gamma_temp)
    plt.plot(alphas, gammalist, marker='o')
    slope, intercept = np.polyfit(alphas, gammalist, 1)
    plt.plot(alphas, slope*np.array(alphas) + intercept, 
             linestyle = '--',
             label=f'Fit line: gamma={slope:.2f}alpha{intercept:.2f}')
    plt.xlabel('Alpha')
    plt.ylabel('Estimated Tail Index (Gamma)')
    plt.legend()
    plt.show()

def plot_multiple_a(N, beta = 0):
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))
    alphas = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    for ax, alpha in zip(axs.flatten(), alphas):
        x = generate_x(alpha, beta, N)
        ax.hist(x, bins = int(np.sqrt(N)), density = True, label = 'Histogram')
        #ax.set_yscale('log')
        ax.set_title(f'Histogram for alpha={alpha}, beta={beta}')
        ax.set_xlabel('Random Value')
        ax.set_ylabel('Probability Density')
        if alpha == 2:
            ax.plot(np.linspace(-8,8,1000), stats.norm.pdf(np.linspace(-8,8,1000),0, np.sqrt(2)),
                    label = 'N(0,2) PDF')
        ax.legend()
    plt.tight_layout()
    plt.show()




ini_alphas = np.arange(0.5, 1.6, 0.1)
alphas = ini_alphas[ini_alphas != 1.0]

if __name__ == "__main__":
    #estimate_tail_index(alphas=alphas, N=100000, num_it=50, beta=0)
    #plot_multiple_a(N=100000, beta=0)
    plot_data()