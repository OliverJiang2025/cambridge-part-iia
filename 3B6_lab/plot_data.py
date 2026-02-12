import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.odr as s_odr

# resistance in TIR used to read current
R = 20

# random and system error of measurements
v_ran, i_ran, L_ran = 0.005, 0.25, 0.5   # absolute error in respective units
v_sys, i_sys, L_sys = 0.03, 0.03, 0.03   # percentage error of 3%


def load_data():
    # read data from excel
    df = pd.read_excel("3B6_lab/3B6 data.xlsx")
    #print(df)

    # load data
    v = np.array(df['Voltage Probe Reading (V)'].tolist())
    i = np.array((df['Current Probe Reading (V)']/R*1000).tolist())
    L = np.array(df['Photodiode Probe Reading (mV)'].tolist())
    #print(intensities)
    return v, i, L

def plot_rawdata():
    fig, axs = plt.subplots(1, 2, figsize = (12,6))
    axs[0].scatter(i, L)
    axs[0].set_title('Intensity - Current plot')
    axs[1].scatter(i, v)
    axs[1].set_title('Voltage - Current plot')
"""
def linear_func(B, x):
    return B[0] * x + B[1]
"""
def odr_fit(i,v,L,fit_type):
    plt.figure(figsize=(8, 6))
    if fit_type == 'VI':
        mask = i > 20
        x = i[mask]
        y = v[mask]
        x_ran, x_sys = i_ran, i_sys
        y_ran, y_sys = v_ran, v_sys
        title = 'Linear Fit of Voltage against Current'
        plt.xlabel('Current (mA)')
        plt.ylabel('Voltage (V)')
        plt.scatter(x,y)
    elif fit_type == 'LI':
        mask = i > 75
        x = i[mask]
        y = L[mask]
        x_ran, x_sys = i_ran, i_sys
        y_ran, y_sys = L_ran, L_sys
        title = 'Linear Fit of Light Intensity against Current'
        plt.xlabel('Current (mA)')
        plt.ylabel('Intensity (mV)')
        plt.scatter(x,y)
    else:
        raise ValueError("Invalid type. Use 'IV' or 'IL'.")
    
    sx = np.sqrt(np.power(x_ran, 2) + np.power(x * x_sys, 2))
    sy = np.sqrt(np.power(y_ran, 2) + np.power(y * y_sys, 2))
    linear_model = s_odr.Model(lambda p, x: p[0] * x + p[1])

    data = s_odr.RealData(x, y, sx=sx, sy=sy)

    my_odr = s_odr.ODR(data, linear_model, beta0=[1.0, 0.0])
    output = my_odr.run()

    k, b = output.beta
    k_err, b_err = output.sd_beta 
    print(k,k_err,b,b_err)
    plt.errorbar(x, y, 
                 xerr=sx, 
                 yerr=sy, 
                 fmt='o', 
                 color='blue', 
                 ecolor='gray', 
                 capsize=3, 
                 label='Measured Data',
                 markersize=5,
                 elinewidth=1)
    x_fit = np.linspace(min(x) - 1, max(x) + 1, 100)
    y_fit = k * x_fit + b
    label_str = f'Linear Fit\n$1000k={1000*k:.4f} \pm {1000*k_err:.4f}$\n$b={b:.4f} \pm {b_err:.4f}$'
    plt.plot(x_fit, y_fit, 'r-', linewidth=1.5, label=label_str)
    plt.title(title, fontsize=14)
    plt.legend(loc='best', fontsize=10) 
    plt.grid(True, linestyle='--', alpha=0.6) #

if __name__ == '__main__':
    v, i, L = load_data()
    #plot_rawdata()
    odr_fit(i,v,L,'VI')
    plt.show()