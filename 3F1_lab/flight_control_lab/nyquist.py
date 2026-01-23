import numpy as np
import matplotlib.pyplot as plt
import cmath



k = 1.56
D = 0.57

def abs_G(w):
    return k / np.sqrt(w**4 + 100*w**2)

def phase_G(w):
    return -D*w+np.arctan(10*w, w**2)

def abs_G2(w):
    return -2/np.sqrt(w**2+1)

def phase_G2(w):
    return np.arctan(w)-w*0.1

    
def nyquist_plot(w_start=0.01, w_end=1000, num_points=10000):
    w = np.logspace(np.log10(w_start), np.log10(w_end), num_points)
    G_real = abs_G2(w) * np.cos(phase_G2(w))
    G_imag = abs_G2(w) * np.sin(phase_G2(w))

    plt.figure(figsize=(8, 8))
    plt.plot(G_real, G_imag, label='Nyquist Plot')
    plt.plot(G_real, -G_imag, linestyle='--', label='Conjugate')
    plt.plot([-1], [0], 'ro', label='-1+j0 Point')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.title('Nyquist Plot of $G_2(j \omega)$ with D = 0.1s')
    plt.grid()
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.legend()
    plt.show()

nyquist_plot()
