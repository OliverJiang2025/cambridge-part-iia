import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.odr import ODR, Model, RealData
# resistance in TIR used to read current
R = 20

# read data from excel
df = pd.read_excel("3B6_lab/3B6 data.xlsx")
#print(df)

# load data
v = np.array(df['Voltage Probe Reading (V)'].tolist())
i = np.array((df['Current Probe Reading (V)']/R*1000).tolist())
L = np.array(df['Photodiode Probe Reading (mV)'].tolist())
#print(intensities)

def plot_rawdata():
    fig, axs = plt.subplots(1, 2, figsize = (12,6))
    axs[0].scatter(i, L)
    axs[0].set_title('Intensity - Current plot')
    axs[1].scatter(i, v)
    axs[1].set_title('Voltage - Current plot')
    plt.show()

def linear_func(B, x):
    return B[0] * x + B[1]

def odr_fit(i,v,L,fit_type):
    plt.figure(figsize=(8, 6))
    if fit_type == 'VI':
        mask = i > 20
        x = i[mask]
        y = v[mask]
        plt.xlabel('Current (mA)')
        plt.ylabel('Voltage (V)')
    elif fit_type == 'LI':
        x = i[8:]
        y = L[8:]
        plt.xlabel('Current (mA)')
        plt.ylabel('Intensity (mV)')
    else:
        raise ValueError("Invalid type. Use 'IV' or 'IL'.")
  

if __name__ == '__main__':
    plot_rawdata()
    print(v)
    print(i)
    odr_fit(i,v,L,'VI')
   